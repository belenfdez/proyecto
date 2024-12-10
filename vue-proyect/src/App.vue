<template>
  <div id="app" class="app-background">
    <!-- Navegación superior -->
    <nav>
      <a href="#SN">SOBRE NOSOTRAS</a>
      <a href="#P">PROYECTOS</a>
    </nav>

    <!-- Encabezado con información personal -->
    <header>
      <h1 style="text-align:center; font-size: 65px;font-family: 'Lexend';margin-left: -500px;">PORTFOLIO DE PROYECTOS</h1>
      <img :src="programadores" alt="programadores" style="width:400px;height:350px;float:right;margin-top:-20px;margin-right:40px;">
    </header>

    <!-- Sección "Nosotras" -->
    <section id="SN">
      <h2><br><br>Sobre Nosotras</h2>
      <p>Somos Belén y Laura, estudiantes de tercer año en Ciencia e Ingeniería de Datos en la Universidad Autónoma de Madrid.<br><br>
         Como pareja de trabajo en todos nuestros proyectos universitarios, hemos combinado nuestras habilidades en programación
         (principalmente en Python y Java), gestión de bases de datos, análisis de datos y machine learning. A lo largo de nuestros estudios,
         hemos abordado una variedad de desafíos que incluyen la implementación de modelos de aprendizaje automático, la visualización de datos y 
         la optimización de procesos.
      </p>
      <div style="text-align: center">
        <img :src="dataSciences" alt="dataSciences" style="max-width: 25%;max-height: 25%;width: auto;height: auto;margin-top:40px;margin-right:120px;">
      </div>
      <nav>
        <a href="#top">INICIO</a>
      </nav>
    </section>
    
    <!-- Sección "Proyectos" -->
    <section id="P">
      <h2>Proyectos</h2>
      <p>En este portfolio, presentamos una selección de proyectos que reflejan nuestra capacidad para trabajar en equipo, nuestra creatividad en la 
         resolución de problemas y nuestro compromiso con la excelencia en el campo de la ciencia de datos y la programación.
      </p>

      <div class="search-container">
        <input
          v-model="searchQuery"
          class="search-input"
          placeholder="Buscar proyecto por título"
        />
        <button class="search-button" @click="searchProject">Buscar</button>
        <button class="cancel-button" @click="fetchProjects">Cancelar Búsqueda</button>
      </div>

      <!-- Componente para mostrar los proyectos existentes -->
      <ProyectosContainer 
        :projects="projects" 
        @add-project="addProject" 
        @delete-project="deleteProject"
        @search-project="searchProject"
        @edit-project="editProject"
      />
      
      <nav>
        <a href="#top">INICIO</a>
      </nav>

    </section>
  </div>
</template>


<script>
import programadores from '@/assets/programadores.png';
import dataSciences from '@/assets/dataSciences.png';
import ProyectosContainer from '@/components/ProyectosContainer.vue';
import img4 from '@/assets/aa_recorte.png';
import img5 from '@/assets/carpeta.png';
import img6 from '@/assets/threads.jpg';
import axios from 'axios';

const backendUrl = 'https://backend-wdn4.onrender.com';
  
