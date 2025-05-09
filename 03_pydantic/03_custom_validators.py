from pydantic import BaseModel, EmailStr, field_validator, ValidationError

class Contact(BaseModel):
    name: str
    email: EmailStr

 
    @field_validator("email")
    def email_domain(cls, v):
        if "example.com" not in v:
            raise ValueError("Email must be from the domain 'yahoo.com'")
        return v


try:
    invalid_contact = Contact(name="Alina", email="alina@gmail.com")  
except ValidationError as e:
    print(e)
