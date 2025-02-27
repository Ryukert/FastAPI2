from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, db

app = FastAPI()


cred = credentials.Certificate("triodeaceleradores-firebase-adminsdk-fbsvc-6448d15405.json")  
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://triodeaceleradores-default-rtdb.firebaseio.com/"
})


class Aceleracion(BaseModel):
    x: float
    y: float
    z: float

class SensorData(BaseModel):
    sensor_id: str
    aceleracion: Aceleracion

class Sensores(BaseModel):
    sensores: List[SensorData]

@app.post("/items")
def add_items(sensores: Sensores):
    ref = db.reference("/acelerometros/item")
    results = []

    for sensor in sensores.sensores:
        new_ref = ref.push({
            "SENSOR_ID": sensor.sensor_id,
            "ACELERACION": {
                "X": sensor.aceleracion.x,
                "Y": sensor.aceleracion.y,
                "Z": sensor.aceleracion.z
            }
        })
        results.append({"sensor_id": sensor.sensor_id, "key": new_ref.key})

    return {"results": results}
