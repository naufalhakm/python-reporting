from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload
from datetime import date

from config.Database import (
    get_db_connection,
)
from models.Kuesioner import Kuesioner


class KuesionerRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def getById(self, id : int) -> Kuesioner:
        query = self.db.query(Kuesioner).filter(Kuesioner.id == id).one()

        return query
    