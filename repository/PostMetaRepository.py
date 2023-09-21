from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload
from datetime import date

from config.Database import (
    get_db_connection,
)
from models.PostMeta import PostMeta


class PostMetaRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def getMetaValue(self, id : int, meta_key : str) -> PostMeta:
        query = self.db.query(PostMeta).filter(PostMeta.post_id == id).filter(PostMeta.meta_key == meta_key).one()

        return query
    