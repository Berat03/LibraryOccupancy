from bs4 import BeautifulSoup
import requests
import datetime
import boto3

class Occupants:
    def __init__(self, date, time, count):
        self.date = date
        self.time = time
        self.count = count

def get_occupancy_count():
    url = 'https://apps.dur.ac.uk/study-spaces/library/bill-bryson/occupancy/display'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    current_occupants = soup.find('text', {'class': 'donut-text'}).string
    current_occupants = current_occupants.strip().replace(',', '')
    now = datetime.datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M')
    return Occupants(date=date_str, time=time_str, count=current_occupants)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BBTable')





def lambda_handler(event, context):
    occupancy = get_occupancy_count()
    print(table)
    table.put_item(Item={
        'Date': occupancy.date,
        'Time': occupancy.time,
        'Count': occupancy.count,
    }
)
