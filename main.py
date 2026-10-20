from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

luchadores = [{"id": 1,"nombre":"prueba","edad":0,"victorias":0,"estado": True}]

class Luchador(BaseModel):
    nombre: str
    edad: int
    victorias: int
    estado: bool

@app.get("/obtener_lista")
def obtener_lista():
    return luchadores

@app.post("/agregar_luchadores")
def agregar_luchadores(luchador:Luchador):
    nuevo_id = len(luchadores)+1
    nuevo_pj = {"id":nuevo_id,"nombre":luchador.nombre,"edad":luchador.edad,"victorias":luchador.victorias,"estado":luchadorw.estado}
    luchadores.append(nuevo_pj)
    return "agregado correctamente"

@app.get("/obtener_id")
def obtener_id(ids: int):
    for l in luchadores:
        if l["id"] == ids:
            return l
        else:
            return "no encontrado"

@app.put("/actualizar_luchador/{ids}")
def actualizar_luchador(ids: int,luchador:Luchador):
    for l in luchadores:
        if l["id"] == ids:
            l["nombre"] =luchador.nombre
            l["edad"]= luchador.edad
            return "datos actualizados"
        else:
            return "no encontrado"


