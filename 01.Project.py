prompt = ("Enter number of days: ")

days = input(prompt)

years = (int(days)//365)
weeks = (int(years)//52)
days = (int(weeks // 7))

print(years)
print(weeks)
print(days)