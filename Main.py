import nltk
from Scrapping import Titulares
from csv import writer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize


url='https://www.bbc.com/mundo/topics/c2lej05epw5t'
BBC= Titulares(url)
titulosejemplo=BBC.getTitulares()

#escribe los titulares en el csv
print('cambio')
with open('FakeNews.csv','w',newline='',encoding='utf-8') as f:
    for titulo in titulosejemplo:
        f.write(titulo+'\n')


listword=[]
for i in range(0,len(titulosejemplo)):
    aux= word_tokenize(titulosejemplo[i])
    listword.append(aux)

stop_words= set(stopwords.words('spanish'))
filteredlist=[]

for i in range(0,len(listword)):
    for word in listword[i]:
        if word.casefold() not in stop_words:
            filteredlist.append(word)
Nouns=[]
