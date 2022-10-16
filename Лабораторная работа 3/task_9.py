salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 1.03  # рост цен, удобнее с 1.03

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for _ in range(months):
    delta = spend - salary
    need_money += delta
    spend *= increase

print(round(need_money))