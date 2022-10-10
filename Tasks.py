#Task-1
# Вывести високосные года:
# def is_leap_year(x):
#     return ((x % 4 == 0) and (x % 100 != 0)) or (x % 400 == 0)




#Task-2
# У вас есть заготовка функции — def get_wind_class(speed):
# Вам нужно вместо "???" написать цикл, который возвращает из функции класс ветра в зависимости от его характера:
# от 1 до 4 м/с - "weak [1]"
# от 5-10 м/c - "moderate [2]"
# от 11-18 м/c - "strong [3]"
# от 19 м/c - "hurricane [4]"
# В последней строке мы просим программу напечатать результат (в зависимости от цифры в скобках) —
# def get_wind_class(speed):  # Объявление функции
#     if speed in [1, 2, 3, 4]:
#         return "weak [1]"
#     elif speed in range(5, 11):
#         return "moderate [2]"
#     elif speed in range(11, 19):
#         return "strong [3]"
#     elif speed >= 19:
#         return "hurricane [4]"
# print(get_wind_class(21))  # Печатаем результат выполнения
#
# # Второй вариант решения:
# def get_wind_class(speed): #объявление функции
#     if 1 <= speed <= 4: #только аргумент
#         return "weak [1]"
#     elif 5 <= speed <= 10:
#         return "moderate [2]"
#     elif 11 <= speed <= 18:
#         return"strong [3]"
#     elif speed >= 19:
#         return "hurricane [4]"
# print(get_wind_class(3)) #мы просим программу напечатать то, что в скобках




# Task-3

# Допишите функцию check_user так, чтобы она по логину пользователя
# проверяла, существует он или нет,
# после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Чтобы вернуть True, напишите "return True";
# чтобы вернуть False, напишите "return False".

# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
#
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False



#  Task-4
# Запишите логическое выражение, которое определяет,
# что число А не принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.

# A = int(input('Вdеди число \n'))

# if not (-10 <= A <= -1 or 2 <= A <= 15):
#     print('True')
# else:
#     print('False')


# Дано двузначное число. Определите, входит ли в него цифра 5.
# Попробуйте решить задачу с использованием
# целочисленного деления и деления с остатком.
#
# n = 15
# first_digit = n // 10
# second_digit = n % 10
#
# print((first_digit == 5) or (second_digit == 5))


#
# # Проверьте, все ли элементы в списке являются уникальными.
#
# a = (input('numbers:'))
# unique = list(set(a))
# print(unique)




# Дано натуральное восьмизначное число.
# Выясните, является ли оно палиндромом
# (читается одинаково слева направо и справа налево).list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# print(len(list_) == len(set(list_)))

# num = int(input('Введи восьмизначное число: '))
# str_num = str(num)
# print(str_num)
#
# print(str(str_num) == str(str_num)[::-1])





