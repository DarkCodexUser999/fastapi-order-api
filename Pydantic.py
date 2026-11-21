# Learning Pydantic used for data validation
from pydantic import BaseModel,Field,EmailStr, field_validator, model_validator
from typing import Any,Optional
#create pydantic 
class Student(BaseModel):
    name: str = Field(min_length= 1, max_length=10, description= "student full name")
    age: int 
    cgpa: float = Field( gt=1, le= 100, default=False, description = "This represents float value", strict = True)
    hostel: bool
    email : EmailStr = Field( description= "Doesnt have .com")
    interest: list[str]
    contact_details : Optional[dict[str, Any]] = None

    @field_validator("email")
    @classmethod
    def email_valid(cls, value):
        if not str(value).endswith(".com"):
            raise ValueError("Email must end with .com domain")
        return value

    @field_validator("age")
    @classmethod
    def check_age(cls, value):
        if value <1 or value> 100:
            raise ValueError("Age must be between 1 and 100")
        return value

    @model_validator( mode="after")
    def check_contact_details(self):
        if self.age > 20 and not self.contact_details:
            raise ValueError("Must have an Emergency Number")
        return self
    
student_info = {
    "name": "Harsh Tari",
    "age": 30,
    "cgpa": 8.9,
    "hostel": True,
    "email": "yoyo@gmail.com",
    "interest": ["FastAPI", "F1"],
    "contact_details": {"email": "harsh@example.com", "phone": 1234567890},
}

#initialize pydantic object to validate cross check gievn input with req foramt
std = Student.model_validate(student_info)

def insert_student(s: Student):
    print(s)

temp = std.model_dump(include =["name","age"])
print(temp)