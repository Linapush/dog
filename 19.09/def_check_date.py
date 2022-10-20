
def check_date(day: int, month: int, year: int):
    month_31days = [1, 3, 5, 7, 8, 10, 12]
    month_30days = [4, 6, 9, 11]
    true_year1 = day in range(1, 31) and month in month_31days
    true_year2 =  day in range (1, 30) and month in month_30days
    leap_year = (year % 100 != 0 and year % 4 == 0) or year % 400 == 0
    # negative_date = datetime.datetime - datetime.timedelta(days = float(inf))  
    leap_date = month == 2 and day in range(1, 29) and leap_year
    february = month == 2 and not(leap_year) and day in range(1, 28)
    result = true_year1 or true_year2 or february or leap_date
    return result

print(check_date(29,2,1600))    

#     if true_year1 or true_year2 or february or leap_date:
#         return True
#     elif leap_year:
#         return False
#     else:
#         return False


