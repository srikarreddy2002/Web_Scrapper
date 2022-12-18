
from lib2to3.pgen2 import driver
from multiprocessing import Condition
from xml.dom.minidom import Element
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
driver = webdriver.Chrome(ChromeDriverManager().install())
count=0

driver.get("https://linkedin.com/uas/login")
time.sleep(3)
try:
    Id=driver.find_element(By.ID,"username")
    Id.send_keys(" ") #enter the username of the linkedin account here
    pass_word=driver.find_element(By.ID,"password")
    pass_word.send_keys(" ") #enter the password of the linkedin account here
    driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button").click()
except:
    print("login failed")
    exit()
founders=[]
df=pd.read_csv('companydetails_test.csv')#name of the csv file that contains names of the companies under title name, whoes founder name is to be scraped
array=df['Name']
for company_name in array[0:200] :
    #linkedin will block us after ceratian number of request so try to limt the range of array,reapeat this process till you get data of your desired number of founders
    query=company_name+"+founder"
    url="https://www.google.com/search?q="+str(query)
    time.sleep(2)
    driver.get(url)
    htmlcontent=driver.page_source
    soup=BeautifulSoup(htmlcontent,'html.parser')
    linkedin=soup.find_all("div",class_="yuRUbf")
    linkedin_url=[]
    for x in linkedin:
        link1=x.find_all("a")
        for y in x:
            url=y.get('href')
            if(url!=None):
                if("https://www.linkedin.com" in url):
                    time.sleep(2)
                    linkedin_url.append(url)
    try:
        driver.get(linkedin_url[0])
        time.sleep(1)
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        founder=soup.find("h1",class_="text-heading-xlarge inline t-24 v-align-middle break-words")
        y=founder.text
        founders.append(y)
    except:
        y="ERROR"
        founders.append(y)
file = pd.DataFrame({'Founder Name': founders})
file.to_csv('founder_details_webdesign1.csv')
    







