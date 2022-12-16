# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11
from decimal import Decimal

def check(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

def number(N,summ = 0):
    if N != 0 :
        if check(N) == True:
            if Decimal(str(N))%1 > 0:
                while float(N) % 1 != 0:
                    N = float(Decimal(str(N))* 10)
            summ = int(N)%10
            return int(summ) + number(int(Decimal((str(N))))//10)
        else:
            print('Некорректный ввод, введите вещественное число: ')
            N = input()
            return number(N,summ = 0)
    return int(summ)


message = (input("Введите число: "))
print(f'Сумма цифр = {number(message)}')


