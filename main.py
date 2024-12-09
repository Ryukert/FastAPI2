from typing import Union
from fastapi import FastAPI # Framework FastAPI
from firebase import firebase # Conexion a Firebase
from pydantic import BaseModel
from datetime import datetime # Para obtener la hora actual
import pytz  # Para manejar zonas horarias
app = FastAPI()

# Configuracion de firebase
firebaseConfig = {
  "apiKey": "AIzaSyCbYS7SnWTQZPQxg5iv0YkSeELfwgvMYtw",
  "authDomain": "esp32temperatura-89c50.firebaseapp.com",
  "databaseURL": "https://esp32temperatura-89c50-default-rtdb.firebaseio.com",
  "projectId": "esp32temperatura-89c50",
  "storageBucket": "esp32temperatura-89c50.appspot.com",
  "messagingSenderId": "820223023080",
  "appId": "1:820223023080:web:af83286599e04ce65c365d",
  "measurementId": "G-LM7S7BS0SQ"
}

# Conexion a la bd
firebase = firebase.FirebaseApplication(firebaseConfig["databaseURL"], None)

# Clase para definir el tipo de los valores
class Esp32(BaseModel):
    humedad: float
    temperatura:float
# Función para obtener la hora actual en la zona horaria de México
def obtener_hora_actual():
    zona_horaria = pytz.timezone("America/Mexico_City")
    hora_actual = datetime.now(zona_horaria).strftime("%Y-%m-%d %H:%M:%S")
    return hora_actual
  
# Obtener todos los datos
@app.get("/")
def read_root():
    return firebase.get("/esp32/item", "")

# Obtener un dato en especifico
@app.post("/items2")
def add_item2(item: Esp32):
    hora_actual = obtener_hora_actual()
    result = firebase.post("/esp32/item2", {
        "TEMPERATURA": item.temperatura,
        "HUMEDAD": item.humedad,
        "HORA": hora_actual
    })
    return result, 

@app.post("/items")
def add_item(item: Esp32):
    hora_actual = obtener_hora_actual()
    result = firebase.post("/esp32/item", {
        "TEMPERATURA": item.temperatura,
        "HUMEDAD": item.humedad,
        "HORA": hora_actual
    })
    return result
