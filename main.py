import datetime as dt

userinput = input("Enter your date of birth: (DD/MM/YY):")
# problem 1 - we need to santize the input

day, month, year = userinput.split("/")

yrborn = int(year)
mtborn = int(month)
dyborn = int(day)

yrnow = dt.datetime.now().year
mtnow = dt.datetime.now().month
dynow = dt.datetime.now().day

now = dt.datetime.now()
yrnow , mtnow, dynow - now.year, year.month, now.day

hashadbirthday = (mtnow > mtborn) or (mtnow == mtborn and dynow >= dyborn)

age = yrnow - yrborn - (not hashadbirthday)

# if hashadbirthday;
#        age = yrnow - yrborn
#else:
#        age = yrnow - yrborn - 1

#day = int(userinput[0:2])
#month = int(userinput[3:5])
#year = int(userinput[6:])
#print(f"day: {day}, month {month}, year: {year}")

print(f"You are {yrnow-yrborn} years old.")