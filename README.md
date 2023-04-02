# Tracking Bill Bryson Library Occupancy

### Why?
Durham universitie's main library, the Bill Bryson Library, has a website that displays how busy it is currently. However, there is no way to know how the occupancy of the library changes throughout the day, nor a way to see easily which bookable rooms are booked.

### How?
Used BeautifulSoup 4 to webscrape the current occupancy from the university website. To collect the data continuously throughout the day, I used an AWS Lambda function with a sheduler and connected it to a DynamoDB table. This has been running consistently since 01/04/2023.

### Todo?
Create a website to display results to students. Web scrape the data for the bookable study rooms as well.
