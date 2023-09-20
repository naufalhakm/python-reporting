from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload
from datetime import date

from config.Database import (
    get_db_connection,
)
from models.Orders import Order


class OrderRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(
        self,
        date_from: Optional[str],
        to: Optional[str],
    ) -> List[Order]:
        query = self.db.query(Order)

        if date_from != None and to != None:
            query = query.filter(Order.created_at.between(date_from, to))
        elif date_from != None : 
            today = date.today()
            query = query.filter(Order.created_at.between(date_from, today))

        return query.all()
    