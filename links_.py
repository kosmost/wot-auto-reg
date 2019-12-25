from bs4 import BeautifulSoup
import requests
import re

link = input(' Введите ссылку  ')

html_t = requests.get(link)
soup = BeautifulSoup(html_t.text , "html.parser")
text = str(soup)
i = 1
links = str(soup.find_all(attrs={"class": "g-i-tile-i-title clearfix"}))
links = re.findall(r'href="(.*?)"',links)

print(str(len(links)))

f = open('links.txt','a')
for x in links:
    f.write(x + '\n')
f.close()

f = open('D:\Documents\PROGRAMMING\pythoncode\Парсер емейлов\links.txt').read()
f = f.split('\n')

x = open('links.txt','w')
x.close()
for e in f:
    if e == '':
        f.pop(f.index(e))

f = '\n'.join(f)
z = open('links.txt','a')
z.write(f)

