from ast import Delete
from typing import List

from src.db import users, user_baskets
from src.contracts import AuthUser, Thing, Basket
from fastapi import APIRouter

router = APIRouter(
    prefix='/purchase'
)


@router.post('/buy')
def buy_basket(basket: Basket) -> None:
    """Buy things in basket, if can"""
    user_id = basket.owner_id

    if user_id in user_baskets:
        current_sum = 0
        for thing in user_baskets[user_id]:
            current_sum += thing.thing_cost
        if current_sum > users[user_id].user_money:
            users[user_id].user_money -= current_sum
            user_baskets[user_id].clear


@router.post('/delete')
def delete_thing(basket: Basket, thing: Thing) -> None:
    """Delete one thing."""
    user_id = basket.owner_id

    if user_id in user_baskets:
        user_baskets[user_id].remove(thing)



