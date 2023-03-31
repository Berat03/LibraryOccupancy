from bs4 import BeautifulSoup
import requests
import datetime


class Occupants:
    def __init__(self, date, time, count):
        self.date = date
        self.time = time
        self.count = count


url = 'https://apps.dur.ac.uk/study-spaces/library/bill-bryson/occupancy/display'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
current_occupants = soup.find('text', {'class': 'donut-text'}).string
current_occupants = current_occupants.string.strip()
current_occupants = current_occupants.replace(',', '')
# As soon as we get the count, we also get the date
now = datetime.datetime.now()
date_str = now.strftime('%Y-%m-%d')
time_str = now.strftime('%H:%M')
# todo: if i run the webscraper every x time frame, ill already be tracking the time and so will have the time
# todo: hence, this would be redundant, so remove this once i implement to web server

event = Occupants(date=date_str, time=time_str, count=current_occupants)
