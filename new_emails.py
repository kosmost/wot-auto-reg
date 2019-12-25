import requests
import re
import time
import os
import wget
import sys
import random
from termcolor import colored
from fake_useragent import UserAgent
from requests.auth import AuthBase
from bs4 import BeautifulSoup
from itertools import groupby
from PIL import Image
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains


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
    print(name_str)
    print(model_str)
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

def ebay_img():
    path = ('D:\\Documents\\PROGRAMMING\\pythoncode\\Парсер емейлов\\pictures\\1-400\\' + folder_name + '\\')
    os.makedirs(path)
    ebay_img_str = '+'.join(model_str.split(' ')[:3])
    print(ebay_img_str)
    def ebay_img_download(num):
        
        ebay_link = ()
        browser.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw='+ebay_img_str +'&_sacat=0&LH_TitleDesc=0&rt=nc&LH_ItemCondition=3000')
        
        search_form = browser.find_elements_by_class_name('s-item__image-wrapper')#поиск элемента для перехода к товару
        search_form = search_form[num]
        search_form.click()
    
        time.sleep(1.5)
        search_form = browser.find_element_by_class_name('img500')#клик по картинке товара
        search_form.click()
    
        index = browser.find_elements_by_xpath('.//td[@class="tdThumb"]')
        index = int(((int(len(index)) - 2) / 2) + 1)
    
        i = 0
        x = []
        if index:
            while i < index :
                image_link  = browser.find_element_by_id('viEnlargeImgLayer_img_ctr').get_attribute('src')
        
                x.append(image_link)
                i = i+1
                time.sleep(1.7)
                try:
                    my_element = browser.find_element_by_xpath('.//a[@class="pntrArr pntrArrNext pntrArrImg activeNext"]')
                    my_element.click()
                except:
                    print('my_element не найден')
        
            x = x[:index - 1]
        for e in x:
            print(e)
            wget.download(e, path + '_' + str(num) + '_' + str(random.randint(1,2000)) + '.jpg')
    

        
    
    ebay_img_download(0)
    print('-----------')
    ebay_img_download(1)
    print('-----------')
    ebay_img_download(2)
    
    

def ImageLink_for_notebook():
    global IMGlink_str
    IMGlink_str = str(soup.find_all("div", { "name" : "scroll-element" }))
    IMGlink_str = re.findall(r'data-accord-original-url="(.*?)"',text)[4]
    
    img_list.append(IMGlink_str)
    

    
j = open('D:\\Documents\\PROGRAMMING\\pythoncode\\Парсер емейлов\\last_img_num.txt','r')    
z = (int((j.readline()).replace('п»ї',''))+ 1)
j.close()
img_num = z
def img_download(i_n):
    print('Beginning file download with wget module')
    wget.download(IMGlink_str, 'D:\\Documents\\PROGRAMMING\\pythoncode\\Парсер емейлов\\pictures\\' +str(i_n) + '.jpg')
    i_n = i_n + 1

i = 0

def jopen():
    j = open('D:\\Documents\\PROGRAMMING\\pythoncode\\Парсер емейлов\\last_img_num.txt','w')
    j.writelines(str(z - 1))
    j.close()

def write_description():
    desc_path = ('D:\\Documents\\PROGRAMMING\\pythoncode\\Парсер емейлов\\pictures\\1-400\\' + folder_name + '\\' + price_str + '.txt')
    try:
        with open(desc_path,'w',encoding='utf-8') as l:
            l.write(desc)
    
    except:
        print(colored(' ---FOLDER NOT CREATED','red'))
    

browser = Firefox() #Создание браузера вне цикла что бы не открывать кажыдй раз новый
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
    #imagelink()
    ebay_img()
    #auth_repka(name_str,seo_str,price_str,model_str,desc,z)
    #img_download(img_num)
    z = z + 1
    print(str(z))
    img_num = z
    write_description()
    time.sleep(5)
   
jopen()
