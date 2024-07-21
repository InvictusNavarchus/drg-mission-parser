import traceback
from datetime import datetime
import json
import os
import requests

def fetch_json(url):
    response = requests.get(url)
    data = response.json()
    return data

def update_json(iso_timestamp, local_json_path, remote_json_url):
    if os.path.isfile(local_json_path):
        return
    with open(local_json_path, 'w') as json_file:
        json_data = fetch_json(remote_json_url)
        json.dump(json_data, json_file, indent=4)