<template>
  <div>

    <!-- Lista de proyectos en formato caja -->
    <div class="projects-container">
      <div v-for="project in projects" :key="project.id" class="project-card">
        <h3>{{ project.titulo }}</h3>
        <img :src="project.imagen" alt="Imagen del proyecto" class="project-img" />
        <p>{{ project.descripcion }}</p>
        <p><strong>Conclusión:</strong> {{ project.conclusion }}</p>
        <button class="delete-button" @click="deleteProject(project.id)">Eliminar Proyecto</button>
        <button class="edit-modal-button" @click="openEditModal(project)">Editar Proyecto</button>      </div>
    </div>

    <button @click="showModal = true" class="btn-add-project">Añadir Proyecto</button>

    <div v-if="showModal" class="modal">
      <h3>Añadir Nuevo Proyecto</h3>
      <input v-model="newProject.titulo" placeholder="Título del proyecto" />
      <textarea v-model="newProject.descripcion" placeholder="Descripción del proyecto"></textarea>
      <input v-model="newProject.imagen" placeholder="URL de la imagen del proyecto" />
      <textarea v-model="newProject.conclusion" placeholder="Conclusión del proyecto"></textarea>
      

      <button @click="saveProject">Guardar</button> 
      <button @click="closeModal">Cerrar</button>
    </div>

    
    <div v-if="showEditModal" class="edit-modal">
      <h3>Editar Proyecto</h3>
      <input v-model="currentProject.titulo" placeholder="Título del proyecto" />
      <textarea v-model="currentProject.descripcion" placeholder="Descripción del proyecto"></textarea>
      <input v-model="currentProject.imagen" placeholder="URL de la imagen del proyecto" />
      <textarea v-model="currentProject.conclusion" placeholder="Conclusión del proyecto"></textarea>

      <button @click="saveChanges">Guardar cambios</button>
      <button @click="closeEditModal">Cerrar</button>
    </div>

    
  </div>
</template>

<script>
export default {
  props: ['projects'],
  data() {
    return {
      searchQuery: '',
      showModal: false,
      showEditModal: false,
      newProject: {
        id: '',
        titulo: '',
        descripcion: '',
        imagen: '',
        conclusion: ''
      },
    };
  },
  methods: {
    async saveProject() {
      if (this.newProject.titulo && this.newProject.descripcion && this.newProject.conclusion && this.newProject.imagen) {
        const projectToAdd = {
          titulo: this.newProject.titulo,
          descripcion: this.newProject.descripcion,
          imagen: this.newProject.imagen, 
          conclusion: this.newProject.conclusion,
        };
        console.log('Nuevo proyecto:', projectToAdd);
        this.$emit('add-project', projectToAdd);
        this.newProject = { id: '', titulo: '', descripcion: '', imagen: '', conclusion: '' }; 
        this.closeModal(); 
      }
    },
    deleteProject(projectId) {
      this.$emit('delete-project', projectId);
    },
    async saveChanges() {
      // Validar que todos los campos estén llenos
      if (this.currentProject.titulo && this.currentProject.descripcion && this.currentProject.conclusion && this.currentProject.imagen) {
        await this.$emit('edit-project', this.currentProject); // Emitir el evento al componente padre para guardar los cambios
        this.closeEditModal(); // Cerrar el modal
      }
    },
    openEditModal(project) {
      this.currentProject = { ...project }; // Cargar los datos del proyecto a editar
      this.showEditModal = true; // Mostrar el modal de edición
    },
    closeEditModal() {
      this.showEditModal = false; // Ocultar el modal de edición
      this.resetCurrentProject();
    },
    closeModal() {
      this.showModal = false;
    }
  }
};
</script>




<style scoped>

