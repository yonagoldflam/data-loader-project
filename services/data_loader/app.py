from fastapi import FastAPI
from dal import Dall


app = FastAPI()

dall = Dall()

@app.get("/select/{table_name}")
def read_data(table_name: str):
    return dall.select(table_name)
