from database import Base
from datetime import datetime, timedelta
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base


class Taxis(Base):
    __tablename__ = "taxis"

    matricula = Column(String, primary_key=True, index=True)
    conductor = Column(String, index=True)
    colonia = Column(String, index=True)
    numero_taxi = Column(String, index=True)
    ubicacion_actual = Column(String, index=True)
    disponibilidad = Column(String, index=True)
    telefono = Column(String, index=True)
    genero = Column(String, index=True)
