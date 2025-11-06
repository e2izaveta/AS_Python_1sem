# 15. Сумма ряда x - x³/3 + x⁵/5 - ... + (-1)ⁿx²ⁿ⁺¹/(2n+1)
n = 5
x = 0.5

total = 0
for k in range(n + 1):
    total += (-1)**k * x**(2*k + 1) / (2*k + 1)

print(total)