.search-bar {
  margin: 20px auto 20px 0; /* Margen superior e inferior automáticos, margen izquierdo 0, y margen derecho */
  display: block;
  padding: 10px 40px; /* Añade espacio para el icono */
  width: 50%;
  font-size: 18px;
  border: none;
  border-radius: 50px; /* Bordes más redondeados */
  background-color: #f2f2f2; /* Color de fondo suave */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Sombra sutil */
  transition: all 0.3s ease; /* Transición suave */
  margin-right: 20px; /* Añade el margen derecho */
}

.search-bar:focus {
  outline: none; /* Elimina el contorno en el enfoque */
  box-shadow: 0 0 10px rgba(0, 132, 255, 0.5); /* Sombra al enfocar */
}

.search-bar::placeholder {
  color: #aaa; /* Color del texto del placeholder */
  font-style: italic; /* Estilo itálico para el placeholder */
}

/* Icono de búsqueda */
.search-icon {
  position: absolute; /* Posiciona el icono */
  left: 15px; /* Distancia del borde izquierdo */
  top: 50%; /* Centra verticalmente */
  transform: translateY(-50%); /* Ajusta la alineación */
  color: #888; /* Color del icono */
  pointer-events: none; /* Ignora eventos del mouse */
}


.projects-container {
  display: flex;
  flex-wrap: wrap;
  gap: 25px;
  justify-content: center;
}

.project-card {
  background-color: #fff;
  padding: 50px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 400px; /* Aumenta el ancho de la caja si es necesario */
  text-align: center;
  transition: transform 0.3s ease;
  font-family: 'TuFuentePreferida', sans-serif; /* Asegúrate de utilizar la misma fuente que el resto */
}

/* Asegúrate de que h3, h4 y p también tengan la misma fuente */
.project-card h3,
.project-card h4,
.project-card p {
  font-family: 'TuFuentePreferida', sans-serif; /* Usa la misma fuente */
  color: #333; /* Puedes elegir otro color que contraste bien */
}

.project-card ul {
  list-style: none; /* Quita el estilo de la lista si lo prefieres */
  padding: 0; /* Elimina el padding */
}

.project-card li {
  font-family: 'TuFuentePreferida', sans-serif; /* Asegura que el texto dentro de las listas también use la misma fuente */
  color: #333; /* Puedes elegir otro color que contraste bien */
}



.project-img {
  max-width: 60%; /* Asegúrate de que la imagen no se desborde */
  height: auto; /* Mantiene la proporción de la imagen */
  width: 80%; /* Ajusta el ancho de la imagen al 80% de la caja */
  margin: 0 auto; /* Centra la imagen horizontalmente */
  display: block; /* Asegura que la imagen se comporte como un bloque */
}

.delete-button {
  background-color: #4fc3f7; /* Color coral */
  color: white;
  margin-top: 10px;
  width: 100%;
  padding: 10px 15px;
  border: none;
  border-radius: 25px; /* Bordes redondeados */
  font-size: 16px;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Sombra sutil */
  transition: background-color 0.3s, transform 0.2s; /* Transiciones suaves */
}

.delete-button:hover {
  background-color: #ff4d4d; /* Color más oscuro al hacer hover */
  transform: scale(1.05); /* Aumentar ligeramente el tamaño al hacer hover */
}

.delete-button:focus {
  outline: none; /* Sin borde al hacer foco */
}

.modal {
  background-color: #3f9b6a; /* Color más fuerte que armoniza con el resto */
  padding: 40px 30px; /* Mantener el padding */
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(36, 167, 158, 0.1);
  width: 600px; /* Ancho de la caja */
  margin: 20px auto;
  color: white; /* Color del texto */
}

input[type="text"],
input[type="email"],
textarea {
  width: 100%; /* Ocupa el 100% del ancho disponible */
  padding: 10px; /* Espaciado interno */
  border: none; /* Sin borde */
  border-radius: 5px; /* Esquinas redondeadas */
  margin-bottom: 15px; /* Espacio entre los campos */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra para los campos */
}

