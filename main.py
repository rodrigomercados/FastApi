from fastapi import FastAPI

from app.v1.router.user_router import router as user_router
#from app.v1.router.usuario_router import router as usuario_router

app=FastAPI()

app.include_router(user_router)





# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# import psycopg2


# app= FastAPI()
# app.title ="API Truck"
# app.version = "0.0.1"

# # Conectarse a la base de datos
# conn = psycopg2.connect(
#     dbname="transporte",
#     user="postgres",
#     password="postgres",
#     host="localhost",  # O la dirección IP del servidor donde se aloja la base de datos
#     port="5432"  # El puerto por defecto de PostgreSQL es 5432
# )

# camiones = [
#     {
#         "id_camion": 1,
#         "patente_camion":"AABBCC"
#     },
#     {
#         "id_camion": 2,
#         "patente_camion":"DDEEFF"
#     }
# ]

# @app.get('/', tags=['Principal'])
# def home():
#     return "Hola Mundo con cambios!"

# @app.get('/camiones', tags=['Principal'])
# def get_camiones():
#     #return {"idCamion": "1"}
#     #return HTMLResponse('<h1>Saludo<h1>')
#     return camiones

# # Uso de parámetro de ruta
# @app.get('/camiones/{id}', tags=['Principal'])
# def get_camion(id: int):
#     #return {"idCamion": "1"}
#     #return HTMLResponse('<h1>Saludo<h1>')
#     #return id#camiones
#     for camion in camiones:
#         if camion['id_camion'] == id:
#             return camion
#     return []

# @app.get('/camionesdb/{id}', tags=['Principal'])
# def get_camion_db(id: int):
#     cur = conn.cursor()
#     cur.execute("Select cod_camion,patente from camion where cod_camion=%s"%(id))
#     rows = cur.fetchall()
#     for row in rows:
#         return row





# #uso de parametros query
# @app.get('/camiones/', tags=['Principal'])
# def get_camion_by_categoria(id: int,patente:str):
#     if id:
#         for camion in camiones:
#             if camion['id_camion'] == id:
#                 return camion
#         return[]
#     if patente:
#         for camion in camiones:
#             if camion['patente_camion'] == patente:
#                 return camion

