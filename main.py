from typing import List
from enum import Enum

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    CANCEL = "cancel"

class User(BaseModel):
    id: int = 0
    name: str
    role: str
    projectName: str
    status: Status = Status.ACTIVE
    salary: int = 0

user_list: List[User] = [
    User(id=9328947384, name="Juan", role="Admin", projectName="admin", status=Status.ACTIVE, salary=1000),
    User(id=3948832113, name="Lindsey Curtis", role="Web Designer", projectName="Agency Website", status=Status.PENDING, salary=2000),
    User(id=3932894928, name="Zain Geidt", role="Content Writing", projectName="Blog Writing", status=Status.ACTIVE, salary=3000),
    User(id=3290389421, name="Abram Schleifer", role="Digital Marketer", projectName="Social Media", status=Status.CANCEL, salary=6000),
    User(id=9239239481, name="Kathleen Hanner", role="SEO Expert", projectName="SEO", status=Status.INACTIVE, salary=10000),
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health", status_code=status.HTTP_200_OK)
def health():
    return {"status": "ok"}

@app.get("/users", status_code=status.HTTP_200_OK)
def get_user():
    return user_list

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    for u in user_list:
        if u.id == user.id:
            raise HTTPException(status_code=400, detail="User already exist")
        
    user_list.append(user.model_dump())    
    return user.model_dump()