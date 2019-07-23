# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests
import xlwt
import xlrd

workbook=xlrd.open_workbook("info1.xls")
worksheet=workbook.sheet_by_index(0)
nrows1 = worksheet.nrows
ncols1 = worksheet.ncols
dd={}
for j in range(1, nrows1):
    datas1 = worksheet.row_values(j)
    id1 = datas1[0]
    url1 = datas1[1]
    title1 = datas1[2]
    author1 = datas1[3]
    if type(title1) is float:
        continue
    dd[int(id1)]=datas1


workbook1=xlrd.open_workbook("cudos_goodreads.xlsx")
worksheet1=workbook1.sheet_by_index(0)
nrows = worksheet1.nrows
ncols = worksheet1.ncols
with open('data.txt', 'w') as f:
    for i in range(1,nrows):
        datas = worksheet1.row_values(i)
        if datas[2]:
            id=datas[2]
            title=datas[1]
            url=datas[3]
            if type(title) is float:
                continue
            if int(id) in dd.keys():
                print(dd[id])
                f.write(str(int(id))+"\t"+url+"\t"+dd[id][2]+"\t"+dd[id][3]+"\n")