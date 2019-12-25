import requests
import re
import time
import os
import wget
import sys
from termcolor import colored
from fake_useragent import UserAgent
from requests.auth import AuthBase
from bs4 import BeautifulSoup
from itertools import groupby
from PIL import Image


ua = UserAgent()
f = open('D:\Documents\PROGRAMMING\pythoncode\Парсер емейлов\links.txt','r')
links_list =  (str(f.read())).split('\n')
f.close()
global img_list
img_list = []

#def links_():
    
def auth_repka(sname,sseo,sprice,smodel,sdesc,number):
    session = requests.Session()
    
    session.auth = ('admin', 'd280a641')
    
    us_ag = {
        'User-Agent': ua.random,
    }
    
    x = session.post('https://repka.net.ua/admin/index.php?route=common/login',
        data = {'username': 'admin', 'password': 'd280a641'},
        headers = us_ag)
    
    token = str(x.url).split('&')[1]
    
    print(number)
    
    session.post('https://repka.net.ua/admin/index.php?route=catalog/product/add&' + token,
                data = {
                    'product_description[1][name]': sname,
                    'product_description[1][description]': '<p>'+ sdesc +'</p>',
                    'product_description[1][meta_title]': sname,
                    'model': smodel,
                    'price': sprice,
                    'tax_class_id': '0',
                    'quantity': '999',
                    'minimum': '1',
                    'subtract': '1',
                    'stock_status_id': '1',
                    'shipping': '1',
                    'date_available': '2019-09-06',
                    'length_class_id': '1',
                    'weight_class_id': '7',
                    'status': '1',
                    'sort_order': '1',
                    'manufacturer_id': '0',
                    'main_category_id': '0',
                    'product_category[]': '73',
                    'product_store[]': '0',
                    'image': 'catalog/pictures/' + str(number) + '.jpg',
                    'product_seo_url[0][1]': sseo,
    })
    
def name():
    global name_str
    global seo_str
    global model_str
    global folder_name
    name_str = str(re.findall(r'<title>(.*?). Цена,',text))
    name_str = name_str[12:]
    name_str = name_str[:-2]
    if name_str[0] == ' ':
        name_str.replace(name_str[name_str.index(' ')],' ')
    
    #Удаление дублей из строки
    s = []
    name_list = name_str.split(' ')
    for e in name_list:
        if e not in s:
            s.append(e)
    name_str = ' '.join(s)

    seo_str = (name_str.replace('!','').replace('Суперцена','').replace(')','').replace('(','').replace('Ноутбук ','').replace(' ','-').replace('Процессор ', '').replace('/','-'))
    
    model_str = (seo_str[seo_str.find('-') + 1:]).replace('-',' ')
    if len(model_str) > 63:
        while len(model_str) > 63:
            model_str = (model_str[:model_str.rindex(' ')])
    
    seo_str = (model_str.replace('!','').replace('Суперцена','').replace(')','').replace('(','').replace('Ноутбук ','').replace(' ','-').replace('+','').replace('Процессор', '').replace(',','').replace('"','').replace("'",''))
    
    if seo_str[(len(seo_str)-1)] == '-':
        seo_str = seo_str[:-1]
        
    if seo_str[0] == '-':
        seo_str = seo_str[1:]
    folder_name = (name_str.replace(' ','_').replace('/','_').replace('\\','_').replace('"','_').replace(':',''))
    #print(model_str)
    #print(seo_str)
    print(colored(name_str,'green'))
    
    

def price():
    global price_str
    price_str = str(soup.find("div", { "name" : "detail-buy-label" }))
    price_str = (re.findall(r'<meta content="(.*?)"',price_str))
    if price_str:
        price_str = str(price_str[0])
        price_str = str(round(int(price_str) * 0.80))
    else:
        print('Price is empty')
        sys.exit()

def price_for_photo():
    global price_str
    price_str = str(soup.find("span", { "class" : "goods-tile__price-value" }))
    print(price_str)
    price_str = (re.findall(r'> (.*?) </span>',price_str))
    print(price_str)
    if price_str:
        price_str = str(price_str[0])
        price_str = str(round(int(price_str) * 0.80))
    else:
        print('Price is empty')
        sys.exit()
    
    
    
    
    
    
def descript():
    global desc
    desc = str(soup.find("div", {"class": "detail-col-description-indent"}))
    desc = str(soup.find("section", {"class": "detail-tabs-i"}))
    desc = str(soup.find("div", {"class": "b-rich-text text-description-content box-hide"}))

    if len(desc) < 20:
        desc = str(soup.find("ul", {"class": "short-chars-l flex"}))
        desc = str(soup.find_all("li", {"class": "short-chars-l-i"}))
    if len(desc) < 20:
        desc = str(soup.find_all("div", {"class": "short-description"})).replace("[", '').replace(']', '')
    desc = str(re.sub('<[^<]+?>', ' ', desc))
    desc = str(desc.replace('\n', ' ').replace(']','').replace('[',''))
        
    
    
    

def imagelink():
    global IMGlink_str
    IMGlink_str = str(soup.find("div", { "class" : "responsive-img" }))
    IMGlink_str = (str(re.findall(r'src="(.*?)"',IMGlink_str))).replace(']','').replace('[','').replace("'",'')
    img_list.append(IMGlink_str)

