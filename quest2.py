# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def check(N = input('Введите целое число: ')):  ## функция проверки ввода
    try:
        int(N)
        return N
    except ValueError:
        print("Некорректный ввод, введите целое число: ")
        N = input('')
        return check(N)

n = int(check()) 

def muliply(n): ## функция расчета произведений
        if n == 1:
            return 1
        return  n * muliply(int(n)-1)
    
        
list = []
for i in range(1, n+1):   ## вывод перемножений
    list.append(muliply(i))
print(list)

