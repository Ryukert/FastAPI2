from typing import Union
from fastapi import FastAPI # Framework FastAPI
from firebase import firebase # Conexion a Firebase
from pydantic import BaseModel

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

# Obtener todos los datos
@app.get("/")
def read_root():
    return firebase.get("/esp32/item", "")

# Obtener un dato en especifico
#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
 #return {"item_id": item_id, "q": q}

@app.post("/items")
def add_item(item: Esp32):
    result = firebase.post("/esp32/item", {
        "TEMPERATURA": item.temperatura,
        "HUMEDAD": item.humedad
    })
    return result