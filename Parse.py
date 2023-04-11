import requests
from bs4 import BeautifulSoup

HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.64',
           'accept':'*/*'}
def get_content():
    URL = 'https://aviata.kz/railways/'
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.find_all('div', class_='popular-direction__list')
    print(str([c.text for c in items])[1397:-2:].replace('\\n','').replace('            ',' ').replace('₸', '₸\n'))
    return str(' ' + str([c.text for c in items])[1397:-2:].replace('\\n','').replace('            ',' ').replace('₸   ', '₸\n'))
# get_content()
