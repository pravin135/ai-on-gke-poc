from fastapi import FastAPI
from app.agent import ask_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Kubernetes AI Agent"}

@app.post("/ask")
def ask(question: str):

    answer = ask_agent(question)

    return {"response": answer}
