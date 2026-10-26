from datetime import date
from pydantic import BaseModel, EmailStr, ConfigDict


class StudentBase(BaseModel):
    name: str
    date_of_birth: date
    email: EmailStr
    phone: str | None = None
    course: str | None = None
    address: str | None = None


class StudentCreate(StudentBase):
    pass


class StudentResponse(StudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)