import urllib, bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Titulares():
    titulares=[]
    def __init__(self,url):
        self.url= url
        http= urlopen(url).read()
        self.html= BeautifulSoup(http,features='html.parser')
        self.setTitulares()
    def setTitulares(self):
        i=0
        for titulos in self.html.find_all('a',class_="title page-link"):
            titulos=self.html.find_all('a',class_="title page-link")[i].text.strip()
            self.titulares.append(titulos)
            i +=1
    def printTitulares(self):
        for i in range(0,len(self.titulares)):
            print(f'titular[{i}]= {self.titulares[i]}')