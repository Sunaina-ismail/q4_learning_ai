from fastapi import FastAPI, Depends, Query, HTTPException, status
from typing import Annotated

app: FastAPI = FastAPI()

# 1. Simple Dependency Example
def provide_welcome_message():
    return {"message": "Welcome to our amazing platform!"}

@app.get("/welcome")
def show_welcome(msg: Annotated[dict, Depends(provide_welcome_message)]):
    return msg


# 2. Dependency with Parameters Example
def get_user_goal(username: str):
    return {"goal": f"{username}'s goal is to master new technologies."}

@app.get("/goal")
def get_user_goal_info(goal_info: Annotated[dict, Depends(get_user_goal)]):
    return goal_info


# 3. Dependency with Query Parameters Example
def validate_login(username: str = Query(...), password: str = Query(...)):
    if username == "admin" and password == "secret":
        return {"status": "Login successful!"}
    else:
        return {"status": "Login failed, please try again."}

@app.get("/login")
def login_response(user_status: Annotated[dict, Depends(validate_login)]):
    return user_status


# 4. Multiple Dependencies Example
def increment_number(num: int):
    return num + 1

def double_number(num: int):
    return num * 2

@app.get("/calculate/{num}")
def perform_calculation(num: int, incremented: Annotated[int, Depends(increment_number)], doubled: Annotated[int, Depends(double_number)]):
    result = num + incremented + doubled
    return {"calculation_result": result}


# 5. Class-Based Dependency Example
products = {
    "101": "Smartphone",
    "102": "Laptop",
    "103": "Headphones"
}

class FetchProduct:
    def __init__(self, product_catalog):
        self.product_catalog = product_catalog

    def __call__(self, product_id: str):
        product = self.product_catalog.get(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product ID {product_id} not found")
        return product

product_dependency = FetchProduct(products)

@app.get("/product/{id}")
def fetch_product_details(product_name: Annotated[str, Depends(product_dependency)]):
    return {"product": product_name}


# 6. Class-Based Dependency for User Data
users_db = {
    "101": "John Doe",
    "102": "Jane Smith"
}

class FetchUser:
    def __init__(self, user_db):
        self.user_db = user_db

    def __call__(self, user_id: str):
        user = self.user_db.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")
        return user

user_dependency = FetchUser(users_db)

@app.get("/user/{id}")
def get_user_details(user_name: Annotated[str, Depends(user_dependency)]):
    return {"user": user_name}
