#ejemplo
import urllib
from bs4 import BeautifulSoup
from Scrapping import Titulares

url='https://www.eltiempo.com'
Tiempo= Titulares(url)
Tiempo.printTitulares()
