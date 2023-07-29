import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

c_path = r"D:\chromedriver.exe"
service = Service(executable_path=c_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.daraz.com.bd/products/laikou-17-ml-i127087185-s1047115173.html?spm=a2a0e.searchlistcategory.list.1.184b6d1eM91dNo&search=1')
driver.maximize_window()


comment_list = []

h = driver.execute_script('return document.body.scrollHeight')

for p in range(0,h+1000,30):
    driver.execute_script(f'window.scrollTo(0,{p});')
    time.sleep(0.4)


all_comments = driver.find_elements(By.CLASS_NAME,'content')
for i in all_comments:
    comment_list.append(i.text)

print(comment_list)


time.sleep(10)

data = {'Comment': comment_list}
df = pd.DataFrame(data)
df.to_csv('comment.csv', index=False)