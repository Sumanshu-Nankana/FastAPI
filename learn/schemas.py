from pydantic import BaseModel, Emaiilstr

class Users(BaseModel):
	username : str
	email : Emailstr
	password: str
