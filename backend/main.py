from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/bot_query")
def bot_query(input_text: str):
    return {"output_text": input_text.lower()}
