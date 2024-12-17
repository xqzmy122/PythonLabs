from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List, Dict

app = FastAPI()

class Task(BaseModel): 
    id: int = Field(..., gt=0, description="id должен быть больше 0")
    title: str
    complete: bool

tasks = [
    {'id': 1, 'title': "dqdqw", 'complete': False}
]


@app.get("/tasks", response_model=List[Task])
async def get_tasks() -> List[Task]:
    return [Task(**task) for task in tasks]

@app.get("/add",  response_model=List[Task])
async def add_task(
    id: int = Query(..., description="Идентификатор задачи"),
    title: str = Query(..., min_length=1, description="Название задачи"),
    complete: bool = Query(False, description="Статус выполнения задачи")
    ) -> None:
    for existing_task in tasks:
        if existing_task['id'] == task.id:
            raise HTTPException(status_code=400, detail="Task with this ID already exists.")
    
    tasks.append(task)

