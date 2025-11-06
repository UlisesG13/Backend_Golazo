from fastapi import FastAPI

app = FastAPI(
    title="Golazo",
    description="Backend del e-commerce Golazo",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Bienvenido a Golazo"}
