from bs4 import BeautifulSoup
import requests

url = 'https://apps.dur.ac.uk/study-spaces/library/bill-bryson/occupancy/display'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
count = soup.find('text', {'class': 'donut-text'}).string
count = count.string.strip()
count = count.replace(',', '')
print(count)