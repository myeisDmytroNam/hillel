# Задача 1
# Напишіть программу "Касир в кінотеватрі", яка попросить користувача ввести свій вік
# (можна використати константу або функцію input(), на екран має бути виведено лише одне повідомлення).
# якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
# якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# якщо від 16 до 65 то зробіть якесь вітальне повідомлення, на ваш розсуд.
# якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"

age = int(input("Enter your age: "))
if age < 7:
    print("Де твої батьки?")
elif age < 16:
    print("Це фільм для дорослих!")
elif age <= 65:
    print("Заходь")
else:
    print("Покажіть пенсійне посвідчення!")




# Задача 2
# Текстова в чому різниця між is та ==?
# Наскільки я зрозумів з лекції, == це перевірка на рівність, в той час як is це перевірка на сутність.
# Тобто == повернить True or False, а is перевірить чи збігаються комірки в пам'ті


#
# Задача 3
# Напишіть програму яка в користувача запитує два числа(можуть бути числа типу інт, а можуть бути в стр).
# Потім запитує це стр чи інт і в залежності від відповіді конкатенує їх або додає і повертає результат перемножений на три.
# якщо після конкатенації отримали 10 то перемноживши на 3 отримаємо 30.

num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")

number_types = input("Select INT or STR: ")
number_types = number_types.upper() # Этого требования нет, но в теории пользователь может проигнорировать то как именно мы просим ввести его значение. Проверка на дурака.
if number_types == "INT":
    answer = (int(num_1) + int(num_2))*3
else:
    answer = num_1 + num_2
    answer = int(answer)*3
print(answer)


# 1) Так як я у відео міняв значення за допомогою віднімання та додавання,
# зробіть це ж саме за допомогою множення. Там дуже простий алгоритм вирішення.
# Спробуйте в ньому розібратись


a = 3
b = 4
print(a, b)

a = a * b
b = a // b
a = a // b

print(a, b)


# 2) Напишіть програму яка буде приймати квадратне рівняння і розвязувати його.
# Памятайте що там є декілька випадків по іксам. Завдання не складне але обьємне.
# Подумайте як прийняти дані від користувача, ну і над рештою).

# # x**2-3x-4=0
#   1   -3 -4
# d = "5*x"
# c = d - "x"
#
# print(c)

#
equation = input("Enter the equation: ")
a = int(input("Enter root 1: "))  # 1
b = int(input("Enter root 2: "))  # -3
c = float(input("Enter root 3: "))  # -4
#
d = b**2-4*a*c
if d > 0:
    d_1 = ((-b + (b ** 2 - 4 * a * c) ** (1 / 2)) // 2 * a)
    d_2 = ((-b - (b ** 2 - 4 * a * c) ** (1 / 2)) // 2 * a)
    print(d_1, d_2)
elif d == 0:
    d_1 = ((-b + (b ** 2 - 4 * a * c) ** (1 / 2)) // 2 * a)
    d_2 = d_1  # напевно зайвий код
    print(d_2)
else:
    print("Коренів немає")

# # d_1 = 3 + (9 + 16)**(1/2)