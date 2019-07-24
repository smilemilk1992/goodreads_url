# https://www.bklynlibrary.org/

# https://www.bklynlibrary.org/sapi/search.php?search=The%20Berenstain%20Bears%20and%20the%20Truth
# A Counting and Barking Book

#https://borrow.bklynlibrary.org/r1s/iii/encore/search/C__St%3A%28The%20Berenstain%20Bears%20and%20the%20Blame%20Game%29%20a%3A%28Stan%20Berenstain%29__Orightresult__U?lang=eng&suite=def
#   没有完成
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests
import xlwt
import xlrd
url="https://borrow.bklynlibrary.org/r1s/iii/encore/search/C__S{}__Orightresult__U?lang=eng&suite=def"
colum=["cudosid","goodreadsid","title","author","goodreadsUrl","aclibraryUrl","detailUrl"]
file=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet=file.add_sheet("Brooklyn",cell_overwrite_ok=True)
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
        if "None" in author:
            aclibraryUrl =url.format(re.sub('[^0-9a-zA-Z]+', '%20', title))
        else:
            authors=author.split(",")
            st = "t%3A({})".format(title)
            for a in authors:
                st=st+"%20"+"a%3A({})".format(a)
            aclibraryUrl = url.format(st)
        rs=requests.get(aclibraryUrl)
        soup = BeautifulSoup(rs.text, 'html.parser')
        link = soup.find(id="recordDisplayLink2Component")
        if link:
            detailUrl = "https://borrow.bklynlibrary.org/r1s" + link["href"]
        else:
            detailUrl = "None"

        sheet.write(j, 0, cudosid)
        sheet.write(j, 1, goodreadsid)
        sheet.write(j, 2, title)
        sheet.write(j,3,author)
        sheet.write(j, 4, goodreadsUrl)
        sheet.write(j, 5, aclibraryUrl)
        sheet.write(j, 6, detailUrl)
        file.save('Brooklyn.xls')
        print(cudosid,goodreadsid,title,aclibraryUrl,detailUrl)