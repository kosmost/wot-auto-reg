from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = Firefox()

#search_form = browser.find_elements_by_class_name('s-item__title')
#search_form = search_form[:3]
#search_form.click()

#time.sleep(3)
#search_form = browser.find_element_by_class_name('img500')
#search_form.click()

#time.sleep(1.5)
#x = []
#image_link  = browser.find_element_by_id('viEnlargeImgLayer_img_ctr').get_attribute('src')
#print(image_link)

def ebay_img_download(num):
    browser.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=IdeaPad+S340+14IWL&_sacat=0&LH_TitleDesc=0&rt=nc&LH_ItemCondition=3000')
    search_form = browser.find_elements_by_xpath('.//img[@class="s-item__image-img"]')
    #search_form = browser.find_elements_by_class_name('s-item__image-img')
  
  
    search_form = search_form[num]
    print(search_form)
    search_form.click().perform()
    
    search_form = browser.find_element_by_class_name('img500')
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
            time.sleep(0.7)
            try:
                my_element = browser.find_element_by_xpath('.//a[@class="pntrArr pntrArrNext pntrArrImg activeNext"]')
                my_element.click()
            except:
                print('my_element не найден')
        
        x = x[:index - 1]
    

    for e in x:
        print(e)
    
        
ebay_img_download(0)
print('-----------')
ebay_img_download(1)
print('-----------')
#ebay_img_download(2)
print('-----------')



