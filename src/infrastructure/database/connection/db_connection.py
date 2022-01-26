import os
from typing import Any, Tuple

from flask import Flask
from flask_sqlalchemy import SQLAlchemy, Pagination

HOST: str = os.getenv('DB_HOST', 'localhost')
PORT: str = os.getenv('DB_PORT', '5432')
USER: str = os.getenv('DB_USER', 'postgres')
PASSWORD: str = os.getenv('DB_PASSWORD', 'password')
DATABASE: str = os.getenv('DB_DATABASE', 'postgres')

DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

db = SQLAlchemy()


def start_connection(app: Flask) -> None:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    db.init_app(app=app)


def get_page_number(p: int) -> int or None:
    return p - 1 if p is not None else None


def get_pagination_limit_and_page(page: int, limit: int) -> Tuple[int, int]:
    page: int = page + 1
    limit: int = limit if limit <= 50 else 50
    return page, limit


def paginated_result(model: Any, result: Pagination, limit: int) -> dict:
    items = list(
        map(
            model.to_json,  # Method we are iterating the loop
            result.items  # Loop we are iterating
        )
    )

    return {
        "previousPage": get_page_number(result.prev_num),
        "currentPage": get_page_number(result.page),
        "nextPage": get_page_number(result.next_num),
        "last": not result.has_next,
        "totalPages": result.pages,
        "totalItems": result.total,
        "maxItemsPerPage": limit,
        "totalItemsPage": len(items),
        "items": items
    }
