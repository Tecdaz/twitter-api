# Twitter-api
API para publicar tweets construida con Fast-Api, este proyecto es parte del curso de Fast-Api en Platzi, incluye las siguientes caracteristicas:
- Creacion de usuarios
- Creacion de tweets
- Lectura de tweets por id
- Informacion del usuario
- Lista con todos los tweets
- Lista con los usuarios
- Eliminar tweets
- Eliminar usuarios
- Editar usuarios

## Instalacion
Primero crear un entorno virtual

```python3.10 -m venv venv```

Iniciar el entorno virtual

```source venv/bin/activate```

Instalamos las dependencias

```pip install -r requirements.txt```

## Ejecutar

```uvicorn main:app --reload```

Esto enciende el servidor en localhost

## Documentacion

Para acceder a la documentacion de la API, hay que primero encender el servidor con uvicorn, despues abrir el navegador con la ruta que uvicorn nos provee.
para dirigirnos a la documentacion agregamos el endpoint "/docs". Ejemplo "127.0.0.1:8000/docs"
