from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload
from datetime import date

from config.Database import (
    get_db_connection,
)
from models.Jawaban import Jawaban


class JawabanRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(
        self,
        date_from: str,
        to: str,
    ) -> List[Jawaban]:
        query = self.db.query(Jawaban)

        query = query.filter(Jawaban.created_at.between(date_from, to))

        return query.all()
    