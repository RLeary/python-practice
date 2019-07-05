from datetime import date

now = date.today()
print(now)

print(now.strftime("%m-%d-%y"))
print(now.strftime("%d %b %Y"))
print(now.strftime("%A the %d of %B, %Y"))

birthday = date(1995, 6, 13)
age = now - birthday
print(age.days)
