from pydantic import BaseModel
from typing import Dict
from datetime import datetime

class TransactionData(BaseModel):
    csv_file_path: str
    txt_file_path: str

class ReconciliationResult(BaseModel):
    sales_amount: float
    refund_amount: float
    sales_count: int
    refund_count: int
    source: str

class ReportMetrics(BaseModel):
    sales_difference: float
    refund_difference: float
    sales_count_difference: int
    refund_count_difference: int
    is_reconciled: bool
    timestamp: datetime

class DashboardOutput(BaseModel):
    csv_data: ReconciliationResult
    txt_data: ReconciliationResult
    metrics: ReportMetrics
    visualization_data: Dict