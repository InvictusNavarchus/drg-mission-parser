import traceback
import os
from datetime import datetime
import requests
import json
import csv

col_headers = [
    'timestamp',
    'id',
    'CodeName',
    'Biome',
    'Complexity',
    'Length',
    'MissionMutator',
    'MissionWarnings',
    'PrimaryObjective',
    'SecondaryObjective',
    'included_in'
]

def parse_mission_to_csv(mission_dict):
    column_values = [''] * len(col_headers)
    i = 0   
    for column in col_headers:
        if column in mission_dict:
            value = mission_dict[column]
            if type(value) is list:
                value = ','.join(value)
            column_values[i] = value
        i += 1
    print(column_values)
    return column_values

def initialize_csv(csv_path):
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(col_headers)

def write_to_csv(data, csv_path):
    with open(csv_path, 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data)

def parse_json_to_csv(json_path, csv_path):
    with open(json_path, 'r') as json_file:
        json_data = json.load(json_file)
        for timestamp, wrapper in json_data.items():
            if timestamp == 'dailyDeal':
                return
            mission_list = wrapper['Biomes']
            for biome, missions in mission_list.items():
                for mission in missions:
                    mission['timestamp'] = timestamp
                    mission['Biome'] = biome
                    column_values = parse_mission_to_csv(mission)
                    write_to_csv(column_values, csv_path)

current_date_iso = datetime.now().date().isoformat()
initialize_csv(f'{current_date_iso}.csv')

try:
    traverse(f'{current_date_iso}.json', f'{current_date_iso}.csv')
except Exception as e:
    traceback.print_exc()
    os.remove(current_date_iso + '.csv')