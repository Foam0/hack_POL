def hack_hash(hash_need, where_to_add):
    for j in range(-1000, 1000):
        if hashlib.md5(str(j).encode()).hexdigest() == hash_need:
            answers[where_to_add].append(j)


import hashlib

import bs4
import requests

# bs4.BeautifulSoup(requests.get("https://www.kpolyakov.spb.ru/school/test9a/15.htm").content).find_all('div', {'class': 'q'})
s = input("enter site of test, for example \nhttps://www.kpolyakov.spb.ru/school/test9a/15.htm\n")
x = requests.get(s)
y = bs4.BeautifulSoup(x.content, features="html.parser")
answers = dict()
questions = y.find_all('div', {'class': 'q'})
for i in range(len(questions)):
    answers[questions[i]['id']] = []
    if str(questions[i]).find('value="введите число"') != -1:
        hack_hash(questions[i].find_next('input', {'type': 'hidden'})['value'], questions[i]['id'])
    else:
        boxes = bs4.BeautifulSoup(str(questions[i].contents[0]),features="html.parser").find_all('td', {'class': ['radio', 'ans']})
        for j in range(0, len(boxes), 2):
            if boxes[j].find_next('input')['value'] == '1':
                answers[questions[i]['id']].append(boxes[j + 1].contents[0])

#
for i in answers.keys():
    print(i,end=': ')
    for j in answers[i]:
        print(j,end=' ')
    print()
input("нажмите enter что бы закрыть")
