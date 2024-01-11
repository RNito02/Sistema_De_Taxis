from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import date


# Todo el schema de empleado
class Modelo_Taxi_Nuevo(BaseModel):
    matricula: str
    conductor: str
    colonia: str
    numero_taxi: int
    ubicacion_actual: str
    disponibilidad: str
    telefono: int
    genero: str


class leer_taxi_matricula(BaseModel):
    matricula: str
    conductor: str
    colonia: str
    numero_taxi: int
    ubicacion_actual: str
    disponibilidad: str
    telefono: int
    genero: str


# Editar Taxi
class Taxi_Edit(BaseModel):
    conductor: str
    colonia: str
    numero_taxi: int
    ubicacion_actual: str
    disponibilidad: str
    telefono: int
    genero: str
