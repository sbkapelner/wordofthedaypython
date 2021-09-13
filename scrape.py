import requests
from bs4 import BeautifulSoup
import random

def scrape():
    html = requests.get("https://spanish.kwiziq.com/learn/theme/721820").text
    soup = BeautifulSoup(html,"html5lib")
    
    test = soup.find_all('span')
    foreign = soup.find_all("span", {"class" : "txt--lang-foreign"})
    native = soup.find_all("span", {"class" : "txt--lang-native"})
    i = random.randint(0, len(foreign)-1)
    text = native[i].text + ' => ' + foreign[i].text
    
    with open('word.txt','w+') as file:
        file.write(text)