import requests
import pandas as pd
from bs4 import BeautifulSoup
names=[]
urls=[]
location=[]
for i in range(200):
    url="https://www.goodfirms.co/directory/platforms/top-web-design-companies?page="+str(i)
    r=requests.get(url)
    htmlcontent=r.content
    soup=BeautifulSoup(htmlcontent,'html.parser')
    title=soup.find_all(class_="service-provider")
    links=soup.find_all("div",class_="firms-r")
    locations=soup.find_all("div",class_="firm-location")
    for x in title:
        y=x.get('id')
        names.append(y)
    for x in links:
        link1=x.find_all("a")
        for y in link1:
            company_url=y["href"]
            urls.append(company_url)
    for x in locations:
        location.append(x.text.strip())
file=pd.DataFrame({'Name': names,'locality': location,'url': urls})
file.to_csv('companydetails_goodfirms.csv')