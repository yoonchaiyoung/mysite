# from django.test import TestCase

import guestbook.models as guestbookmodel

# def test_guestbookmodel_insert():
#     guestbookmodel.insert('윤채영', '1234', '안녕하세요~')
#
# def test_guestbookmodel_fetchlist():
#     results = guestbookmodel.fetchlist()
#     print(results)


# def test_guestbookmodel_delete():
#     guestbookmodel.delete(6, '1234')



# test_guestbookmodel_insert()
# test_guestbookmodel_fetchlist()

# test_guestbookmodel_delete()

def test_guestbookmodel_delete():
    guestbookmodel.delete(13, '1234')
test_guestbookmodel_delete()

