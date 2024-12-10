"""
Arquitectura basada en (micro)servicios REST - Servidor
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas


def get_db_connection():
    conn = sqlite3.connect('mi_base_de_datos.db')
    conn.row_factory = sqlite3.Row
    return conn

with get_db_connection() as conn:
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS proyectos;")
    conn.commit()
    cursor.execute(
        """CREATE TABLE proyectos (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            descripcion TEXT, 
            imagen TEXT,
            conclusion TEXT
        )"""
    )
    conn.commit()

@app.route('/add', methods=['POST'])
def addProject():
    data = request.json
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO proyectos (titulo, descripcion, imagen, conclusion) VALUES (?, ?, ?, ?)',
                       (data['titulo'], data['descripcion'], data['imagen'], data['conclusion']))
        conn.commit()
    return jsonify({"mensaje": "Proyecto añadido con éxito"})

@app.route('/delete', methods=['DELETE'])
def deleteProject():
    data = request.json
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM proyectos WHERE id = ?', (data["id"],))
        conn.commit()
        return jsonify({"mensaje": "Proyecto eliminado con éxito"})

@app.route('/get', methods=['GET'])
def getProject():
    titulo = request.args.get('titulo', '')
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM proyectos WHERE titulo LIKE ?', (titulo + '%',))
        proyectos = cursor.fetchall()
    proyecto_list = [dict(proyecto) for proyecto in proyectos]
    return jsonify({"resultado": proyecto_list})

@app.route('/getProjects', methods=['GET'])
def getProjects():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM proyectos')
        proyectos = cursor.fetchall()
    proyectos_list = [dict(proyecto) for proyecto in proyectos]
    return jsonify({"resultado": proyectos_list})

@app.route('/edit', methods=['PUT'])
def editProject():
    data = request.json
    project_id = data['id']
    titulo = data['titulo']
    descripcion = data['descripcion']
    imagen = data['imagen']
    conclusion = data['conclusion']

    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE proyectos SET titulo = ?, descripcion = ?, imagen = ?, conclusion = ? WHERE id = ?',
                       (titulo, descripcion, imagen, conclusion, project_id))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"mensaje": "Proyecto no encontrado"}), 404

    return jsonify({"mensaje": "Proyecto actualizado con éxito"})

if __name__ == "__main__":
    app.run(port=9000)
