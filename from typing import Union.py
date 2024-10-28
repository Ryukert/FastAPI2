from typing import Union
from fastapi import FastAPI # Framework FastAPI
from firebase import firebase # Conexion a Firebase
from pydantic import BaseModel

app = FastAPI()

# Configuracion de firebase
firebaseConfig = {
    "apiKey": "AIzaSyD7-kCrPX9cQsHQQT_Zs8YPXZANDxy8mpM",
    "authDomain": "esp32-431c8.firebaseapp.com",
    "databaseURL": "https://esp32-431c8-default-rtdb.firebaseio.com",
    "projectId": "esp32-431c8",
    "storageBucket": "esp32-431c8.appspot.com",
    "messagingSenderId": "470035568895",
    "appId": "1:470035568895:web:afa800f0cb55148244d4ca",
    "measurementId": "G-8Z822YLLM7"
}

# Conexion a la bd
firebase = firebase.FirebaseApplication(firebaseConfig["databaseURL"], None)

# Clase para definir el tipo de los valores
class Esp32(BaseModel):
    type: str
    project_id: str
    private_key_id: str
    private_key: str
    client_email: str
    client_id: str
    auth_uri: str
    token_uri: str
    auth_provider_x509_cert_url: str
    client_x509_cert_url: str
    universe_domain: str

# Obtener todos los datos
@app.get("/")
def read_root():
    return firebase.get("/esp32/item", "")

# Obtener un dato en especifico
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items")
def add_item(item: Esp32):
    result = firebase.post("/esp32/item", {
        "type": item.type,
        "project_id": item.project_id,
        "private_key_id": item.private_key_id,
        "private_key": item.private_key,
        "client_email": item.client_email,
        "client_id": item.client_id,
        "auth_uri": item.auth_uri,
        "token_uri": item.token_uri,
        "auth_provider_x509_cert_url": item.auth_provider_x509_cert_url,
        "client_x509_cert_url": item.client_x509_cert_url,
        "universe_domain": item.universe_domain
    })
    return result