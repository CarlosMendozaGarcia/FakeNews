#ejemplo
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
url='https://www.eltiempo.com'
url2='https://www.dw.com/es/actualidad/s-30684'
http= urlopen(url).read()
http2= urlopen(url2).read()
html= BeautifulSoup(http,features='html.parser')
html2= BeautifulSoup(http2,features='html.parser')
i=0
print('titulos el tiempo')
for titulos in html.find_all('a',class_="title page-link"):
    titulos=html.find_all('a',class_="title page-link")[i].text.strip()
    print (titulos)
    i +=1
print('titulos deutsche welle')
i=0
classname= "linkable ui-accordion-header ui-corner-top ui-accordion-header-collapsed ui-corner-all ui-state-default"
for titulos in html2.find_all('a',class_=classname):
    titulos=html2.find_all('a',class_=classname)[i].getText()
    print (titulos)
    i +=1
print(html2.prettify)
