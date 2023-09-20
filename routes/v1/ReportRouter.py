from typing import Union

from fastapi import APIRouter, Depends, status

from service.ReportService import ReportService

ReportRouter = APIRouter(
    prefix="/api/v1/reports", tags=["report"]
)

@ReportRouter.get("/orders")
async def reportOrders(
    field: Union[str, None] = None, 
    to: Union[str, None] = None, 
    date_from: Union[str, None] = None,
    reportService: ReportService = Depends(),
):
    return ReportService.report(reportService,field,date_from,to)

