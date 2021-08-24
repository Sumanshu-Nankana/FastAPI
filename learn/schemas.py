from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

class UserCreate(BaseModel):
	email : EmailStr
	password: str

class ShowUser(BaseModel):
	email : EmailStr
	is_active : bool

	class Config:
		orm_mode = True


class ItemBase(BaseModel):
	title : Optional[str]
	description : Optional[str]
	date_posted : Optional[date] = datetime.now().date()

class ItemCreate(ItemBase):
	title : str
	description : str

class ShowItem(ItemBase):
	title : str
	description : str
	date_posted : date

	class Config:
		orm_mode = True
