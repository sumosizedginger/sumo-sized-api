from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone

app = FastAPI()

# Strictly allow only your GitHub Pages origin
origins = [
    "https://sumosizedginger.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the strictly typed telemetry payload
class TelemetryData(BaseModel):
    device_type: str
    file_size_mb: float
    render_time_seconds: float
    is_success: bool
    error_message: Optional[str] = None

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.post("/telemetry")
def receive_telemetry(data: TelemetryData):
    # Print telemetry data to the server console
    print(f"Telemetry received: {data.model_dump()}")
    return {"message": "Telemetry received successfully"}
