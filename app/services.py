from .agents import ReconAgent, ReportingAgent, VisualizationAgent
from .models import TransactionData, DashboardOutput

class ReconciliationService:
    def __init__(self):
        self.recon_agent = ReconAgent()
        self.reporting_agent = ReportingAgent()
        self.visualization_agent = VisualizationAgent()

    def process_transactions(self, data: TransactionData) -> DashboardOutput:
        # Process data using ReconAgent
        csv_results = self.recon_agent.process_csv(data.csv_file_path)
        txt_results = self.recon_agent.process_txt(data.txt_file_path)

        # Generate metrics using ReportingAgent
        metrics = self.reporting_agent.generate_metrics(csv_results, txt_results)

        # Create visualizations using VisualizationAgent
        viz_data = self.visualization_agent.create_comparison_chart(csv_results, txt_results)

        # Return consolidated dashboard output
        return DashboardOutput(
            csv_data=csv_results,
            txt_data=txt_results,
            metrics=metrics,
            visualization_data=viz_data
        )
