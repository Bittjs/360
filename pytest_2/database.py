# Имитация базы данных – просто список словарей
tasks_db = []
task_id_counter = 1


def get_all_tasks():
    return tasks_db


def get_task_by_id(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    return None  # баг: не возвращает ошибку, а просто None


def add_task(task_data: dict):
    global task_id_counter
    new_task = {
        "id": task_id_counter,
        "title": task_data["title"],
        "description": task_data.get("description", ""),
        "completed": False,
        "created_at": "2026-09-07"  # баг: дата всегда сегодняшняя,
        # не из запроса
    }
    tasks_db.append(new_task)
    task_id_counter += 1
    return new_task


def update_task(task_id: int, updated_data: dict):
    task = get_task_by_id(task_id)
    if task is None:
        return None
    # баг: не обновляет поле completed, если оно передано
    if "title" in updated_data:
        task["title"] = updated_data["title"]
    if "description" in updated_data:
        task["description"] = updated_data["description"]
    # забыли обработать "completed"
    return task


def delete_task(task_id: int):
    global tasks_db
    task = get_task_by_id(task_id)
    if task is None:
        return False
    tasks_db = [t for t in tasks_db if t["id"] != task_id]
    return True


def reset_db():
    """Сбрасывает состояние базы данных (для тестов)"""
    global tasks_db, task_id_counter
    tasks_db = []
    task_id_counter = 1