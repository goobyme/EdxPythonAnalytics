import requests
import pymysql
import bs4


def webdl(url):
    """Downloads web-page, retries on initial failures, returns None if fails thrice (common!)"""
    print('Downloading...{}'.format(url))
    for i in range(3):
        try:
            r = requests.get(url)
            r.raise_for_status()
            return r
        except:     # Ugly but it works, hard to account for all the possible error codes otherwise
            print('[Warning webdl]: Retrying Download')
            continue
    print('[Error webdl]: Download failed for {}'.format(url))
    return None


def get_quote(html=str):
    soup = bs4.BeautifulSoup(html)
    soup.find('')
    ticker = ''
    stock = ''

    return {'stock': stock, 'ticker': ticker}


def write_to_db(json):
    db = pymysql.connect('localhost', 'root', None, database='stock_db')
    cursor = db.cursor()

    cursor.execute("")