export default {
  name: "App",
  components: { ProyectosContainer },
  data() {
    return {
      searchQuery: '',
      showModal: false,
      programadores,
      dataSciences,
      projects: [
        {
          id: '1',
          titulo: 'Aprendizaje Automático. Reducción de Dimensionalidad',
          imagen: img4,
          descripcion: 'En esta práctica de reducción de dimensionalidad, se aplicó inicialmente PCA (Análisis de Componentes Principales) al dataset de fuga de clientes de una empresa telefónica, utilizado previamente en la práctica 3. PCA tiene como objetivo reducir las dimensiones del conjunto de datos al proyectarlo en un espacio de menor dimensión, maximizando la varianza. Se comenzó estandarizando las variables para evitar que aquellas con mayores rangos influyeran de manera desproporcionada en los resultados.',
          conclusion: 'La reducción de dimensionalidad es una técnica fundamental en el análisis de datos, especialmente cuando se trabaja con conjuntos de datos de alta dimensionalidad. El uso de PCA y LDA no solo permite simplificar la visualización de datos, sino que también puede mejorar el rendimiento de los modelos de aprendizaje automático. Estos resultados destacan la importancia de la preparación y el preprocesamiento de datos en el análisis de datos, ya que influye en gran medida en la efectividad de los algoritmos utilizados.',
        },
        {
          id: '2',
          titulo: 'Base de Datos. Gestión y Consultas de Películas con pgAdmin',
          imagen: img5,
          descripcion:
            'En este proyecto de bases de datos, se utilizó la herramienta pgAdmin para gestionar un conjunto de datos sobre películas. El proceso comenzó con la creación de un esquema relacional que incluía información clave como los detalles de las películas, el reparto, los géneros, los países de producción, las compañías productoras, y las valoraciones de los usuarios.',
          
          conclusion: 'Gracias a pgAdmin, fue posible manejar sin problemas una base de datos compleja con varias tablas y relaciones. Las consultas SQL realizadas ayudaron a obtener información útil sobre el catálogo de películas, el reparto y las valoraciones de los usuarios, haciendo más fácil el análisis y la obtención de datos importantes para el mundo del cine.',
          },
          {
            id: '3',
            titulo: 'Solución del Problema SAT usando Threads en Java',
            imagen: img6,
            descripcion:
              'En este proyecto, se implementó una solución al problema de satisfacibilidad booleana (SAT) utilizando Java y la programación con threads. El objetivo fue mejorar la eficiencia en la resolución de instancias grandes del problema mediante la paralelización del proceso. Para estructurar la solución, se desarrollaron varias clases en Java, como Clause, CNF, y SAT, encargadas de representar los diferentes elementos del problema.',
            conclusion: 'El uso de threads en Java para resolver el problema SAT, combinado con la implementación de clases como Clause, CNF, y SAT, permitió una mejora notable en la eficiencia del programa. Al distribuir el trabajo entre múltiples hilos y estructurar el problema de forma clara con las clases Java, se logró reducir el tiempo de ejecución en instancias grandes del problema SAT.',
          },
        ]
    };
  },
  watch: {
    projects: {
      handler(newProjects) {
        this.projects = newProjects; 
      },
      immediate: true,
    },
  },
  methods: {
    async fetchProjects() {
      try {
        const response = await axios.get(`${backendUrl}/getProjects`);
        if (!response.data.resultado || response.data.resultado.length === 0) {
          await this.initializeProjects();
        }
        this.projects = response.data.resultado;
      } catch (error) {
        console.error('Error al obtener los proyectos:', error);
      }
    },
    async addProject(project) {
      try {
         const response = await axios.post(`${backendUrl}/add`, project);
         console.log('Respuesta del servidor:', response.data);  // Agregar esta línea para ver la respuesta completa
        await this.fetchProjects();
      } catch (error) {
         console.error('Error al guardar el proyecto en el servidor:', error);
      }
    },
    async deleteProject(projectId) {
      try {
        await axios.delete(`${backendUrl}/delete`, { data: { id: projectId } });
        this.projects = this.projects.filter(project => project.id !== projectId);
      } catch (error) {
        console.error('Error al eliminar el proyecto:', error);
      }
    },
    async searchProject() {
      if (this.searchQuery.trim() === '') return;

      try {
        const response = await axios.get(`${backendUrl}/get`, { params: { titulo: this.searchQuery } });
        this.projects = response.data.resultado || null;
      } catch (error) {
        console.error('Error al buscar el proyecto:', error);
      }
    },
    async initializeProjects() {
      for (const project of this.projects) {
        await this.addProject(project);
      }
    },
    async editProject(updatedProject) {
      try {
        await axios.put(`${backendUrl}/edit`, updatedProject);
        const index = this.projects.findIndex(project => project.id === updatedProject.id);
        if (index !== -1) {
          this.projects.splice(index, 1, updatedProject);
        }
      } catch (error) {
        console.error('Error al editar el proyecto:', error);
      }
    }
  },
  created() {
    this.fetchProjects(); 
    
  }
}
</script>


    
<style>
/* Estilos generales */
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 30px;
}

