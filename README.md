Monitoring Task 10

Description:

This script collects system metrics such as CPU usage, RAM usage, and disk usage. Each time the script runs, it appends these metrics (with timestamp and hostname) to a CSV file for later analysis.

Installation
	1.	Clone this repository or download the files.
	2.	Create a virtual environment:

python3 -m venv .venv
	3.	Activate the virtual environment:
	•	macOS/Linux:
            source .venv/bin/activate
	•	Windows:
            .venv\Scripts\activate
	4.	Install required packages:
            pip install -r requirements.txt



How to Run

Run the script with:

python MonitoringTask10+11.py

Output
	•	The script creates/updates a file called MonitoringData.csv.
	•	If the file is empty, a header row is added automatically.
	•	Each run appends the current metrics as new rows.

Thank you!