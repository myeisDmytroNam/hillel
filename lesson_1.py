#1 Арифметичні операції:
# Написати програму, яка зчитує два числа та виводить їхню суму, різницю, добуток та частку.
Num1 = 8
Num2 = 4

print(Num1+Num2)
print(Num1-Num2)
print(Num1*Num2)
print(type(Num1//Num2), Num1/Num2)
print(type(Num1/Num2), Num1//Num2)
# Решил использовать как / так и //


# 2 Залишок від ділення:
# Користувач вводить два числа. Вивести залишок від ділення першого числа на друге.

Num1 = int(input("Введіть перше число: "))
Num2 = int(input("Введіть друге число: "))

result = Num1/Num2
print(result)

# 3 Цілочисельне ділення:
# Користувач вводить два числа. Вивести, скільки разів перше число ділиться на друге без залишку.

Num1 = int(input("Введіть перше число: "))
Num2 = int(input("Введіть друге число: "))

result = Num1//Num2
print(result)
