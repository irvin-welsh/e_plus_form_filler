import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

URL="https://e-plus.by"
page=requests.get(URL)
# html=page.read().decode("utf-8")
soup=BeautifulSoup(page.content, "html.parser")

print(soup.findAll("div",id("form-RubricsId")))
# for i in b:
#     a=[]
#     a.append(soup.get_text(i))
#     print(len(a))


# print(b)
