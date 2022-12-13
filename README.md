# IMDbData
First Attempt at Web Scraping
Uses Beautiful Soup (bs4) and requests modules to fetch and parse data from Html page
Data Scrapped is from IMDB's site, source: https://www.imdb.com/chart/top/, Top 250 movies on IMDB
Requests Fetches the data from website
BeautifulSoup Parses the html page and returns the contents in text format
then Openpyxl module can be used to store that data directly on an excel sheet or Pandas can be used to store it in Dataframe, I used openpyxl
