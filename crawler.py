import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def web(page, index, spamwriter, WebUrl=""):
    if(page != 0):
        url = WebUrl + str(index)
        print(url)
        code = requests.get(url)
        
        if (code.ok == False):
            print("Finished")
            return web(0, index, spamwriter)
        
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        
        for header in s.findAll('h2', {'class':'entry-title taggedlink'}):
            link = header.find('a')
            link_title = link.text
            link_url = link.get('href')
            print(link_title, link_url)
            spamwriter.writerow([link_title, link_url])

        web(1, index + 1, spamwriter ,WebUrl)

if __name__ == "__main__":

    URL = ""
    with open('ecs_blogs.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';' , quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['title', 'url'])
        web(1, 0, spamwriter,'http://www.linuxembedded.fr/page/')    
