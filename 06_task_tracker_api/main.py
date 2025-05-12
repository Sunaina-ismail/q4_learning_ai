from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from typing import Optional, List, Annotated
from datetime import date

app = FastAPI()

# Global storage
USERS: dict[int, dict] = {}
TASKS: dict[int, dict] = {}

# Auto-increment IDs
user_id_counter = 1
task_id_counter = 1


# MODELS 


class UserCreate(BaseModel):
    email: EmailStr
    username: Annotated[str,constr(min_length=3, max_length=20)]

class UserRead(BaseModel):
    id: int
    email: EmailStr
    username: str


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: date
    status: str
    user_id: int

    @validator("due_date")
    def validate_due_date(cls, value):
        if value < date.today():
            raise ValueError("Due date must be today or in the future.")
        return value

    @validator("status")
    def validate_status(cls, value):
        allowed = ["pending", "in-progress", "completed"]
        if value not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return value


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    status: str
    user_id: int

    @validator("due_date")
    def validate_due_date(cls, value):
        if value < date.today():
            raise ValueError("Due date must be today or in the future.")
        return value

    @validator("status")
    def validate_status(cls, value):
        allowed = ["pending", "in-progress", "completed"]
        if value not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return value


class TaskUpdateStatus(BaseModel):
    status: str

    @validator("status")
    def validate_status(cls, value):
        allowed = ["pending", "in-progress", "completed"]
        if value not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return value


#  USERS

@app.get("/")
def root():
    return {"message": "Task Tracker API is running!"}

@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    global user_id_counter
    user_data = user.dict()
    user_data["id"] = user_id_counter
    USERS[user_id_counter] = user_data
    user_id_counter += 1
    return user_data

@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


#  TASKS 

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter
    if task.user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")

    task_data = task.dict()
    task_data["id"] = task_id_counter
    TASKS[task_id_counter] = task_data
    task_id_counter += 1
    return task_data

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, status_update: TaskUpdateStatus):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task["status"] = status_update.status
    return task

@app.get("/users/{user_id}/tasks", response_model=List[Task])
def list_user_tasks(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return [task for task in TASKS.values() if task["user_id"] == user_id]