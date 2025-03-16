import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient
from routes.api import router as api_router

# Creating app from Fast API
app = FastAPI()

@app.get('/')
def welcome():
    return {'message': 'Welcome to my FastAPI application'}

@app.on_event("startup")
def startup_db_client():
    # Creating connection to "Inventory" database and "Grocery Data" collection
    app.client = MongoClient('localhost', 27017)
    app.db = app.client.inventory

@app.on_event("shutdown")
def shutdown_db_client():
    MongoClient.close()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload=True)