summa = 20000
r = 12/100/12
month = 36


pay = summa * r * pow((1 + r), month) / (pow((1 + r), month) - 1)
print(pay)
print(pay * month)

