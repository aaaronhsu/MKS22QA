# classwork
def isLeapYear(year):
    if year % 400 == 0:
        print("leap year")
        return True
    elif year % 4 == 0 and (year % 100) != 0:
        print("leap year")
        return True
    else:
        print("not leap year")
        return False

# challenge
def daysInMonth(month, year):
    if month == 2 and isLeapYear(year):
        print(29)
    elif month == 2:
        print(28)
    else:
        if month > 7:
            if month % 2 == 0:
                print(31)
            else:
                print(30)
        else:
            if month % 2 == 0:
                print(30)
            else:
                print(31)

isLeapYear(2104)
