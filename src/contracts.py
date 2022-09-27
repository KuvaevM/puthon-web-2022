from pydantic import BaseModel


class NotAuthUser(BaseModel):
    """New user."""
    user_name: str


class AuthUser(BaseModel):
    """Register user."""
    user_name: str
    user_id: str
    user_money: int


class Basket(BaseModel):
    """User basket."""
    owner_id: str


class Thing(BaseModel):
    """Stuff from shop."""
    thing_name: str
    thing_id: str
    thing_cost: int
