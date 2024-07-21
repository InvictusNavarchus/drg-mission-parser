import traceback
from datetime import datetime
import json
import os
import requests

def fetch_json(url):
    response = requests.get(url)
    data = response.json()
    return data

def update_json(local_json_path, remote_json_url):
    if os.path.isfile(local_json_path):        
        return
    with open(local_json_path, 'w') as json_file:
        json_data = fetch_json(remote_json_url)
        json.dump(json_data, json_file, indent=4)

base_url = 'https://doublexp.net/static/json/bulkmissions/'
current_date_iso = datetime.now().date().isoformat()
local_json_path = current_date_iso + '.json'
remote_json_url = base_url + local_json_path

try:
    update_json(local_json_path, remote_json_url)
except:
    traceback.print_exc()
    os.remove(local_json_path)