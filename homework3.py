# Задание №1
# x = int(input())
# while (x % 2 != 0) and (x % 10 != 5):
#     x = int(input())
# Задание №2
# for i in range(10):
#     print(i)
# Задание №3
# k = int(input())
# n = int(input())
# summa = 0
# while k <= n:
#     if k % 2 != 0:
#         summa += k
#     k += 1
# print(summa)
# Задание №4
N = int(input())
factorial = 1
if N > 0:
    for i in range(1, N + 1):
        factorial = factorial * i
    print(factorial)
