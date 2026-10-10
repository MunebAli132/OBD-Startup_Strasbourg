
from fastapi import FastAPI, HTTPException

app = FastAPI(title="OBD SmartCare Mock API")

vehicles = [
    {
        "vehicle_id": "VEH-001",
        "registration_number": "FR-AB-123-CD",
        "make": "Peugeot",
        "model": "208",
        "device": {
            "serial_number": "ELM327-1001",
            "connection_status": "connected"
        },
        "obd_codes": [
            {
                "code": "P0420",
                "description": "Catalyst system efficiency below threshold",
                "status": "active"
            }
        ],
        "last_visit": {
            "date": "2026-09-20",
            "reason": "Engine warning light",
            "report": "Catalyst inspection recommended"
        },
        "repairs": [
            {
                "title": "Inspect catalytic converter",
                "status": "pending",
                "priority": "medium"
            }
        ],
        "summary": (
            "Inspect the exhaust system and verify the cause "
            "of the catalyst-efficiency fault."
        ),
        "source": "MOCK_DATA",
        "updated_at": "2026-10-10T08:50:00Z"
    },
    {
        "vehicle_id": "VEH-002",
        "registration_number": "FR-EF-456-GH",
        "make": "Renault",
        "model": "Clio",
        "device": {
            "serial_number": "ELM327-1002",
            "connection_status": "disconnected"
        },
        "obd_codes": [
            {
                "code": "P0171",
                "description": "System too lean bank 1",
                "status": "active"
            }
        ],
        "last_visit": {
            "date": "2026-09-15",
            "reason": "Loss of power",
            "report": "Lean mixture fault recorded"
        },
        "repairs": [
            {
                "title": "Inspect intake system",
                "status": "pending",
                "priority": "medium"
            }
        ],
        "summary": (
            "Investigate the lean mixture fault and check for "
            "intake leaks before deciding on repairs."
        ),
        "source": "MOCK_DATA",
        "updated_at": "2026-10-10T09:00:00Z"
    }
]


@app.get("/")
def home():
    return {
        "service": "OBD SmartCare Mock API",
        "status": "online"
    }


@app.get("/api/vehicles")
def list_vehicles():
    return vehicles


@app.get("/api/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id: str):
    for vehicle in vehicles:
        if vehicle["vehicle_id"] == vehicle_id:
            return vehicle

    raise HTTPException(
        status_code=404,
        detail="Vehicle not found"
    )