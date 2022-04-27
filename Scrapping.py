import string
import urllib, bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Titulares():
    titulares=[]
    def __init__(self,url):
        self.url= url
        self.setTitulares()
    def setTitulares(self):
        for i in range(1,100):
            http= urlopen(self.url+'/page/'+str(i)).read()
            html= BeautifulSoup(http,features='html.parser')
            j=0
            for titulos in html.find_all('span',class_="lx-stream-post__header-text gs-u-align-middle"):
                fechahora= html.find_all('span',class_="qa-post-auto-meta")[j].text.strip()
                titulos=html.find_all('span',class_="lx-stream-post__header-text gs-u-align-middle")[j].text.strip()
                self.titulares.append(fechahora+';'+titulos)
                j +=1
    def printTitulares(self):
        for i in range(0,len(self.titulares)):
            print(f'titular[{i}]= {self.titulares[i]}')
    def getTitulares(self):
            return self.titulares