# https://www.bklynlibrary.org/

# https://www.bklynlibrary.org/sapi/search.php?search=The%20Berenstain%20Bears%20and%20the%20Truth
# A Counting and Barking Book
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests
import xlwt
import xlrd
url="https://www.bklynlibrary.org/sapi/search.php?search={}"
colum=["id","title","goodreadsUrl","aclibraryUrl","detailUrl"]
file=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet=file.add_sheet("Brooklyn",cell_overwrite_ok=True)
for i in colum:
    sheet.write(0, colum.index(i), i)
j=0
workbook=xlrd.open_workbook("cudos_goodreads.xlsx")
worksheet=workbook.sheet_by_index(0)
nrows = worksheet.nrows
ncols = worksheet.ncols
for i in range(1,nrows):
    j=j+1
    datas = worksheet.row_values(i)
    if worksheet.row_values(i-1)[2] == datas[2]:
        continue
    if datas[2]:
        id=int(datas[2])
        title=datas[1]
        if type(title) is float:
            continue
        goodreadsUrl=datas[3]
        aclibraryUrl =url.format(re.sub('[^0-9a-zA-Z]+', '%20', datas[1]))
        rs=requests.get(aclibraryUrl)
        soup = BeautifulSoup(rs.text, 'xml')
        link=soup.find("a",{"class":"text-white"})["href"] if soup.find("a",{"class":"text-white"}) else None
        if link:
            detailUrl = link
        else:
            detailUrl="None"
        if id:
            sheet.write(j, 0, id)
            sheet.write(j, 1, title)
            sheet.write(j, 2, goodreadsUrl)
            sheet.write(j, 3, aclibraryUrl)
            sheet.write(j, 4, detailUrl)
            file.save('Brooklyn.xls')
            print(id,title,aclibraryUrl,detailUrl)