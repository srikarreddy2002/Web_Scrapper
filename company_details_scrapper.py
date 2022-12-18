import requests
import pandas as pd
from bs4 import BeautifulSoup
company_names=[]
company_locations=[]
company_urls=[]
#rage should be equal to maximum number of pages that the website has
for x in range (200):
    url="https://clutch.co/us/it-services?page="+str(x) 
    r=requests.get(url)
    htmlcontent=r.content

    soup=BeautifulSoup(htmlcontent,'html.parser')

    title=soup.find_all("div",class_="provider-info col-md-10")

    location=soup.find_all("span",class_="locality")

    urls=soup.find_all("li",class_="website-link website-link-a")

    for x in title:
        company_name=x.find("h3",class_="company_info")
        company_names.append(company_name.text.strip())
    for x in location:
        company_locations.append(x.text)
    for link in urls:
        link1=link.find_all("a")
        for x in link1:
            link_url=x["href"]
            company_urls.append(link_url)
file = pd.DataFrame({'Name': company_names,'location': company_locations, 'url': company_urls})
file.to_csv('companydetails_it_services.csv') #enter the name of the file in which the company details should be stored
#details of it services companies from clutch.co are scrapped 