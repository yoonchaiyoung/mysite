from MySQLdb import connect
from django.db import models

def insert(name, email, password, gender):
    conn = getconnection()
    cursor = conn.cursor()

    sql = '''
        insert 
        into user 
        values(null, %s, %s, password(%s), %s, now())
    '''
    cursor.execute(sql, (name, email, password, gender))
    conn.commit()

    # 자원 정리
    cursor.close()
    conn.close()

def getconnection():
    return connect(
        user='mysite',
        password='mysite',
        host='192.168.1.138',
        port=3306,
        db='mysite',
        charset='utf8')

