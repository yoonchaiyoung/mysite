from MySQLdb import connect
from MySQLdb.cursors import DictCursor
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

def fetchone(email, password):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    sql = '''
            SELECT no, name
            FROM user
            WHERE email=%s AND password=password(%s)
            '''
    cursor.execute(sql, (email, password))
    result = cursor.fetchone()

    # 자원 정리
    cursor.close()
    conn.close()

    return result



def fetchonebyno(no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    sql = '''
            SELECT *
            FROM user
            WHERE no=%s;
            '''

    cursor.execute(sql, (no,))
    result = cursor.fetchone()

    # 자원 정리
    cursor.close()
    conn.close()

    return result


def update(name, email, password, gender, no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    sql = '''
            UPDATE user
            SET name=%s, email=%s, password=password(%s), gender=%s
            WHERE no=%s
        '''

    cursor.execute(sql, (name, email, password, gender, str(no)))
    conn.commit()

    # 자원 정리
    cursor.close()
    conn.close()

    return



def getconnection():
    return connect(
        user='mysite',
        password='mysite',
        host='192.168.1.138',
        port=3306,
        db='mysite',
        charset='utf8')

