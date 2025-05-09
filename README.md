# Multi-Agent Transaction Reconciliation System

A multi-agent system for reconciling transaction data from CSV and TXT files using FastAPI and Pydantic.

## Agents

1. **ReconAgent**: Handles the processing of CSV and TXT files
2. **ReportingAgent**: Generates metrics and reconciliation reports
3. **VisualizationAgent**: Creates visual comparisons of the data

## Running in VS Code

1. Open the project in VS Code:
   ```bash
   code /Users/ananyagoel/CascadeProjects/recon_agents
   ```

2. Open VS Code's integrated terminal (Cmd + ` or View -> Terminal)

3. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Copy transaction files (run this first):
   ```bash
   python3 setup_data.py
   ```

6. Start the FastAPI server:
   ```bash
   python3 -m uvicorn main:app --reload --port 8000
   ```

7. Test the API (in a new terminal window):
   ```bash
   curl -X POST http://127.0.0.1:8000/api/v1/reconcile \
   -H "Content-Type: application/json" \
   -d '{
     "csv_file_path": "/Users/ananyagoel/CascadeProjects/recon_agents/data/vss_detail_torpagoinc_visa_20250506.csv",
     "txt_file_path": "/Users/ananyagoel/CascadeProjects/recon_agents/data/VSS_Trpginc_1000771423_2025050610465322.txt"
   }'
   ```

8. View visualization (in a new terminal window):
   ```bash
   python3 -m http.server 8010
   ```
   Then open http://localhost:8010/visualization.html in your browser

## Project Structure

```
recon_agents/
├── app/
│   ├── __init__.py
│   ├── agents.py      # Contains the three agent classes
│   ├── models.py      # Pydantic models for data validation
│   ├── routes.py      # FastAPI route definitions
│   └── services.py    # Service layer for reconciliation
├── data/             # Transaction files directory
├── main.py          # FastAPI application entry point
├── requirements.txt  # Project dependencies
└── setup_data.py    # Script to copy transaction files
```

Send a POST request to `/api/v1/reconcile` with the following JSON body:
```json
{
    "csv_file_path": "/path/to/your/csv/file",
    "txt_file_path": "/path/to/your/txt/file"
}
```

## File Upload

Place your transaction files in the `data` directory:

1. Create a directory named `data` in the project root (if not already present)
2. Copy your CSV and TXT files into the `data` directory
3. When making API calls, use the full path to these files, for example:

```json
{
    "csv_file_path": "/Users/ananyagoel/CascadeProjects/recon_agents/data/vss_detail_torpagoinc_visa_20250507.csv",
    "txt_file_path": "/Users/ananyagoel/CascadeProjects/recon_agents/data/VSS_Trpginc_1000771423_2025050710492520.txt"
}
```

## Project Structure

```
recon_agents/
├── app/
│   ├── agents.py      # Contains the three agent implementations
│   ├── models.py      # Pydantic models
│   ├── routes.py      # API routes
│   └── services.py    # Service layer
├── data/             # Directory for CSV and TXT files
├── main.py           # FastAPI application
└── requirements.txt  # Project dependencies
```
