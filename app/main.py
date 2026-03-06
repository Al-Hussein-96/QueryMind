from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import create_agent

app = FastAPI()
agent = create_agent()

class QuestionRequest(BaseModel):
    question: str



@app.post("/ask")
async def ask(request: QuestionRequest):
    result = agent.invoke({"input": request.question})
    return {
        "answer": result["output"],
    }
    