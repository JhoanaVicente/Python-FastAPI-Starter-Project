# Python-FastAPI-Starter-Project  
## Clonar y ejecutar el proyecto  

### Crear y activar el entorno virtual en Pycharm 
Windows:
````bash
python -m venv env #Crea el entorno virtual
.\env\Scripts\activate  #Activa el entorno virtual
````
macOS/Linux:
````bash
python -m venv env #Crea el entorno virtual
source env/bin/activate  #Activa el entorno virtual
````
### Instalar Dependencias 
````bash  
pip install -r requirements.txt  
````  
### Ejecutar la Aplicación FastAPI  
````bash  
python -m uvicorn main:app --reload  
````  
* Si cierras el proyecto y vuelves a abrir, solo activas el entorno virtual y ejecutas.  

## Documentación Automática
FastAPI genera documentación interactiva automáticamente basada en los tipos de datos declarados y las anotaciones de Python. Asegúrate de explorar y documentar adecuadamente todos tus endpoints:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc  

## Definir un Endpoint para la Ruta Raíz
Para evitar el mensaje {"detail":"Not Found"}, puedes definir un endpoint para la ruta raíz en main.py:  
````bash  
@app.get("/")
async def read_root():
    return {"message": "Welcome to my FastAPI application!"}
````  
Después de realizar estos cambios, navega a http://127.0.0.1:8000 en tu navegador para ver el mensaje de bienvenida.  

## Pruebas  
Instalación de Pytest  
Para ejecutar pruebas unitarias y de integrasción instalamos `pytest`:  
````bash  
pip install pytest  
pytest #Ejecuta las pruebas
````  
1. Definimos correctamente los endpoints de creación y lectura de ítems.
2. Ajustamos el mensaje del endpoint raíz para que coincidiera con la prueba.
3. Actualizamos las pruebas para que coincidieran con los cambios en la API.



