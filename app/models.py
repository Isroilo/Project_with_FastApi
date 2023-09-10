from pydantic import BaseModel, EmailStr, Field


class Blog(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    text: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Python is the best in the world",
                "text": "Fast api the fasttest in while world of programming"
            }
        }


class User(BaseModel):
    fullname: str = Field(...)
    email:  EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example":{
                "fullname": "Azizbek",
                "email": "azizbek611@gmail.com",
                "password": "any"
            }
        }


class UserLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "azizbek611@gmail.com",
                "password": "any"
            }
        }