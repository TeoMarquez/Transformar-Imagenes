# Proyecto de Conversión de Imágenes

Este proyecto consiste en un script de Python que permite seleccionar una carpeta de entrada y una carpeta de salida para convertir imágenes PNG y JPEG.

## 🚀 Funcionalidad

El script realiza las siguientes acciones:

1. **Selección de Carpetas:**
   - Utiliza la biblioteca Tkinter para abrir cuadros de diálogo que permiten al usuario seleccionar las carpetas de entrada y salida.

2. **Procesamiento de Imágenes PNG:**
   - Lista todas las imágenes PNG en la carpeta de entrada.
   - Para cada imagen, recorta la imagen al contenido visible utilizando la caja delimitadora y guarda la imagen recortada en la carpeta de salida.

3. **Conversión de Imágenes JPEG a PNG:**
   - Convierte todas las imágenes JPEG encontradas en la carpeta de entrada a imágenes PNG y las guarda en la carpeta de salida.

## 🛠️ Tecnologías Utilizadas

- **Python:** Lenguaje de programación principal.
- **PIL (Python Imaging Library) / Pillow:** Utilizado para el manejo de imágenes y conversiones.
- **Tkinter:** Utilizado para la interfaz gráfica básica de selección de carpetas.

## 📋 Ejecución

1. **Clonar el Repositorio:**
   ```
   git clone https://github.com/tu-usuario/Proyecto-Conversión-Imágenes.git
   ```
2. **Instalar Dependencias:**
   - Asegúrate de tener instalada la biblioteca PIL / Pillow. Puedes instalarla usando pip:
     ```
     pip install Pillow
     ```

3. **Ejecutar el Script:**
   - Ejecuta el script `convertir_imagenes.py` desde tu entorno de desarrollo o terminal:
     
4. **Sigue las Instrucciones:**
   - El script abrirá dos cuadros de diálogo para seleccionar la carpeta de entrada y salida.
   - Después de seleccionar las carpetas, procesará las imágenes según la descripción mencionada.
