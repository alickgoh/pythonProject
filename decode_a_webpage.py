import requests
from bs4 import BeautifulSoup as bs


def PrintHeaders(url):
    r = requests.get(url)
    r_html = r.text

    soup = bs(r_html, 'html.parser')
    title = soup.find_all("h3")

    headers = []

    for i in range(0, len(title)):
        if title[i] not in headers:
            headers.append(title[i].get_text())

    for i in headers:
        print(i + "\n")


PrintHeaders('https://www.nytimes.com')