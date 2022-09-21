from fastapi import APIRouter

from src import contracts

router = APIRouter()


@router.get("/")
def read_root():
    """Hello world!"""
    return {"Text": "Hello world!"}


@router.get("/news/{news_id}")
async def read_item(news_id: int):
    """News id."""
    return {"news_id": news_id}


@router.get("/news/")
async def read_news(news_id: str, text: str | None = None):
    """Read news."""
    if text:
        return {"news_id": news_id, "text": text}
    return {"news_id": news_id, "text": "no news"}


@router.post("/news/")
async def create_news(news: contracts.News):
    """Make description news."""
    news_dict = news.dict()

    if news.description:
        text_with_description = news.description + news.text
        news_dict.update({"text_with_description": text_with_description})
    return news_dict
