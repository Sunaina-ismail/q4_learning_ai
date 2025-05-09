from pydantic import BaseModel, ValidationError
from typing import Optional


class Student(BaseModel):
    roll_number: int
    name: str
    email: str
    grade: Optional[str] = None 


student_data = {
    "roll_number": 56,
    "name": "Babar Azam",
    "email": "babar.azam@example.com",
    "grade": "A1"
}
student = Student(**student_data)
print(student)  
print(student.model_dump())  



try:
    invalid_student = Student(roll_number=102, name="Mohammad Ali")
except ValidationError as e:
    print(e)
