money_capital = 10000
salary = 5000
spend = 6000
increase = 1.05 # удобнее с 1.05

month = 0

while money_capital >= spend:
# while money_capital >= spend - salary -> ответ 5
    money_capital -= spend
    money_capital += salary
    spend *= increase
    month += 1

print(month)
