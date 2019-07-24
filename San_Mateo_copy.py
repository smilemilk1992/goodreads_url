# https://smcl.org/
# https://smcl.bibliocommons.com/v2/search?query=The+Grumpus+Under+the+Rug&searchType=smart
# https://smcl.bibliocommons.com/item/show/2351553076

# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests
import xlwt
import xlrd
url="https://smcl.bibliocommons.com/v2/search?query={}&searchType=smart"
colum=["cudosid","goodreadsid","title","author","goodreadsUrl","aclibraryUrl","detailUrl"]
file=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet=file.add_sheet("San_Mateo",cell_overwrite_ok=True)
for i in colum:
    sheet.write(0, colum.index(i), i)
j=0


with open('cudos_goodreads.txt', "r",encoding="utf-8") as f:
    datas = f.readlines()
    for data in datas:
        j = j + 1
        data=data.strip().split("\t")
        cudosid=int(data[0])
        goodreadsid=int(data[1].replace("https://www.goodreads.com/book/show/",""))
        goodreadsUrl=data[1]
        title=data[2]
        author=data[3]
        aclibraryUrl = url.format(re.sub('[^0-9a-zA-Z]+', '+', title+"+"+author))
        rs=requests.get(aclibraryUrl)
        soup = BeautifulSoup(rs.text, 'html.parser')
        link = soup.find("h2", {"class": "cp-title"}).a["href"] if soup.find("h2", {"class": "cp-title"}) else None
        if link:
            detailUrl = "https://smcl.bibliocommons.com" + link
        else:
            detailUrl = "None"

        sheet.write(j, 0, cudosid)
        sheet.write(j, 1, goodreadsid)
        sheet.write(j, 2, title)
        sheet.write(j,3,author)
        sheet.write(j, 4, goodreadsUrl)
        sheet.write(j, 5, aclibraryUrl)
        sheet.write(j, 6, detailUrl)
        file.save('San_Mateo.xls')
        print(cudosid,goodreadsid,title,aclibraryUrl,detailUrl)