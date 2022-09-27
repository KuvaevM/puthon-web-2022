import pytest

from src.db import users, user_baskets
from src.auth.routers import auth
from src.contracts import AuthUser, NotAuthUser


def test_auth() -> None:
    test_user = NotAuthUser(user_name="Someone")
    id_user = auth(test_user)
    right_user = AuthUser(user_name=test_user.user_name, user_id=id_user, user_money=100)
    assert id_user in users
    assert id_user in user_baskets
    assert users[id_user] == right_user


def test_similar_auth() -> None:
    test_user1 = NotAuthUser(user_name="someone")
    id_user1 = auth(test_user1)
    right_user1 = AuthUser(user_name=test_user1.user_name, user_id=id_user1, user_money=100)
    test_user2 = NotAuthUser(user_name="someone")
    id_user2 = auth(test_user2)
    right_user2 = AuthUser(user_name=test_user2.user_name, user_id=id_user2, user_money=100)
    assert id_user1 in users
    assert id_user2 in users
    assert id_user1 in user_baskets
    assert id_user2 in user_baskets
    assert users[id_user1] == right_user1
    assert users[id_user2] == right_user2
    assert id_user1 != id_user2


def test_different_double() -> None:
    test_user1 = NotAuthUser(user_name="someone1")
    id_user1 = auth(test_user1)
    right_user1 = AuthUser(user_name=test_user1.user_name, user_id=id_user1, user_money=100)
    test_user2 = NotAuthUser(user_name="someone2")
    id_user2 = auth(test_user2)
    right_user2 = AuthUser(user_name=test_user2.user_name, user_id=id_user2, user_money=100)
    assert id_user1 in users
    assert id_user2 in users
    assert id_user1 in user_baskets
    assert id_user2 in user_baskets
    assert users[id_user1] == right_user1
    assert users[id_user2] == right_user2
    assert id_user1 != id_user2
