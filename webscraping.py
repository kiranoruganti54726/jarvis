import pandas as pd
import requests
from bs4 import BeautifulSoup
#sending request to website using requests package
response=requests.get("https://www.flipkart.com/search?q=mobiles+under+20000+camera+phone&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_8_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_8_na_na_na&as-pos=4&as-type=RECENT&suggestionId=mobiles+under+20000+camera+phone&requestId=2c281f00-73dd-44b6-b62d-63fc5f8d36c0&as-searchtext=mobiles%20")
print(response)#if response is 200 then we have access to extract data otherwise no

extract=BeautifulSoup(response.content,"html.parser")#website data ni unstructured ga extract chesthadi
#print(extract)

#the <div> tag defines a division or a section in an HTML document divions in this code are price,name,rating

mobilename=extract.find_all("div",class_="_4rR01T")
#print(mobilename)#prints names in unstructured format
names=[]
for i in mobilename:
    d=i.get_text()#text osthadi
    names.append(d)#d loki achina prathi mobile ni empty list loki append chestanam
print(names)#prints names in list format

mobileprice=extract.find_all("div",class_="_30jeq3 _1_WHN1")
prices=[]
for i in mobileprice:
    d=i.get_text()
    s = d[1:]#we are removing the first ₹ from all the prices becuz in excel we get another symbol like @
    prices.append(s)
print(prices)

mobilerating=extract.find_all("div",class_='_3LWZlK')
ratings=[]
for i in mobilerating:
    d=float(i.get_text())#converting '4.5' string to 4.5 float
    ratings.append(d)
print(ratings)

mobileimg=extract.find_all("img",class_="_396cs4 _3exPp9")#for image img tag is used
images=[]
for i in mobileimg:
    d=i["src"]#for image we use this
    images.append(d)
print(images)
#we get a url as output we have to copy and search that inn chrome their we can find the image

mobilelinks=extract.find_all("a",class_="_1fQZEK")#for link "a" module is used
links=[]
for i in mobilelinks:
#href is used to get link href specifies url of page
#with only i["href"] we get mobile link but not the http:flipkart link in the beginning
#to get https:flipkart.com we have to manually copy that and concatenate the string with i["href"]
    d="https://www.flipkart.com"+i["href"]
    links.append(d)
print(links)

df=pd.DataFrame()
print(df)
#df("name of mobile") is column and names is row
df['Mobile name']=names
df['Mobile Price']=prices
#you get error for ratings ndukante aa website la first mobile ki divv function telvakunda thisnav so okati miss avvadam valla rows and columns mismatch aithandi
#df['Mobile Ratings']=ratings
df['Mobile Images']=images
df['Mobile Links']=links
print(df)

df.to_csv('kiran created Mobiles data.csv')#excel file will be created
#this excel file will be in the path of this program