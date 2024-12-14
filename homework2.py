# Задание №1
''' Программа выведет True, мы использовали and
 и она выведет False даже если одно
  из двух условий окажется неверным
 и x, и y, больше 5, но меньше 25, потому программа выведет True '''
#Задание №2
password = input()
repit_password = input()
if password == repit_password:
    print(True)
else:
    print(False)
# Задача №3 Ответ = 5
number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
number_4 = int(input())
if number_1 < number_2:
    num_1_2 = number_1
else:
    num_1_2 = number_2
if number_3 < number_4:
    num_3_4 = number_3
else:
    num_3_4 = number_4
if num_1_2 < num_3_4:
    print(num_1_2)
else:
    print(num_3_4)
#Задача №4 Ответ = 5
number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
number_4 = int(input())
if number_1 > number_2:
    num_1_2 = number_1
else:
    num_1_2 = number_2
if number_3 > number_4:
    num_3_4 = number_3
else:
    num_3_4 = number_4
if num_1_2 > num_3_4:
    print(num_1_2)
else:
    print(num_3_4)
# Задача №5 Ответ = 30
a = int(input())
b = int(input())
c = int(input())
if a <= b + c and b <= a + c and c <= a + b:
    print(True)
else:
    print(False)
# Задача №6 Ответ = Вырожденный
a = int(input())
b = int(input())
c = int(input())
abc = a + b > c and b + c > a and a + c > b
if a != b and b != c and c != a and abc:
    print('Разносторонний')
elif a == b and b == c:
    print('Равносторонний')
elif abc == 0:
    print('Вырожденный')
# Задача №7 Ответ = 7
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if b < c or d < a:
    print(0)
elif a <= c and d <= b:
    print(d - c + 1)
elif c <= a and b <= d:
    print(b - a + 1)
elif c >= a and b >= c and d >= b:
    print(b - c + 1)
elif a >= c and d >= a and b >= d:
    print(d - a + 1)