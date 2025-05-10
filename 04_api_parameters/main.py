from fastapi import FastAPI, Path , Query, Body, Header
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello! This is the homepage of our FastAPI project."}
# Path parameter validations
@app.get("/users/{user_id}")
async def get_user(
    user_id: int = Path(
         ..., # the parameter is required
        title="User Identifier",
        description="A unique number to identify the user. Must be at least 1.",
        ge=1
    )
):
    return {
        "User ID": user_id,
        "Message": "User data fetched successfully"
    }
    
    
#  02_query_parameter_validation   
@app.get("/courses/")
async def read_courses(
    topic: str | None = Query(
        None,  # Optional query parameter
        title="Course Topic",
        description="Search courses by topic name (e.g., Python, Data Science, Web Development).",
        min_length=3,
        max_length=50
    ),
    skip: int = Query(0, ge=0),  
    limit: int = Query(5, le=50)  
):
    return {"searched_topic": topic, "skip": skip, "limit": limit}


# 03_multiple_parameters
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float


@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None, description="Optional item data (JSON body)")
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item.model_dump()})
    return result


# 04_header_parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(
    ..., 
    title="The ID of the item"), x_custom_header: str | None = Header(None)):
    return {"item_id": item_id, "X-Custom-Header": x_custom_header}
