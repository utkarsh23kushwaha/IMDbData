from bs4 import BeautifulSoup
import requests
import openpyxl

excel=openpyxl.Workbook()
print(excel.sheetnames)
sheet=excel.active
sheet.title='Top Rated Movies'
sheet.append(['Rank','Movie','Year','rating'])
link= requests.get('https://www.imdb.com/chart/top/')
link.raise_for_status()
soup = BeautifulSoup(link.text, 'html.parser')

data = soup.find('tbody', class_="lister-list").find_all('tr')
for movie in data:
    name=movie.find('td', class_='titleColumn').a.text
    rank=movie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
    year=movie.find('td',class_='titleColumn').span.text.strip('()')
    rating=movie.find('td', class_="ratingColumn imdbRating").strong.text

    sheet.append([rank,name,year,rating])

excel.save('IMDB_Data.xlsx')