import traceback
import os
from datetime import datetime

from update_json import update_json
from json_to_csv import parse_json_to_csv

def main(iso_timestamp, local_json_path, csv_path):
    # Fetch new json if doesn't exist yet
    if os.path.isfile(local_json_path) == False:
        print("Fetching new json...")
        remote_base_url = 'https://doublexp.net/static/json/bulkmissions/'
        remote_json_url = f'{remote_base_url}{iso_timestamp}.json'
        try:
            update_json(iso_timestamp, local_json_path, remote_json_url)
        except:
            traceback.print_exc()
            os.remove(local_json_path)
    else:
        print(f'{local_json_path} already exists')

    # parse json to csv if doesn't done yet
    if os.path.isfile(csv_path) == False:
        print("Parsing json to csv...")
        try:
            parse_json_to_csv(iso_timestamp, local_json_path, csv_path)
        except:
            traceback.print_exc()
            os.remove(csv_path)
    else:
        print(f'{csv_path} already exists')

iso_timestamp = datetime.now().date().isoformat()
main(iso_timestamp, f'json/{iso_timestamp}.json', f'csv/{iso_timestamp}.csv')