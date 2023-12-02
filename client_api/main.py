import os

from fastapi import FastAPI
from ultralytics import YOLO

app = FastAPI()
triton_service = os.getenv("TRITON_SERVICE", "localhost:8000")


@app.get("/")
def read_root():
    print(f"Connecting to triton server host at: {triton_service}")

    # Load the Triton Server model
    model = YOLO(f"http://{triton_service}/yolo", task="detect")

    # Run inference on the server
    results = model("bus.jpg")
    print(results)
    return results[0].speed
