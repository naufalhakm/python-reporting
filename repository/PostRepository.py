from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload
from datetime import date

from config.Database import (
    get_db_connection,
)
from models.Post import Post


class PostRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def getById(self, id : int) -> Post:
        query = self.db.query(Post).filter(Post.ID == id).one()

        return query
    