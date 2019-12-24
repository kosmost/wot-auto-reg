from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import string
import random

browser = Firefox()

def warg_auth():
    browser.get('https://track.wg-aff.com/click?offer_id=28&pid=965')
    time.sleep(10)
    try:
        link = browser.find_element_by_xpath('//span[@class="button-link_text"]/parent::a').get_attribute('href')
        print('step1')
    except:
        link = browser.find_element_by_xpath('//span[@class="cta-button_text"]/parent::a').get_attribute('href')
        print('step2')
    browser.get(str(link))
    email_str = (str(random.random()) + '@list.ru')
    time.sleep(15)
    search_form = browser.find_element_by_id('id_login')
    search_form.send_keys(email_str)
    
    game_name =''.join(random.choices(string.ascii_uppercase +
                                string.digits, k =18)) 
    search_form = browser.find_element_by_id('id_name')
    search_form.send_keys(game_name)
    browser.find_element_by_id('id_password').send_keys('Waid12345')
    browser.find_element_by_id('id_re_password').send_keys('Waid12345')
    
    search_form = browser.find_element_by_link_text('У вас есть инвайт-код?')
    search_form.click()
    browser.find_element_by_id('id_bonus_code').send_keys('TANKOLET')
    
    search_form = browser.find_element_by_class_name('list-blocks_item')
    search_form.click()
    
    search_form = browser.find_element_by_xpath('//span[@class="b-big-button_inner b-big-button_inner__arrow"]')
    #Нужно подгрузить html код в переменную browser, не ищет следующие два элемента.
    #search_form.click()
    
    #time.sleep(6)
    #search_form = browser.find_element_by_xpath('//a[@class="cm-user-menu-link js-cm-dropdown-link js-cm-event js-cm-user-menu-link cm-user-menu-link__premium"]')
    #search_form.click()
    
    #search_form = browser.find_element_by_xpath('//a[@class="cm-singletons"]')
    #search_form.click()
     
    print(email_str + ':' + 'Waid12345' + '      ' + game_name)
    
    




warg_auth()