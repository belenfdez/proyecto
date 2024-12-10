// src/config/api.js
import axios from 'axios';

export const api = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_URL, // Usamos la variable de entorno para la URL base
  timeout: 5000,  // Tiempo máximo para la petición
});
