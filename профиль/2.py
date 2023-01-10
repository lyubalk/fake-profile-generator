"""Программа для создания фэйковых профилей. По запросу от пользователя есть ли
образование и какой желателен пол, создаются данные: имя, фамилия, город проживания,
город обучения (если есть образование), год рождения, логин и пароль."""
from transliterate import translit  # модуль для перевода на другой (английский) язык
import random  # модуль случайного выбора
import string  # строковый модуль
import secrets  # модуль для генерации криптографически стойких случайных чисел

education = input('Есть образование (введите Y или Д если да, N или Н если нет) >>> ').lower()  # запрос у
# пользователя по наличию образования
gender = input('Введите пол W или Ж если женский, M если мужской >>> ').lower()  # запрос у пользователя по желанию пола


def read_file(file_name):  # функция для чтения файлов
    with open(file_name, 'r') as f:  # открытие файла в режиме чтения
        lines = f.readlines()  # чтение файла по строчно
        return random.choice(lines).replace('\n', '')  # Случайный выбор строки из файла с заменой символа новой
        # строки на пробел


def fake_profile():  # основная функция
    age = random.randrange(1990, 2005)  # Генерация даты рождения
    alphabet = string.digits + string.ascii_letters + string.punctuation  # Создания алфавита для пароля
    password = ''.join(secrets.choice(alphabet) for _ in range(8))  # Генерация пароля из 8 символов

    my_mail = read_file('mail.txt')  # файл с почтовыми сервисами
    city = read_file('city.txt')  # Файл городов

    if gender == 'w' or 'ж':  # Выбор женского пола
        name = read_file('woman_name.txt')  # Файл женских имен
        surname = read_file('woman_surname.txt')  # Файл женских фамилий

    else:  # Выбор мужского пола
        name = read_file('man_name.txt')  # Файл с мужскими именами
        surname = read_file('man_surname.txt')  # Файл мужских фамилий

    my_login = translit(name + '.' + surname, language_code='ru', reversed=True)  # Перевод имени и фамилии на
    # английский
    my_login_eng = my_login + '.' + str(age) + my_mail  # Сбор логина (имя.фамилия.год рождения почтовый сервис)

    print(
        f'Имя и фамилия: {name} {surname} '
        f'\nГод рождения: {age} '
        f'\nЛогин:{my_login_eng}'
        f'\nГород проживания: {city} '
        f'\nПароль: {password}'
    )  # Вывод всех данных

    if education == 'y' or 'д':  # Выбор наличия образования (да)
        education_city = read_file('city.txt')  # Выбор города образования
        print(f'Город образования: {education_city}')
    else:
        print('нет образование')  # Выбор образования (нет)


fake_profile()
