from fastapi import FastAPI
from task_manager import TaskManager
from fastapi import HTTPException



app = FastAPI()

manager = TaskManager()
manager.load_from_file("tasks.json")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    deleted = manager.delete_task(task_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Задача не найдена")

    manager.save_to_file("tasks.json")
    return {"message": "Задача удалена"}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = manager.find_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")

    return {
        "id": task.id,
        "title": task.title,
        "priority": task.priority,
        "done": task.done
    }

from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    priority: int

@app.post("/tasks")
def create_task(task: TaskCreate):
    manager.add_task(task.title, task.priority)
    manager.save_to_file("tasks.json")
    return {"message": "Задача добавлена"}

@app.patch("/tasks/{task_id}")
def mark_done(task_id: int):
    task = manager.find_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")

    task.done = True
    manager.save_to_file("tasks.json")

    return {"message": "Задача обновлена"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    manager.delete_task(task_id)
    manager.save_to_file("tasks.json")
    return {"message": "Задача удалена"}

