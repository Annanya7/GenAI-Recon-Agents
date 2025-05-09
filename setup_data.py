import os
import shutil
from pathlib import Path

# Define file paths
desktop_path = str(Path.home() / "Desktop")
project_path = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(project_path, "data")

# Create data directory if it doesn't exist
os.makedirs(data_dir, exist_ok=True)

# Files to copy
files = [
    "vss_detail_torpagoinc_visa_20250506.csv",
    "VSS_Trpginc_1000771423_2025050610465322.txt"
]

print("Starting file copy process...")

for file in files:
    source = os.path.join(desktop_path, file)
    destination = os.path.join(data_dir, file)
    
    try:
        shutil.copy2(source, destination)
        print(f"Successfully copied {file} to {data_dir}")
    except FileNotFoundError:
        print(f"Error: Could not find {file} on Desktop")
    except Exception as e:
        print(f"Error copying {file}: {str(e)}")

print("\nFile paths for API calls:")
print("CSV file path:", os.path.join(data_dir, files[0]))
print("TXT file path:", os.path.join(data_dir, files[1]))