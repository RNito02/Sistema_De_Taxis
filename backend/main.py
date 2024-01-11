from sqlalchemy.orm import sessionmaker, Session
from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from database import SessionLocal, engine
from schemas import Modelo_Taxi_Nuevo, leer_taxi_matricula, Taxi_Edit
from crud import create_taxi, get_all_taxis, leer_taxi, edit_taxi, delete_taxi_by_matricula
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configura el middleware CORS
origins = [
    "http://localhost",
    "http://192.168.105.93:8080",
    "http://localhost:8080",
    "http://127.0.0.1:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Ruta cuando se añade un nuevo empleado
@app.post("/add_taxi/")
async def create_taxi_route(taxi_input: Modelo_Taxi_Nuevo, db: SessionLocal = Depends(get_db)):
    try:
        created_taxi = create_taxi(db, taxi_input)
        return {"message": "Taxi creado", "taxi": created_taxi}
    except HTTPException as e:
        return JSONResponse(content={"error": e.detail}, status_code=e.status_code)


# Buscar un empleado por su numero de nomina
@app.get("/search_taxi/{matricula}", response_model=leer_taxi_matricula)
async def read_taxi(matricula: str, db: Session = Depends(get_db)):
    taxi_data = leer_taxi(matricula, db)
    if not taxi_data:
        raise HTTPException(status_code=204, detail="Taxi no encontrado")
    return taxi_data


# Buscar todos los empleados
@app.get("/get_all_taxis")
def all_taxis(db: Session = Depends(get_db)):
    taxis = get_all_taxis(db)
    return taxis


# Editar a un empleado por su numero de nomina
@app.put("/edit_taxi/{matricula}", response_model=Taxi_Edit)
def update_taxi(matricula: str, taxi_data: Taxi_Edit, db: Session = Depends(get_db)):
    return edit_taxi(matricula, taxi_data, db)


# Eliminar un empleado por su numero de nomina
@app.delete("/delete_taxi/{matricula}")
async def delete_taxi_route(matricula: str, db: Session = Depends(get_db)):
    return await delete_taxi_by_matricula(matricula, db)
