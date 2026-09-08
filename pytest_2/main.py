from fastapi import FastAPI, HTTPException, status
from database import (
    get_all_tasks, get_task_by_id, add_task,
    update_task, delete_task
)

from models import TaskCreate, TaskUpdate

app = FastAPI(title="To-Do API")

@app.get("/tasks")
def list_tasks():
    return get_all_tasks()

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    # баг: нет валидации длины заголовка (может быть пустая строка)
    new_task = add_task(task.dict())
    return new_task

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)
    if task is None:
        # баг: ошибка 404 не выбрасывается, возвращается None -> FastAPI упадёт с 500
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}")
def update_task_endpoint(task_id: int, updated: TaskUpdate):
    task = update_task(task_id, updated.dict(exclude_unset=True))
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int):
    success = delete_task(task_id)
    if not success:
        # баг: при удалении несуществующей задачи возвращается 204 вместо 404
        # (так как delete_task возвращает False, но мы не обрабатываем это)
        pass
    return {"status": "deleted"}  # всегда возвращает 200, даже если задача не найдена