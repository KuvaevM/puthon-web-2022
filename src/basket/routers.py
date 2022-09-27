from typing import List

from src.db import users, user_baskets
from src.contracts import AuthUser, Thing, Basket
from fastapi import APIRouter

router = APIRouter(
    prefix='/basket'
)


@router.get('/show')
def user_basket(user_id: str) -> List[str]:
    if user_id not in user_baskets:
        return []
    return {thing.thing_name: thing.thing_cost for thing in user_baskets[user_id]}


@router.post('/add')
def add_thing(basket: Basket, thing: Thing) -> None:
    user_id = basket.owner_id

    if user_id in user_baskets:
        user_baskets[user_id].append(thing)


