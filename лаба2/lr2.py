#Кол-во рус букв
# def count_russian_letters(s):
#     russian_letters = 0  # Переменная для подсчета русских букв
#     for char in s:
#         # Проверяем, является ли символ русской буквой
#         if ('а' <= char <= 'я') or ('А' <= char <= 'Я'):
#             russian_letters += 1  # Увеличиваем счетчик, если символ русская буква
#     return russian_letters
#
# text = input("Введите строку: ")
# result = count_russian_letters(text)
# print(f"Количество русских букв: {result}")


#Образуют ли лат буквы полиндром
# def is_latin_palindrome(s):
#     # Создаем пустую строку для хранения только строчных латинских букв
#     only_latin = ""
#
#     # Проходим по каждому символу в строке
#     for char in s:
#         # Если символ является строчной латинской буквой, добавляем его в нашу строку
#         if 'a' <= char <= 'z':
#             only_latin += char
#
#     # Теперь проверяем, является ли строка палиндромом
#     # Сравниваем строку с её перевернутой версией
#     if only_latin == only_latin[::-1]:
#         return True  # Если палиндром, возвращаем True
#     else:
#         return False  # Если не палиндром, возвращаем False
#
#
# text = input("Введите строку: ")
# if is_latin_palindrome(text):
#     print("Строчные латинские буквы образуют палиндром.")
# else:
#     print("Строчные латинские буквы не образуют палиндром.")


#Поиск даты в тексте
def find_dates(text):
    # Список месяцев на русском языке
    months = ["января", "февраля", "марта", "апреля", "мая", "июня",
              "июля", "августа", "сентября", "октября", "ноября", "декабря"]

    # Разбиваем текст на отдельные слова
    words = text.split()

    dates = []

    # Проходим по каждому слову в тексте
#     for i in range(len(words) - 2):
#         # Проверяем, является ли текущее слово числом от 1 до 31 (день)
#         if words[i].isdigit() and 1 <= int(words[i]) <= 31:
#             # Проверяем, является ли следующее слово месяцем
#             if words[i + 1] in months:
#                 # Проверяем, состоит ли третье слово из 4 цифр (год)
#                 if words[i + 2].isdigit() and len(words[i + 2]) == 4:
#                     # Если все проверки пройдены, добавляем найденную дату
#                     dates.append(f"{words[i]} {words[i + 1]} {words[i + 2]}")
#
#     return dates
#
# text = input("Введите текст: ")
# found_dates = find_dates(text)
#
# if found_dates:
#     print("Найденные даты:")
#     for date in found_dates:
#         print(date)
# else:
#     print("Даты не найдены.")
