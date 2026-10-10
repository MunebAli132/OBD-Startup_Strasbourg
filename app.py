
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="OBD SmartCare API",
    description="JSON API for vehicle diagnostics and garage management",
    version="1.0.0"
)

# In-memory storage for the MVP
vehicles = {}


class Vehicle(BaseModel):
    vehicle_id: str
    registration_number: str
    make: str
    model: str


class Reading(BaseModel):
    vehicle_id: str
    rpm: int = Field(ge=0, le=12000)
    speed_kmh: float = Field(ge=0, le=400)
    engine_temp_c: float
    battery_voltage: float
    codes: list[str] = []


@app.get("/")
def home():
    return {
        "name": "OBD SmartCare API",
        "status": "online",
        "format": "JSON"
    }


@app.post("/api/vehicles")
def create_vehicle(vehicle: Vehicle):
    if vehicle.vehicle_id in vehicles:
        raise HTTPException(409, "Vehicle already exists")

    vehicles[vehicle.vehicle_id] = {
        **vehicle.model_dump(),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "latest_reading": None,
        "history": []
    }

    return {
        "message": "Vehicle created",
        "vehicle": vehicles[vehicle.vehicle_id]
    }


@app.get("/api/vehicles")
def list_vehicles():
    return list(vehicles.values())


@app.get("/api/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id: str):
    vehicle = vehicles.get(vehicle_id)
    if not vehicle:
        raise HTTPException(404, "Vehicle not found")
    return vehicle


@app.post("/api/readings")
def post_reading(reading: Reading):
    vehicle = vehicles.get(reading.vehicle_id)
    if not vehicle:
        raise HTTPException(404, "Register the vehicle first")

    data = reading.model_dump()
    data["recorded_at"] = datetime.now(timezone.utc).isoformat()
    data["alert"] = (
        reading.engine_temp_c >= 110
        or reading.battery_voltage < 11.8
    )

    vehicle["latest_reading"] = data
    vehicle["history"].append(data)

    return {
        "message": "Reading received",
        "reading": data
    }


@app.get("/api/vehicles/{vehicle_id}/readings")
def get_readings(vehicle_id: str):
    vehicle = vehicles.get(vehicle_id)
    if not vehicle:
        raise HTTPException(404, "Vehicle not found")
    return vehicle["history"]


@app.get("/api/vehicles/{vehicle_id}/latest")
def get_latest_reading(vehicle_id: str):
    vehicle = vehicles.get(vehicle_id)
    if not vehicle:
        raise HTTPException(404, "Vehicle not found")
    if vehicle["latest_reading"] is None:
        raise HTTPException(404, "No readings available")
    return vehicle["latest_reading"]