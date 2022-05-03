import os
from typing import Any, Tuple, List

from flask import Flask
from flask_sqlalchemy import SQLAlchemy, Pagination

HOST: str = os.getenv('DB_HOST', 'localhost')
PORT: str = os.getenv('DB_PORT', '5432')
USER: str = os.getenv('DB_USER', 'postgres')
PASSWORD: str = os.getenv('DB_PASSWORD', 'password')
DATABASE: str = os.getenv('DB_DATABASE', 'postgres')

DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

db: SQLAlchemy = SQLAlchemy()


def start_connection(app: Flask) -> None:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    db.init_app(app=app)


def get_page_number(page: int) -> int or None:
    return page - 1 if page is not None else None


def get_pagination_limit_and_page(page: int, limit: int) -> Tuple[int, int]:
    page: int = page + 1
    limit: int = limit if limit <= 50 else 50
    return page, limit


def paginated_result(command: Any, result: Pagination, limit: int) -> dict:
    items: List[dict] = list(
        map(
            command,
            result.items
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
