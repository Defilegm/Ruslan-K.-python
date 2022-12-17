# Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.

# Пример:

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}


def check(n):
    try:
        int(n)
        return n
    except ValueError:
        n = input('Некорректный ввод, введите целое число: ')
        return check(n)
    
N = check(input(' Введите кол-во чисел в последовательности: '))

dict = {i+1: round((1+ 1/(i+1))**(i+1),2) for i in range(int(N))}
print(dict)
  
