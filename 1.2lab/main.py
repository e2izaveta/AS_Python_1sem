# 1. Вывести K N раз
K, N = 5, 3
print("1.", *[K for _ in range(N)])

# 2. Числа от A до B включительно
A, B = 2, 5
numbers = list(range(A, B + 1))
print("2.", *numbers, f"Количество: {len(numbers)}")

# 3. Числа между A и B в порядке убывания
A, B = 2, 7
numbers = list(range(B - 1, A, -1))
print("3.", *numbers, f"Количество: {len(numbers)}")

# 4. Таблица стоимости
price = 20.4
print("4.")
for i in range(1, 11):
    print(f"   {i} шт: {i * price:.1f} руб")

# 5. Квадраты чисел с шагом H
A, B, H = 1, 10, 2
print("5.")
for i in range(A, B + 1, H):
    print(f"   {i}² = {i**2}")

# 6. Положительные числа с шагом H
A, B, H = -3, 8, 2
print("6.", *[i for i in range(A, B + 1, H) if i > 0])

# 7. Сумма чисел от A до B
A, B = 1, 5
total = sum(range(A, B + 1))
print("7.", total)

# 8. Произведение чисел от A до B
A, B = 1, 4
product = 1
for i in range(A, B + 1):
    product *= i
print("8.", product)

# 9. Сумма квадратов
A, B = 1, 3
total = sum(i**2 for i in range(A, B + 1))
print("9.", total)

# 10. Стоимость конфет
price = 150
print("10.")
weight = 1.2
while weight <= 2:
    print(f"   {weight} кг: {weight * price:.1f} руб")
    weight += 0.2

# 11. Квадрат как сумма нечетных
N = 4
square = sum(range(1, 2*N, 2))
print("11.", f"{N}² = {square}")

# 12. Степени числа A
A, N = 2, 5
print("12.", *[f"{A}^{i}={A**i}" for i in range(1, N + 1)])

# 13. Наибольшее K: K² ≤ N
N = 17
K = 0
while (K + 1)**2 <= N:
    K += 1
print("13.", K)

# 14. Наибольшее K: 3^K < N
N = 100
K, power = 0, 1
while power * 3 < N:
    power *= 3
    K += 1
print("14.", K)

# 15. Разбиение отрезка
A, B, N = 0, 10, 5
H = (B - A) / N
points = [A + i * H for i in range(N + 1)]
print("15.", f"H = {H}", *points)
