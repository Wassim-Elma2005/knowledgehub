import psutil
import datetime
import socket
import os
import json
import requests

try:
    metrics = {
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hostname": socket.gethostname(),
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent
    }
except Exception as e:
    print("Error while measuring system metrics", e)
    exit()
    
file_path = os.path.join(os.path.dirname(__file__), 'monitoring_data.json')
def save_metrics():
    data = []

    if os.path.isfile(file_path):
        try:
            with open(file_path, "r") as file:
                try:
                    data = json.load(file)
                except Exception:
                    print("JSON is empty or corrupted, importing new data")
                    exit()
        except Exception as e:
            print("Couldn't read existing JSON file", e)
            exit()
    try:
        data.append(metrics)
        with open("monitoring_data.json", "w") as file:
            json.dump(data, file, indent=2)
            print("Metrics are successfully appended to the JSON file")
    except Exception as e:
        print("Couldn't write to JSON file", e)
        exit()
save_metrics()  

api_url = "http://acishit.e6a7b5gpdse2hdfc.spaincentral.azurecontainer.io:8000/metrics"
try:
    response = requests.post(api_url, json=metrics)
    print(response.status_code)
except Exception as e:
    print("Error while sending metrics to API", e)