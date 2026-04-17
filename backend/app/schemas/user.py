from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    last_name: str
    first_name: str
    email: str

    model_config = {"from_attributes": True}


class UserCreate(BaseModel):
    last_name: str
    first_name: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
