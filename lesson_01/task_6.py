result = int(input("В первый день результат составил: "))
day = 1
objective = int(input("Цель пробежать: "))
print(f"{day}-й день: {result:.2f}")
while result < objective:
    result = result + result*0.1
    day += 1
    print(f"{day}-й день: {result:.2f}")
print(f"на {day}-й день спортсмен достиг результата — не менее {objective} км.")