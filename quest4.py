# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.
import random

def check(N):  ## функция проверки ввода
    try:
        int(N)
        return N
    except ValueError:
        print("Некорректный ввод, введите целое число: ")
        N = input('')
        return check(N)

n = int(check(input('Введите кол-во элементов списка: ')))

list = [n for n in range(-n, n+1)] ## генерируем список
print(f'изначальная последовательность: {list}')
random.shuffle(list)
print(f'Перемешанная последовательность: {list}')

F = open('file.txt','w')  ## создаем рандомные позиции в файле
for i in range(1,random.randint(0,n*2+1)):
    F.write(str(random.randint(0,n*2))+'\n')
F.close
F = open('file.txt','r')
line = F.read().splitlines()
F.close




def multiply(arrayofpos,arrayofnumbers): ## функция перемножения элементов 
    result = 1
    for i in arrayofpos:
        result = result * arrayofnumbers[int(i)]
    return result
print(f'Произведение элементов перемешанной последовательности на позициях = {multiply(line,list)}')

    
    

    

