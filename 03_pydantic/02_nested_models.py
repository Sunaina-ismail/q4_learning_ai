from pydantic import BaseModel, EmailStr
from typing import List

class Employee(BaseModel):
    name: str
    position: str
    email: EmailStr

class Company(BaseModel):
    company_name: str
    employees: List[Employee]

data = {
    "company_name": "TechZone",
    "employees": [
        {"name": "Ayesha", "position": "Developer", "email": "ayesha@techzone.com"},
        {"name": "Hamzah", "position": "Designer", "email": "hamzah@techzone.com"}
    ]
}

company = Company.model_validate(data)
print(company.model_dump())


