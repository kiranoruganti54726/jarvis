'''
Web Scrapping extracts the data from websites in the unstructured format.
It helps to collect these unstructured data and convert it in a structured form.
'''







'''
pip:

pip is the standard package manager for Python. 
It allows you to install and manage additional packages.

'''
#installations
# pip install pandas
# pip install requests
# pip install beautifulsoup4
import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp3&fm=neo%2Fmerchandising&iid=M_a854b0e4-215b-40ef-8ac4-609c9d47b1b8_3.Q1PDG4YW86MF&ppt=hp&ppn=homepage&ssid=9igh02irkw0000001658324345497")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
names=soup.find_all('div',class_='_4rR01T')
# print(names)
name=[]
for i in names:
    d=i.get_text()
    name.append(d)



price=soup.find_all('div',class_='_30jeq3 _1_WHN1')
# print(names)
prices=[]
for i in price:
    d=i.get_text()
    s=d[1:]
    prices.append(s)



rate=soup.find_all('div',class_='_3LWZlK')
# print(names)
ratings=[]
for i in rate:
    d=float(i.get_text())
    ratings.append(d)

image=soup.find_all('img',class_='_396cs4 _3exPp9')
# print(names)
images=[]
for i in image:
    d=i['src']
    images.append(d)



link=soup.find_all('a',class_='_1fQZEK')
# print(names)
links=[]
for i in link:
    d='https://www.flipkart.com'+i['href']
    links.append(d)
print(links)

df=pd.DataFrame()

df['Name of Mobile']=name
df['Mobile Price']=prices
df['Mobile Ratings']=ratings
df['Mobile Images']=images
df['Mobile Links']=links
print(df)

df.to_csv('Mobiles_data.csv')