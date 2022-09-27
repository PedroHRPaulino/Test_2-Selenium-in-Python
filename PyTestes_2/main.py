import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

nav = webdriver.Chrome()

nav.get('https://ticket-box.s3.eu-central-1.amazonaws.com/index.html')

nav.find_element('id', 'first-name').send_keys('Pedro')
nav.find_element('id', 'last-name').send_keys('Henrique')
nav.find_element('id', 'email').send_keys('pedro@hotmail.com.br')
x = nav.find_element('id', 'ticket-quantity')
drop = Select(x)
drop.select_by_visible_text('1')
nav.find_element('id', 'vip').click()
nav.find_element('id', 'friend').click()
nav.find_element('id', 'publication').click()
nav.find_element('id', 'social-media').click()
nav.find_element('id', 'requests').send_keys('dasdasdasdasmifoaoisfnaodingoaisndfoiansdoifgnaoinfoasi')
nav.find_element('id', 'agree').click()
nav.find_element('id', 'signature').send_keys('Pedro')
nav.find_element('xpath', '//*[@id="app"]/form/div[8]/button[2]').click()
