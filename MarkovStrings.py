import csv
import markovify

FakeNews=[]
with open('FakeNews.csv',newline='',encoding='utf-8') as csvr:
    text= csvr.read()


for i in range(20):
    model_a= markovify.NewlineText(text,state_size=2)
    model_b= markovify.NewlineText(text,state_size=2)
    model_combo= markovify.combine([model_a,model_b],[1,0.5])
    FakeNews.append(model_combo.make_sentence())
for i in range(20):
    print(f'Titular[{i}]= {FakeNews[i]}')
