import bs4
import requests
import hashlib

s=input("enter site of test, for example \nhttps://www.kpolyakov.spb.ru/school/test9a/15.htm\n")
x = requests.get(s)
y = bs4.BeautifulSoup(x.content,features="html.parser")
z=y.find_all('input', type='hidden')
for i in range(2,len(z)):
    hash_need=z[i]['value']
    masans=[]
    for j in range(0,1000):
        if hashlib.md5(str(j).encode()).hexdigest()==hash_need:
            masans.append(j-1)
    print(z[i]['name'],') ',*masans,sep='')
#
input("нажмите enter что бы закрыть")