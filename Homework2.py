lines = input().split() #делим строку на подстроки

def func_1(word):       #берем отдельно подстроку, считаем, где букв больше 
    upper = 0           # кол-во загл. букв. 
    lower = 0           # кол-во строч.б.
    for sym in word:    # в каждой подстоке проходимся по каждому символу 
        if sym.isupper():   #ф-ция проверяет, заглавная буква или нет
            upper += 1
        else:
            lower += 1
    return upper > lower 

def func_2(words):          #считаем кол-во подстрок с заглавными буквами в строке
    num = 0
    for word in words:         #для подстроки в строке
        if func_1(word):
            num += 1          #len(words) - кол-во всех подстрок 

    print(f'{num/len(words) * 100}%')

func_2(lines)