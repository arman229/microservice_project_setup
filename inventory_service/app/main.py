from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"App": " new inventory_service"}
