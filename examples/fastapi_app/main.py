from fastapi import FastAPI, File
from pydantic import BaseModel

app = FastAPI(title="Loom Data Ingestion - Example")

class SystemMetrics(BaseModel):
    timestamp: str
    source_id: str
    metric_name: str
    value: float

@app.post('/data/network-flow', status_code=202)
async def ingest_network_flow(file: bytes = File(...)):
    # Placeholder: enqueue/process packet bytes
    return {"status": "accepted", "size": len(file)}

@app.post('/data/system-metrics', status_code=202)
async def ingest_system_metrics(metrics: SystemMetrics):
    # Placeholder: validate/store metrics
    return {"status": "accepted", "metric": metrics.metric_name}
