from django.test import TestCase

import user.models as usermodels


def test_usermodels_insert():
    usermodels.insert('마이콜', 'michol@gmail.com', '1234', 'male')


def test_usermodels_fetchone():
    result = usermodels.fetchone('michol@gmail.com', '1234')
    print(result)


# def test_usermodels_update():
#     result = usermodels.update('4', '1234', '4567@gmail.com', '1234')

# test_usermodels_insert()
test_usermodels_fetchone()
# test_usermodels_update()