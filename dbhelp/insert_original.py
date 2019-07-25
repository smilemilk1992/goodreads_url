# -*- coding: utf-8 -*-
import MySQLdb

class insertDb:
    def mysqlhelp(item):
        conn = MySQLdb.connect(
            host='120.27.218.142',
            port=3306,
            user='worker',
            passwd='worker',
            db='test',
            charset="utf8"
        )
        cur = conn.cursor()
        sql = '''INSERT IGNORE into p_news_originalUrl1(cudosId,goodreadsId,title,goodreadsUrl,goodreadsReq,goodreadsAmazonUrl,AmazonUrl,goodreadsAlibrisUrl,AlibrisUrl,goodreadsWalmarteBooksUrl,WalmarteBooksUrl,goodreadsBarnesNoble,BarnesNoble,goodreadsIndieBound,IndieBound,goodreadsIndigo,Indigo)value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

        insertdata = (
            item['cudosId'],
            item['goodreadsId'],
            item['title'],
            item['goodreadsUrl'],
            item['goodreadsReq'],
            item['goodreadsAmazonUrl'],
            item['AmazonUrl'],
            item['goodreadsAlibrisUrl'],
            item['AlibrisUrl'],
            item['goodreadsWalmarteBooksUrl'],
            item['WalmarteBooksUrl'],
            item['goodreadsBarnesNoble'],
            item['BarnesNoble'],
            item['goodreadsIndieBound'],
            item['IndieBound'],
            item['goodreadsIndigo'],
            item['Indigo']
        )
        cur.execute(sql, insertdata)
        conn.commit()
        cur.close()
        conn.close()