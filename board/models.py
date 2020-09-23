from django.db import models
from MySQLdb import connect
from MySQLdb.cursors import DictCursor

def getconnection():
    return connect(
        user='mysite',
        password='mysite',
        host='192.168.1.138',
        port=3306,
        db='mysite',
        charset='utf8')

def fetchlist():
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    sql = '''
        SELECT b.no, b.title, a.name, b.hit, b.reg_date
        FROM user a, board b
        WHERE a.no=b.user_no
        ORDER BY reg_date DESC
        '''
    cursor.execute(sql)
    results = cursor.fetchall()

    # 자원 정리
    cursor.close()
    conn.close()

    return results

def insert(title, content, no):
    conn = getconnection()
    cursor = conn.cursor()

    sql = '''
        INSERT
        INTO board
        VALUES(null, %s, %s, 0, now(), (SELECT MAX(g_no)+1
										          FROM board b), 1, 1, %s)
          '''
    cursor.execute(sql, (title, content, str(no)))
    conn.commit()

    # 자원 정리
    cursor.close()
    conn.close()