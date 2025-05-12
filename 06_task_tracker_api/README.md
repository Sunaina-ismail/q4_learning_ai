# 📝 Task Tracker API
# Author: Sunaina Ismail

This is a simple Task Tracker API built with **FastAPI**, designed to help users manage their daily tasks. It allows user registration and task handling — such as creating, updating, and tracking — with built-in validation. All data is temporarily stored in memory using Python dictionaries, making it perfect for learning and small practice projects.

---

## 🔧 Tech Stack

- **FastAPI** – Lightning-fast web framework for building APIs
- **Pydantic** – Powerful tool for data validation and type checking
- **uv** – Modern Python package manager for quick project setup

---

## 🚀 Features

- Register new users with email and username
- Create, view, and update task details
- Update task status to `pending`, `in-progress`, or `completed`
- Retrieve tasks assigned to a specific user
- All input is validated using Pydantic
- Built-in interactive documentation at `/docs` (Swagger UI)

---

## ✅ Validations

- **Username** must be between 3 and 20 characters  
- **Due date** must be today or a future date  
- **Status** must be either `pending`, `in-progress`, or `completed`  
- **Email** should be in a valid format  

---

## 🔌 API Endpoints Overview

- `/users/` → Register a new user  
- `/users/{user_id}` → Get user info by ID  
- `/users/{user_id}/tasks` → Get all tasks for a specific user  
- `/tasks/` → Create a task  
- `/tasks/{task_id}` → Get a task by its ID  
- `/tasks/{task_id}` → Update the status of a task  

---


### Set Up the Environment

```bash
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/bin/activate  
uv add "fastapi[standard]"
```

### Start the Development Server

```bash
fastapi dev main.py
```
