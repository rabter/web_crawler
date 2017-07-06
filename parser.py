import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib3.util import parse_url
import csv

def start_parse():

    # csv file reader
    for row in csv.reader(open('input_file.csv'), delimiter=';'):
        print(row)


    # html parse
    req = requests.get('[URL]')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find_all('div')[0]
    print(div)

    # selenium + BeautifulSoup
    try:
        driver = webdriver.Chrome('[CHROME_DRIVER_PATH]')
        driver.implicitly_wait(3)
        driver.get('[URL]')
        html = driver.page_source

        soup = BeautifulSoup(html)

    except Exception as e:
        print(e)

    # csv file writer
    with open('./output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        writer.writerows([ARRAY])

        
if __name__ == "__main__":
    print('===== start =====')
    start_parse()
