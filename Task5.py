from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
import json
import os
app = FastAPI()

Json_file = "tasks.json"

if os.path.exists(Json_file):
    print(f"Файл {Json_file} существует.")
else:
    print(f"Файл {Json_file} не найден.")

if not os.path.exists(Json_file) or os.path.getsize(Json_file) == 0:
    with open(Json_file, "w") as file:
        json.dump([], file)
        print(f"Файл {Json_file} был создан с пустым содержимым.")
else:
    print(f"Файл {Json_file} уже существует и не пустой.")

class Task(BaseModel): 
    id: int = Field(..., gt=0, description="id должен быть больше 0")
    title: str
    complete: bool = False

class TaskUpdate(BaseModel): 
    complete: bool = False

def load_tasks() -> List[Task]:
    try:
        with open(Json_file, "r") as file:
            return [Task(**task) for task in json.load(file)]
    except FileNotFoundError:
        return []

def save_tasks(tasks: List[dict]):
    with open(Json_file, "w") as file:
        json.dump(tasks, file, indent=4)

tasks: List[Task] = load_tasks()
print(tasks)

@app.get("/tasks", response_model = List[Task])
async def get_tasks() -> List[Task]:
    return tasks

@app.post("/add", response_model=Task)
async def add_task(task: Task) -> Task:
    for existing_task in tasks:
        if existing_task.id == task.id:
            raise HTTPException(status_code=404, detail="Задача с таким ID уже существует.")
    
    tasks.append(task.dict())
    save_tasks(tasks)
    return task

@app.delete("/delete")
async def delete_task(id: int) -> Task:
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            save_tasks(tasks)
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/update", response_model=Task)
async def update_task(id: int, model: TaskUpdate) -> Task:
    for idx, task in enumerate(tasks):
        if task.id == id:
            updated_task = Task(id=task.id, title=task.title, complete=model.complete)
            tasks[idx] = updated_task
            save_tasks([task.dict() for task in tasks])
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")  