def ImageLink_for_notebook():
    global IMGlink_str
    IMGlink_str = str(soup.find_all("div", { "name" : "scroll-element" }))
    IMGlink_str = re.findall(r'data-accord-original-url="(.*?)"',text)[4]
    
    img_list.append(IMGlink_str)
    

def zapis(silka):
    x = open('email.txt', 'a', encoding='utf-8')
    x.write('\n\n' + str(i) + '\nНазвание товара : "' +  name_str + '"\n' +'Цена товара : "' + price_str + '"\n' +'Описание товара : "' + desc + '"\n' +  'Ссылка на картинку : "'+IMGlink_str + '"\n' + 'Ссылка на товар : "' + silka + '"')
    x.write('\n' + '%%%%%%******???')
    x.close()
    
j = open('D:\\Documents\\PROGRAMMING\\pythoncode\\Парсер емейлов\\last_img_num.txt','r')    
z = (int((j.readline()).replace('п»ї',''))+ 1)
j.close()
img_num = z
def img_download(i_n):
    print('Beginning file download with wget module')
    wget.download(IMGlink_str, 'D:\\Documents\\PROGRAMMING\\pythoncode\\Парсер емейлов\\pictures\\' +str(i_n) + '.jpg')
    i_n = i_n + 1

not_in_avito = list()
url_without_img = list()
def avito_img(el_link_list):
    
    avito_name = name_str
    try:
        index = ([i for i, symb in enumerate(avito_name) if symb==' '])[5]
    except:
        index = ([i for i, symb in enumerate(avito_name) if symb==' '])[2]
    avito_name = avito_name[:int(index)]
    avito_name = avito_name[:avito_name.find('-')]
    if avito_name[len(avito_name) - 1] == ' ':
        avito_name = avito_name[:-1]
    def find_url(find):
        find = re.findall(r'href="(.*?)"',find)
        return(str(find[0]))
        
        
    html_t = requests.get('https://www.avito.ru/rossiya?q=' + (avito_name.replace(' ','+')))
    soup = BeautifulSoup(html_t.text , "html.parser")
    
    

    product_names = (soup.find_all(attrs={"class": "item-description-title-link"}))
    url_list = list()
    
    
    if 'По вашему запросу ничего не найдено' not in soup:
        if not product_names:
            url_without_img.append(el_link_list)
        for e in product_names:
            url = ('https://www.avito.ru' + find_url(str(e)))
            url_list.append(url)
    else:
        url_without_img.append(el_link_list)
    
    url_list = url_list[-4:] 
    if url_list:
        path = ('D:\\Documents\\PROGRAMMING\\pythoncode\\Парсер емейлов\\pictures\\1-400\\' + folder_name)
        os.makedirs(path)
        for e in url_list:
            html_t = requests.get(e)
            soup = BeautifulSoup(html_t.text , "html.parser")
    
            image_links = (str(soup.find_all(attrs={"class": "gallery-img-frame js-gallery-img-frame"}))).replace('//','')
            image_links = re.findall(r'data-url="(.*?)"',image_links)
            if len(image_links) < 1:
                url_without_img.append(el_link_list)
            for e in image_links:
                try:
                    temp_url = ('http://' + str(e))
                    z = wget.download(temp_url, path)
                    img = Image.open(z)
                    width = img.size[0]
                    height = img.size[1]
                    img= img.crop( (0,0,width,height-40) )
                    img.save(z)
                except:
                    print(colored('Bad img link', 'red'))
                    continue
                    
    
    print(avito_name)
            
    
i = 0

def if_url():
    if url_without_img:
        f = open('D:\Documents\PROGRAMMING\pythoncode\Парсер емейлов\links.txt').read()
    
        for e in url_without_img:
            if e == '':
                url_without_img.pop(url_without_img.index(e))
        f = f.split('\n')
    
        for e in url_without_img:
            try:
                f.pop(f.index(e))
            except:
                print(colored('ЭЛЕМЕНТ НЕ В СПИСКЕ','red'))
    
        f = '\n'.join(f)
        
        x = open('D:\Documents\PROGRAMMING\pythoncode\Парсер емейлов\links.txt','w')
        x.write(str(f))
        x.close()
def jopen():
    j = open('D:\\Documents\\PROGRAMMING\\pythoncode\\Парсер емейлов\\last_img_num.txt','w')
    j.writelines(str(z - 1))
    j.close()

def w_desc():
    desc_path = ('D:\\Documents\\PROGRAMMING\\pythoncode\\Парсер емейлов\\pictures\\1-400\\' + folder_name + '\\' + price_str + '.txt')
    try:
        with open(desc_path,'w',encoding='utf-8') as l:
            l.write(desc)
    
    except:
        print(colored(' ---FOLDER NOT CREATED','red'))
    
for e in links_list:
    if len(e) < 10:
        img_num = img_num + 1
    else:
        pass
    i= i+1
    header = {
        'User-Agent': ua.random,
    }
    html_t = requests.get(e,headers=header)
    soup = BeautifulSoup(html_t.text , "html.parser")
    text = str(soup)
    name()
    price()
    #price_for_photo()
    descript()
    #ImageLink_for_notebook()
    imagelink()
    #auth_repka(name_str,seo_str,price_str,model_str,desc,z)
    img_download(img_num)
    avito_img(e)
    z = z + 1
    print(str(z))
    img_num = z
    if_url()
    w_desc()
    time.sleep(5)
    #zapis(e)
   
jopen()
