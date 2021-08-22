from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
	email : EmailStr
	password: str
