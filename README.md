# Tracking Bill Bryson Library Occupancy

### Why?
Durham universitie's main library, the Bill Bryson Library, has a website that displays how busy it is currently. However, there is no way to know how the occupancy of the library changes throughout the day, nor a way to see easily which bookable rooms are booked. The goal of this project is to create a website that combines all the infomation about the library into (from different websites) and track the occupancy so that inferences can be made about how the occupancy changes with respect to time, day, week, term and eventually year.

One other aspect is that just because there are free study spaces, doesn't transalte to there being free study spaces (as students will often take up a whole desk/table for them selves). I will explore what the occupancy actual translates in a qualitative manner.

### How?
Used BeautifulSoup 4 to webscrape the current occupancy from the university website. To collect the data continuously throughout the day, I used an AWS Lambda function with a sheduler (EvenyBridge) and connected it to a DynamoDB table.

### Todo?
Create a website to display results to students. Web scrape the data for the bookable study rooms as well.
