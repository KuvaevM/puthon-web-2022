from fastapi import APIRouter
from src.contracts import AuthUser, NotAuthUser
from src.db import users, user_baskets
from uuid import uuid4 as getid

router = APIRouter(
    prefix="/auth"
)


@router.post("/")
def auth(new_user: NotAuthUser) -> str:
    """Register new user. Init his basket."""
    id_user = str(getid())
    new_user = AuthUser(user_name=new_user.user_name, user_id=id_user, user_money=100)
    users[id_user] = new_user
    user_baskets[id_user] = []
    return id_user
