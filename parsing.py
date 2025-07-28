import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup

web_page = requests.get('https://lyceum62kem.ru/litsey/kollektiv-litseya.php')
soup = BeautifulSoup(web_page.text, 'html.parser')

work_book = Workbook()
work_sheet = work_book.active

items = soup.find_all(class_='gallery')

for elem in items:
    name = elem.find(class_='desc').text.strip()
    name = name.replace("\n\t\t ", " ")

    position = elem.find(class_='desc2').text.strip()
     
    row = [name, position]
    print(row)
    work_sheet.append(row)

work_book.save('Коллектив лицея.xlsx')

'''
web_page = requests.get('https://live.skillbox.ru/playlists/code/python/')
soup = BeautifulSoup(web_page.text, 'html.parser')

work_book = Workbook()
work_sheet = work_book.active

items = soup.find_all(class_='playlist-inner__item')

for elem in items:
    title = elem.find(class_='playlist-inner-card__link-text').text
    relative_url = elem.find(class_='playlist-inner-card__link').attrs['href']
    timing = elem.find(class_='playlist-inner-card__small-info').text.strip().split(',')[-1].strip()
    url = 'https://live.skillbox.ru' + relative_url
    row = [title, url, timing]
    print(row)
    work_sheet.append(row)

work_book.save('Вебинары про Python от Skillbox.xlsx')
'''