from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas import Modelo_Taxi_Nuevo, leer_taxi_matricula, Taxi_Edit
from models import Taxis
from sqlalchemy.exc import IntegrityError

# Funcion para creaer un nuevo empleado


def create_taxi(db: Session, taxi_input: Modelo_Taxi_Nuevo):
    existing_taxi = db.query(Taxis).filter(
        Taxis.matricula == taxi_input.matricula).first()
    if existing_taxi:
        raise ValueError("La matricula ya esta registrada")
    created_taxi = Taxis(
        matricula=taxi_input.matricula,
        conductor=taxi_input.conductor,
        colonia=taxi_input.colonia,
        numero_taxi=taxi_input.numero_taxi,
        ubicacion_actual=taxi_input.ubicacion_actual,
        disponibilidad=taxi_input.disponibilidad,
        telefono=taxi_input.telefono,
        genero=taxi_input.genero,
    )
    try:
        db.add(created_taxi)
        db.commit()
        db.refresh(created_taxi)
        return created_taxi
    except IntegrityError as e:
        db.rollback()
        raise ValueError(
            f"Error al crear Taxi. Detalles de la excepción: {str(e)}"
        ) from e


def leer_taxi(matricula: int, db: Session):
    taxi = db.query(Taxis).filter(
        Taxis.matricula == matricula).first()

    if taxi is None:
        raise HTTPException(status_code=404, detail="Taxi no encontrado")

    taxi_data = leer_taxi_matricula(
        matricula=taxi.matricula,
        conductor=taxi.conductor,
        colonia=taxi.colonia,
        numero_taxi=taxi.numero_taxi,
        ubicacion_actual=taxi.ubicacion_actual,
        disponibilidad=taxi.disponibilidad,
        telefono=taxi.telefono,
        genero=taxi.genero,
    )

    return taxi_data


# Funcion para buscar todos las solicitudes
def get_all_taxis(db: Session):
    taxis = db.query(Taxis).all()
    return taxis


# Editar un taxi por su numero de nomina
def edit_taxi(matricula: str, taxi_data: Taxi_Edit, db: Session):
    taxi = db.query(Taxis).filter(
        Taxis.matricula == matricula).first()

    if taxi is None:
        raise HTTPException(status_code=204, detail="Taxi no encontrado")

    allowed_fields = ["conductor", "colonia", "numero_taxi", "ubicacion_actual",
                      "disponibilidad", "telefono", "genero"]

    for field in allowed_fields:
        if hasattr(taxi_data, field):
            setattr(taxi, field, getattr(taxi_data, field))

    db.commit()
    db.refresh(taxi)

    taxi_dict = taxi.__dict__
    taxi_dict.pop("_sa_instance_state", None)

    return taxi_dict


# Eliminar un taxi por su numero de nomina
async def delete_taxi_by_matricula(matricula: str, db: Session):
    db_taxi = db.query(Taxis).filter(Taxis.matricula == matricula).first()

    if db_taxi is None:
        raise HTTPException(status_code=404, detail="Taxi no encontrado")

    db.delete(db_taxi)
    db.commit()
    return {"message": "Taxi eliminado exitosamente"}