input[type="text"]:focus,
input[type="email"]:focus,
textarea:focus {
  outline: none; /* Sin borde al enfocarse */
  box-shadow: 0 0 5px rgba(255, 255, 255, 0.7); /* Resalta el campo al enfocarse */
}




.btn-add-project {
  display: block;
  margin: 20px auto;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button {
  margin: 10px;
  padding: 10px;
  cursor: pointer;
}

.edit-modal {
  background-color: #6c5b9a; /* Fondo morado más claro */
  padding: 40px 30px; /* Mantener el padding */
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(36, 167, 158, 0.1);
  width: 100%; /* Ancho completo */
  max-width: 1000px; /* Ancho máximo del modal */
  margin: 20px auto; /* Centrado en la página */
  color: white; /* Color del texto */
}

input[type="text"],
input[type="email"],
textarea {
  width: 100%; /* Ocupa el 100% del ancho disponible */
  padding: 10px; /* Espaciado interno */
  border: none; /* Sin borde */
  border-radius: 5px; /* Esquinas redondeadas */
  margin-bottom: 15px; /* Espacio entre los campos */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra para los campos */
}

input[type="text"]:focus,
input[type="email"]:focus,
textarea:focus {
  outline: none; /* Sin borde al enfocarse */
  box-shadow: 0 0 5px rgba(255, 255, 255, 0.7); /* Resalta el campo al enfocarse */
}

button {
  background-color: #5c4b8a; /* Color de fondo de los botones */
  color: white; /* Color del texto en los botones */
  border: none; /* Sin bordes */
  border-radius: 5px; /* Bordes redondeados en los botones */
  padding: 10px 15px; /* Espaciado interno del botón */
  cursor: pointer; /* Cambia el cursor al pasar sobre el botón */
}

button:hover {
  background-color: #8473d2; /* Color de fondo en hover */
}

.edit-modal {
  background-color: #6c5b9a; /* Fondo del modal */
  padding: 40px 30px; /* Mantener el padding */
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(36, 167, 158, 0.1);
  width: 100%; /* Ancho completo */
  max-width: 900px; /* Ancho máximo del modal */
  margin: 15px auto; /* Centrado en la página */
  color: white; /* Color del texto */
}

.edit-modal h2 {
  margin-bottom: 15px;
}

.edit-modal form {
  display: flex;
  flex-direction: column;
}

.edit-modal label {
  margin-bottom: 5px;
  color: white; /* Color del texto de las etiquetas */
}

.edit-modal input,
.edit-modal textarea {
  margin-bottom: 50px;
  padding: 12px; /* Aumentado para más comodidad */
  border: 1px solid #ddd; /* Mantener el borde ligero */
  border-radius: 5px; /* Esquinas redondeadas */
  background-color: #b39cd0; /* Fondo morado más claro para inputs */
  color: white; /* Cambiar el color del texto dentro de los campos a negro para mayor contraste */
  width: 100%; /* Ocupa el 100% del ancho disponible */
}

.edit-modal textarea {
  height: 150px; /* Altura del textarea */
}

.edit-modal input:focus,
.edit-modal textarea:focus {
  outline: none; /* Sin borde al enfocarse */
  box-shadow: 0 0 5px rgba(255, 255, 255, 0.7); /* Resalta el campo al enfocarse */
}

.edit-modal-button {
  background-color: #6c5b9a; /* Color coral */
  color: white;
  margin-top: 10px;
  width: 100%;
  padding: 10px 15px;
  border: none;
  border-radius: 25px; /* Bordes redondeados */
  font-size: 16px;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Sombra sutil */
  transition: background-color 0.3s, transform 0.2s; /* Transiciones suaves */
}

.edit-modal-button:hover {
  background-color: #b39cd0; /* Color más oscuro al hacer hover */
  transform: scale(1.05); /* Aumentar ligeramente el tamaño al hacer hover */
}

.edit-modal-button:focus {
  outline: none; /* Sin borde al hacer foco */
}



</style>
