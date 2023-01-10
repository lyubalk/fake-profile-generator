"""Программа для создания фэйковых профилей. По запросу от пользователя есть ли
образование и какой желателен пол, создаются данные: имя, фамилия, город проживания,
город обучения (если есть образование), год рождения, логин и пароль."""
# from random import choices
from transliterate import translit
import random
import string
import secrets

woman_name = random.choice(open('woman_name.txt').readlines())  # случайный выбор женского имени из файла
man_name = random.choice(open('man_name.txt').readlines())  # случайный выбор мужского имени из файла
woman_surname = random.choice(open('woman_surname.txt').readlines())  # случайный выбор женской фамилии из файла
man_surname = random.choice(open('man_surname.txt').readlines())  # мужские фамилии
city = random.choice(open('city.txt').readlines())  # город проживания и обучения
mail = random.choice(open('city.txt').readlines())  # почтовые сервисы
education = input('Есть образование (введите Y если да, N если нет) >>> ').lower()
gender = input('Введите пол W если женский, M если мужской >>> ').lower()


def fake_profile():
    if gender == 'w':
        my_name = woman_name  # случайный выбор имени
        my_surname = woman_surname
        age = random.randrange(1990, 2005)  # дата рождения
        my_login = my_name + '.' + my_surname  # составление имени и фамилии для создания логина
        my_login_eng = translit(my_login, language_code='ru', reversed=True)  # перевод на английский
        my_login_eng_1 = "".join(my_login_eng) + '.' + "".join(str(age)) + "".join(
            mail)  # создание логина с датой
        # рождения и почтовым сервисом
        print(f'Имя и фамилия: {"".join(my_login)}, \nГод рождения: {age}, \nЛогин: {"".join(my_login_eng_1)}')  #
        # вывод данных
    elif gender == 'm':  # все тоже самое но для мужчин
        my_man_name = man_name
        my_surname_1 = man_surname
        age = random.randrange(1990, 2005)
        my_login_men = my_man_name + '.' + "".join(my_surname_1)
        my_login_men_eng = translit(my_login_men, language_code='ru', reversed=True)
        my_login_men_eng_1 = "".join(my_login_men_eng) + '.' + "".join(str(age)) + "".join(mail)
        print(f'Имя и фамилия: {"".join(my_login_men)}, \nГод рождения: {age}, \nЛогин:{"".join(my_login_men_eng_1)}')
    if education == 'y':  # обработка запроса по образованию
        my_city_education = city
        print(f'Город образования: {"".join(my_city_education)}')
    else:
        print('нет образование')

    my_city = city
    alphabet = string.printable
    password = ''.join(secrets.choice(alphabet) for i in range(8))
    return f'Город проживания: {"".join(my_city)}, \nПароль: {password}'


print(fake_profile())
