from pydantic import BaseModel
import pandas as pd
import numpy as np
import re
import plotly.graph_objects as go
from datetime import datetime
from typing import Dict, List
from .models import ReconciliationResult, ReportMetrics, DashboardOutput

class ReconAgent(BaseModel):
    """Agent responsible for reconciliation of transaction data"""
    
    def process_csv(self, file_path: str) -> ReconciliationResult:
        try:
            df = pd.read_csv(file_path)
            df['Type'] = df['Type'].str.strip().str.upper()
            df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
            
            sales_total = df[df['Type'] == 'SALE']['Amount'].sum()
            refund_total = -abs(df[df['Type'] == 'REFUND']['Amount'].sum())
            
            return ReconciliationResult(
                sales_amount=float(sales_total if not pd.isna(sales_total) else 0),
                refund_amount=float(refund_total if not pd.isna(refund_total) else 0),
                sales_count=len(df[df['Type'] == 'SALE']),
                refund_count=len(df[df['Type'] == 'REFUND']),
                source='CSV'
            )
        except Exception as e:
            raise ValueError(f"Error processing CSV: {str(e)}")

    def process_txt(self, file_path: str) -> ReconciliationResult:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            purchase_amount = 0
            refund_amount = 0
            purchase_count = 0
            refund_count = 0

            for line in lines:
                if "PURCHASE" in line:
                    matches = re.findall(r'\s+(\d+)\s+[0-9,.]+\s+(\d+)\s+([0-9,.]+)', line)
                    if matches:
                        count = int(matches[0][1])
                        amount = float(matches[0][2].replace(',', ''))
                        purchase_count = count
                        purchase_amount = amount

                elif "MERCHANDISE CREDIT" in line:
                    matches = re.findall(r'\s+(\d+)\s+([0-9,.]+)', line)
                    if matches:
                        count = int(matches[0][0])
                        amount = float(matches[0][1].replace(',', ''))
                        refund_count = count
                        refund_amount = amount

            return ReconciliationResult(
                sales_amount=purchase_amount,
                refund_amount=refund_amount,
                sales_count=purchase_count,
                refund_count=refund_count,
                source='TXT'
            )
        except Exception as e:
            raise ValueError(f"Error processing TXT: {str(e)}")

class ReportingAgent(BaseModel):
    """Agent responsible for generating reports and metrics"""
    
    def generate_metrics(self, csv_data: ReconciliationResult, txt_data: ReconciliationResult) -> ReportMetrics:
        tolerance = 0.01
        
        sales_diff = csv_data.sales_amount - txt_data.sales_amount
        refund_diff = abs(csv_data.refund_amount) - txt_data.refund_amount
        
        is_reconciled = (abs(sales_diff) <= tolerance and abs(refund_diff) <= tolerance)
        
        return ReportMetrics(
            sales_difference=sales_diff,
            refund_difference=refund_diff,
            sales_count_difference=csv_data.sales_count - txt_data.sales_count,
            refund_count_difference=csv_data.refund_count - txt_data.refund_count,
            is_reconciled=is_reconciled,
            timestamp=datetime.now()
        )

class VisualizationAgent(BaseModel):
    """Agent responsible for creating visualizations"""
    
    def create_comparison_chart(self, csv_data: ReconciliationResult, txt_data: ReconciliationResult) -> Dict:
        fig = go.Figure()
        
        # Add bars for CSV data
        fig.add_trace(go.Bar(
            name='CSV',
            x=['Sales', 'Refunds'],
            y=[csv_data.sales_amount, abs(csv_data.refund_amount)],
            marker_color=['#1f77b4', '#ff7f0e']
        ))
        
        # Add bars for TXT data
        fig.add_trace(go.Bar(
            name='TXT',
            x=['Sales', 'Refunds'],
            y=[txt_data.sales_amount, txt_data.refund_amount],
            marker_color=['#1f77b4', '#ff7f0e'],
            opacity=0.7
        ))
        
        fig.update_layout(
            title='Transaction Comparison: CSV vs TXT',
            barmode='group',
            yaxis_title='Amount ($)',
            template='plotly_white'
        )
        
        return fig.to_dict()
