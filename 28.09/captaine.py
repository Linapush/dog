# Запись в файл осуществляется с помощью метода write
# Метод write возвращает число записанных символов
# После окончания работы с файлом его обязательно нужно закрыть с помощью метода close

from datetime import date, timedelta

def captain(date, phrases):

    the_next_date = timedelta(days = 1)
    
    captain = open("text.txt", "w")  
    for phrase in phrases:
        result = (str(date) + phrase + '\n')
        captain.write(result)
        date = date + the_next_date
    captain.close()

captain(date(2022, 10, 30), ['Скоро обед', 'Зачет через 9 дней', 'Как переписать самостоятельную?'])
       


# def printScores(student, *scores):
#    print(f"Student Name: {student}")
#    for score in scores:
#       print(score)
# printScores("Jonathan",100, 95, 88, 92, 99)
  
#str(date, phraise) 
# print("Date:", phrase)]
# for phraise, num in date:
# print('%s: %d' % (phraise, num)) 
    