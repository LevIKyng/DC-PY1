money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
difference = salary - spend

while money_capital + difference >= spend:
    spend += spend * increase
    money_capital += difference
    month += 1

print(month)
