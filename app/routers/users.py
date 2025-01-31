from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from ..db import get_session
from ..schemas import User
from ..utils import pwd_context

router = APIRouter(
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/users/")
def create_user(user: User, session: SessionDep):
    user.password = pwd_context.hash(user.password)
    session.add(user)
    session.commit()
    session.refresh(user)

    return user


@router.get("/users/")
def read_users(
    session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100
) -> list[User]:
    return session.exec(select(User).offset(offset).limit(limit)).all()


@router.get("/users/{user_id}")
async def read_user(user_id: int, session: SessionDep) -> User:
    if user := session.get(User, user_id):
        return user
    raise HTTPException(status_code=404, detail="User not found")
