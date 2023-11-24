import datetime as dt

total = 0
cum_days = [total := total + i for i in (0,31,28,31,30,31,30,31,30,31,30,31,30,31)]
            
userinput = input("Enter your date of birth: (DD/MM/YY):")

day, month, _ = [int(x) for x in userinput.split('/')]

now = dt.datetime.now()

days_now = now.day + cum_days[now.month]
days_birthday = day +cum_days[month]
days_to_go = (days_birthday - days_now) % 365

print(f"You have {days_to_go} until your birthday")