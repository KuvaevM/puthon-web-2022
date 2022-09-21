from pydantic import BaseModel


class News(BaseModel):
    """Contract for item."""

    name: str
    description: str | None = None
    text: str
