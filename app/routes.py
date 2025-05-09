from fastapi import APIRouter, HTTPException
from .models import TransactionData, DashboardOutput
from .services import ReconciliationService

router = APIRouter()
service = ReconciliationService()

@router.post("/reconcile", response_model=DashboardOutput)
async def reconcile_transactions(data: TransactionData):
    try:
        return service.process_transactions(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))