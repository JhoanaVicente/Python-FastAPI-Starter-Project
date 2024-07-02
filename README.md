# Python-FastAPI-Starter-Project  
## Configuración del Entorno

### Creación y Activación del Entorno Virtual (Opcional)

Para mantener las dependencias del proyecto separadas del entorno global de Python, se recomienda utilizar un entorno virtual. Para crear y activar el entorno virtual, ejecuta los siguientes comandos desde la terminal:

```bash
python -m venv env       # Crea el entorno virtual 
```  
Windows: Activar el entorno virtual:

````bash
.\env\Scripts\activate  
````
macOS/Linux: Activar el entorno virtual:

````bash
source env/bin/activate  
````
## Instalación de Dependencias
Después de configurar el entorno virtual (si se utiliza), asegúrate de crear o actualizar requirements.txt 
con las dependencias necesarias para el proyecto. Puedes agregar las dependencias directamente al archivo
requirements.txt. Ejemplo:  
````bash  
fastapi==0.68.2
uvicorn==0.15.0  
````  
Luego instalas las dependencias ejecutando:  
````bash  
pip install -r requirements.tx  
````  
#### Desarrollo y Pruebas
A partir de la estructura básica del proyecto, puedes comenzar a desarrollar tu aplicación FastAPI. Aquí algunos pasos iniciales:

1. Archivo Principal (main.py): Define la configuración y ejecución de tu aplicación FastAPI en este archivo.

2. Definición de Modelos: Crea modelos de datos en el directorio app/models/ según sea necesario para tu aplicación.

3. Creación de Enrutadores: Define enrutadores en el directorio app/routers/ para manejar las diferentes rutas y endpoints de tu API.

4. Pruebas: Realiza pruebas unitarias y de integración para asegurar el funcionamiento correcto de tu aplicación.  

## Ejecución de la Aplicación
Para ejecutar tu aplicación FastAPI localmente, usa el siguiente comando desde la terminal:  
````bash  
python -m uvicorn main:app --reload
````  
Esto iniciará el servidor Uvicorn y tu aplicación estará disponible en http://127.0.0.1:8000.

Observación de cambios: Uvicorn está configurado para observar cambios en los archivos y automáticamente reiniciar el
servidor cuando detecta modificaciones. 


