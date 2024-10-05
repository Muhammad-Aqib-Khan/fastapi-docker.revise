from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "Welcome to my API" } # Change to a string



@app.get("/piaic")
def piaic()->dict:
    return {"organization ":  "Welcome to the PIAIC API"}







