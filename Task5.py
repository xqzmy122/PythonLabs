from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
import json
import os
app = FastAPI()

FILE_NAME = "tasks.json"

if os.path.exists(FILE_NAME):
    print(f"Файл {FILE_NAME} существует.")
else:
    print(f"Файл {FILE_NAME} не найден.")

if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
    # Если файла нет или он пустой, создаём его с пустым JSON
    with open(FILE_NAME, "w") as file:
        json.dump([], file)
        print(f"Файл {FILE_NAME} был создан с пустым содержимым.")
else:
    print(f"Файл {FILE_NAME} уже существует и не пустой.")

class Task(BaseModel): 
    id: int = Field(..., gt=0, description="id должен быть больше 0")
    title: str
    complete: bool = False

# Загрузка задач из файла
def load_tasks() -> List[dict]:
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Сохранение задач в файл
def save_tasks(tasks: List[dict]):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

@app.get("/tasks", response_model=List[Task])
async def get_tasks() -> List[Task]:
    return [Task(**task) for task in tasks]

@app.get("/add",  response_model=Task)
async def add_task(
    id: int = Query(..., gt=0, description="Идентификатор задачи (должен быть уникальным)"),
    title: str = Query(..., min_length=1, description="Название задачи"),
    complete: bool = Query(False, description="Статус выполнения задачи")
) -> Task:
    # Проверка, существует ли задача с таким ID
    for existing_task in tasks:
        if existing_task['id'] == id:
            raise HTTPException(status_code=400, detail="Задача с таким ID уже существует.")
    
    new_task = Task(id=id, title=title, complete=complete)
    tasks.append(new_task.dict())
    save_tasks(tasks)
    return new_task

@app.get("/delete", response_model=int)
async def delete_task(id: int) -> Task:
    if id:
        for task in tasks:
            if task['id'] == id:
                tasks.remove(task)
                save_tasks(tasks)
                return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.get("/update", response_model=Task)
async def update_task(id: int, complete: bool) -> Task:
    for task in tasks:
        if task['id'] == id:
            task['complete'] = complete
            save_tasks(tasks)  
            return task  
    raise HTTPException(status_code=404, detail="Task not found")    

