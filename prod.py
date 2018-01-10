import requests
import re
import json
from bs4 import BeautifulSoup

#items will be the list to store all products' data
items=[]

#Defines the Url to access
url="https://www.farmalisto.com.mx/2158-productos-masculinos"
try:
    r=requests.get(url, verify=False)
except:
    print ("Unable to connect")
    exit()

#Gives format to the url content
soup = BeautifulSoup(r.content, "html.parser")
soup.prettify()

#Finds the center block search class which contents al the products listed in the page
products=soup.find_all("div", {"class":"center_block_search"})

#Creates the file products to store the data
with open("products.json", "w") as f:
#This loop gets all the products' attributes
    for item in products:
        #Data will be the dictionary used to stor data for each item
        data = {}
        #Name Product
        data["Name Product"] = item.contents[2].find_all("a")[0].get("title")
        #Price
        data["Price"] = re.findall(r'\$ (.*)', str(item.contents[4].text))[0]
        #Url
        data["url"] = item.contents[2].find_all("a")[0].get("href")
        #Image Url
        data["Image url"] = item.contents[0].find_all("img")[0].get("src")
        #Product ID
        try:
            #print item.contents[5].find_all("a")[0].get("href")
            data["id"] = re.findall(r'id_product=(.*)&', str(item.contents[5].find_all("a")[0].get("href")))[0]
        except:
            pass
        items.append(data)
    dictionary={"prod":items}
    json.dump(dictionary, f)
print ("Ready")
