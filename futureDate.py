todaysDate = int(input("Enter today's day: "))
daysElapsed = int(input("Enter the number of days elapsed since today:"))

if todaysDate == 0:
    print("Today is Sunday")
elif todaysDate == 1:
    print("Today is Monday")
elif todaysDate == 2:
    print("Today is Tuesday")
elif todaysDate == 3:
    print("Today is Wednesday")
elif todaysDate == 4:
    print("Today is Thursday")
elif todaysDate == 5:
    print("Today is Friday")
elif todaysDate == 6:
    print("Today is Saturday")


def future(day):
    if day == 0:
        print("future is Sunday")
    elif day == 1:
        print("future is Monday")
    elif day == 2:
        print("future is Tuesday")
    elif day == 3:
        print("future is Wednesday")
    elif day == 4:
        print("future is Thursday")
    elif day == 5:
        print("future is Friday")
    elif day == 6:
        print("future is Saturday")
future((daysElapsed+todaysDate) % 7)

