from django.test import TestCase

import user.models as usermodels


# def test_usermodels_insert():
#     usermodels.insert('마이콜', 'michol@gmail.com', '1234', 'male')
#
#
# def test_usermodels_fetchone():
#     result = usermodels.fetchone('michol@gmail.com', '1234')
#     print(result)
#
#
# def test_usermodels_update():
#     result = usermodels.update('감자깡', '4567@gmail.com', '1234', 'male')


# test_usermodels_insert()
# test_usermodels_fetchone()
# test_usermodels_update()


def test_usermodels_update():
    result = usermodels.update('감자깡2', 'ggang2@gmail.com', '1234', 'male', 9)
test_usermodels_update()