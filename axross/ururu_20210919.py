year = int(input("Year: "))
month = int(input("Month: "))

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def month_days(year, month):
    month_with_30days = [4, 6, 9, 11]
    days = 31
    if month == 2:
        if leap_year(year):
            days = 29
        else:
            days = 28
    elif month in month_with_30days:
        days = 30
    return days

def total_days(year, month):
    total = 0
    for i in range(1900, year):
        if leap_year(i):
            total += 366
        else:
            total += 365
    for j in range(1, month):
        total += month_days(year, j)
    return total

print("Sun\tMon\tTue\tWed\tThu\tFri\tSat")
week_day = total_days(year, month) % 7 +1
for i in range(week_day % 7):
    print('\t', end='')
for j in range(1, month_days(year, month) + 1):
    print(j, '\t', end=''),
    week_day += 1
    if week_day % 7 == 0:
        print('')

# 問1の回答
# x = total_days(year, month)
# print(x)

# 問2の回答
# week_day = total_days(year, month) % 7 +1
# print(week_day)