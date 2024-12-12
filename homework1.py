#Задание №1 
x = input()
y = input()
w = input()
print(x + y + w, end='!')
# Задание №2 Ответ 32134205104895.5
a = int(input())
b = int(input())
print(2 ** 8 * a ** 8 - 2 ** 4 * a ** 4 + 2 ** 2 * a ** 2 - 2 * b + 0.5 * b ** 0.5 + (a * b) ** (b + a) / 2)
#Задание №3 Ответ 23! input принимает строки, а не числа
a = input()
b = input()
print(a + b, end = "!")
# Задание №4 Ответ ( a + b - c) % 10 = результат данного выражения
a = int(input())
b = int(input())
c = int(input())
print('(', end='')  # выводит '(' и убирает пробел
print(a, b, sep='+', end='-')  # выводит значения a и b, ставит меж ними + вместо пробела, а после них -
print(c, ') % 10', sep='', end=' = ')  # выводит значение 'c' и строку ") % 10", убирает пробелы, добавляет в конце знак print((a + b - c) % 10) # выводит результат выражения которое вы вывели в консоль
# Задание №5 Ответ 23 и 25
this_number = int(input())
last_number = this_number - 1
next_number = this_number + 1
print(f'f/ Предыдущее число: {last_number}, Следующее число: {next_number}')
# Задание №6
sm_value = int(input())
print(sm_value * 0.00001)