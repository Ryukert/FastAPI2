from typing import List
from fastapi import FastAPI
from firebase import firebase
from pydantic import BaseModel

app = FastAPI()

# Configuracion de firebase
firebaseConfig = {
"apiKey": "AIzaSyAY41_3qeC0KAiHArv0q_nLA0YBmqd0anw",
  "authDomain": "triodeaceleradores.firebaseapp.com",
  "databaseURL": "https://triodeaceleradores-default-rtdb.firebaseio.com",
  "projectId": "triodeaceleradores",
  "storageBucket": "triodeaceleradores.firebasestorage.app",
  "messagingSenderId": "349508741823",
  "appId": "1:349508741823:web:eb4ca372b087a66f76740a",
  "measurementId": "G-6BYN9N70WC"
}

# Conexion a la bd
firebase = firebase.FirebaseApplication(firebaseConfig["databaseURL"], None)

# Clase para definir los datos de aceleración
class Aceleracion(BaseModel):
    x: float
    y: float
    z: float

# Clase para definir los datos de cada sensor
class SensorData(BaseModel):
    sensor_id: str
    aceleracion: Aceleracion

# Clase para definir los datos de múltiples sensores
class Sensores(BaseModel):
    sensores: List[SensorData]

# Añadir datos de múltiples sensores
@app.post("/items")
def add_items(sensores: Sensores):
    results = []
    for sensor in sensores.sensores:
        result = firebase.post("/acelerometros/item", {
            "SENSOR_ID": sensor.sensor_id,
            "ACELERACION": {
                "X": sensor.aceleracion.x,
                "Y": sensor.aceleracion.y,
                "Z": sensor.aceleracion.z
            }
        })
        results.append(result)
    return {"results": results}
