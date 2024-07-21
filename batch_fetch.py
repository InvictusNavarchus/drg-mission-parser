from datetime import datetime, timedelta
from main import main

def to_iso_str(date_obj:datetime) -> str:
    return date_obj.date().isoformat()

def batch_fetch(start_date_str:str, end_date_str:str):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    current_date = start_date
    while current_date <= end_date:
        current_date_str = to_iso_str(current_date)
        print(f'fetching and parsing {current_date_str}.json')
        main(current_date_str, f'json/{current_date_str}.json', f'csv/{current_date_str}.csv')
        current_date = current_date + timedelta(days=1)

batch_fetch('2024-07-30', '2024-07-31')