html, body {
  height: 100%; /* Asegura que el body ocupe toda la altura de la ventana */
  margin: 0; /* Elimina el margen por defecto */
  padding: 0; /* Elimina el padding por defecto */
}
.app-background {
  background: linear-gradient(135deg, #f8cdda 0%, #1fc8db 100%);
  min-height: 100vh;
  padding: 20px;
}



header h1 {
  height:100%;
  margin: 0;
  text-align: center;
  font-size: 65px; /* Puedes ajustar este tamaño según prefieras */
  font-family: 'Lexend', sans-serif; /* Asegúrate de que esta fuente esté disponible */
  color: white; /* Color blanco para el contraste */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7); /* Sombra de texto para mejorar la legibilidad */
  margin: 20px 0; /* Espaciado alrededor del título */
}

header h2,
section h2 {
  text-align: left;
  font-size: 35px; /* Puedes ajustar este tamaño según prefieras */
  font-family: 'Lexend', sans-serif; /* Asegúrate de que esta fuente esté disponible */
  color: white; /* Color blanco para el contraste */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7); /* Sombra de texto para mejorar la legibilidad */
  margin: 50px 30px; /* Espaciado alrededor del título */
}

section p {
  color: #333; /* Color negro suave */
  font-size: 18px; /* Tamaño de fuente */
  font-family: 'Lexend', sans-serif; /* Tipo de letra */
  line-height: 1.6; 
  text-align: justify; 
  text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.5); /* Sombra suave del texto */
  margin: 15px 30px; /* Espaciado */
}


/* Navegación */
nav {
  margin: 10px 0;
  display: flex; /* Usar flexbox para alinear los enlaces */
  justify-content: flex-end; /* Alinear a la derecha */
}

nav a {
  margin: 0 15px;
  text-decoration: none;
  color: #ffffff; /* Cambiado a blanco */
  font-weight: bold;
  font-size: 20px;
}

nav a:hover {
  color: #f0f0f0; /* Un blanco más suave al pasar el cursor */
}

.btn-add-project {
  text-align: center;
  margin-bottom: 20px;
  padding: 20px 40px; /* Tamaño del botón */
  background: rgba(34, 139, 34, 0.9); /* Un verde más oscuro y semi-transparente */
  color: #fff; /* Color del texto blanco */
  border: none;
  border-radius: 8px; /* Esquinas más redondeadas */
  cursor: pointer;
  font-size: 22px; /* Tamaño del texto */
  transition: background 0.3s, transform 0.3s; /* Efecto de transición */
}

/* Efecto al pasar el ratón */
.btn-add-project:hover {
  background: rgba(34, 139, 34, 1); /* Cambia a fondo opaco al pasar el ratón */
  transform: scale(1.05); /* Aumenta un poco el tamaño */
}


/* Estilo de imagenes */
header img {
  margin-right: 100px;
}

.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.search-input {
  padding: 10px;
  border: 1px solid #bdbdbd;
  border-radius: 5px;
  flex: 1;
  margin-right: 10px;
  font-size: 16px;
}

.search-button,
.cancel-button {
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.search-button {
  background-color: #4caf50; /* Verde */
  color: white;
}

.cancel-button {
  background-color: #e3635a; /* Rojo */
  color: white;
  margin-left: 10px;
}

.search-button:hover,
.cancel-button:hover {
  transform: scale(1.05);
}

.search-button:focus,
.cancel-button:focus {
  outline: none;
}

.modal h2 {
  margin-bottom: 15px;
}

.modal form {
  display: flex;
  flex-direction: column;
}

.modal label {
  margin-bottom: 5px;
}

.modal input,
.modal textarea {
  margin-bottom: 50px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.modal button {
  margin-top: 10px;
  padding: 10px 15px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.modal button:hover {
  background-color: #2a9d78;
}

</style>
    
