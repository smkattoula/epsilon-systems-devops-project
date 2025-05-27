from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from datetime import datetime
from pydantic import BaseModel

class MaintenanceUpdate(BaseModel):
    message: str

app = FastAPI(title="Epsilon ShipOps Readiness API")

# Sample in-memory log
logs = [
    {"timestamp": "2025-05-20T08:00:00Z", "message": "Routine check complete."},
    {"timestamp": "2025-05-22T13:30:00Z", "message": "Repair scheduled."}
]

@app.get("/readiness-status")
async def readiness_status():
    return {"status": "GREEN", "message": "All systems operational."}

@app.post("/maintenance-update")
async def maintenance_update(update: MaintenanceUpdate):
    timestamp = datetime.utcnow().isoformat() + "Z"
    logs.append({"timestamp": timestamp, "message": update.message})
    return {"status": "OK", "logged": logs[-1]}

@app.get("/ship-log")
async def ship_log():
    return {"logs": logs}
