# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

number = int(input("Введите трехзначное число: "))
digit1 = number//100
digit2 = (number//10)%10
digit3 = number%10
total = digit1 + digit2 + digit3
print(f"Сумма цифр {total}")