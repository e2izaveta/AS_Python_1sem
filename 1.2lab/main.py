# 1. Вывести число K N раз
def task1():
    K = int(input("K = "))
    N = int(input("N = "))
    for _ in range(N):
        print(K)

# 2. Числа от A до B включительно в порядке возрастания
def task2():
    A = int(input("A = "))
    B = int(input("B = "))
    count = 0
    for i in range(A, B + 1):
        print(i)
        count += 1
    print(f"N = {count}")

# 3. Числа между A и B в порядке убывания (исключая A и B)
def task3():
    A = int(input("A = "))
    B = int(input("B = "))
    count = 0
    for i in range(B - 1, A, -1):
        print(i)
        count += 1
    print(f"N = {count}")

# 4. Таблица стоимости товара
def task4():
    price = 20.4
    print("Кол-во | Стоимость")
    print("------------------")
    for i in range(1, 11):
        cost = i * price
        print(f"{i:6} | {cost:9.2f}")

# 5. Квадраты чисел от A до B с шагом H
def task5():
    A = int(input("A = "))
    B = int(input("B = "))
    H = int(input("H = "))
    for i in range(A, B + 1, H):
        print(f"{i}^2 = {i**2}")

# 6. Положительные числа от A до B с шагом H
def task6():
    A = int(input("A = "))
    B = int(input("B = "))
    H = int(input("H = "))
    for i in range(A, B + 1, H):
        if i > 0:
            print(i)

# 7. Сумма чисел от A до B
def task7():
    A = int(input("A = "))
    B = int(input("B = "))
    total = 0
    for i in range(A, B + 1):
        total += i
    print(f"Сумма = {total}")

# 8. Произведение чисел от A до B
def task8():
    A = int(input("A = "))
    B = int(input("B = "))
    product = 1
    for i in range(A, B + 1):
        product *= i
    print(f"Произведение = {product}")

# 9. Сумма квадратов чисел от A до B
def task9():
    A = int(input("A = "))
    B = int(input("B = "))
    total = 0
    for i in range(A, B + 1):
        total += i**2
    print(f"Сумма квадратов = {total}")

# 10. Стоимость конфет от 1.2 до 2 кг
def task10():
    price = float(input("Цена за 1 кг: "))
    weight = 1.2
    print("Вес (кг) | Стоимость")
    print("-------------------")
    while weight <= 2.01:  # 2.01 для учета погрешности
        cost = weight * price
        print(f"{weight:8.1f} | {cost:9.2f}")
        weight += 0.2

# 11. Квадрат числа как сумма нечетных чисел
def task11():
    N = int(input("N = "))
    square = 0
    for i in range(1, 2*N, 2):
        square += i
    print(f"{N}^2 = {square}")

# 12. Степени числа A от 1 до N
def task12():
    A = float(input("A = "))
    N = int(input("N = "))
    for i in range(1, N + 1):
        print(f"{A}^{i} = {A**i}")

# 13. Наибольшее K, где K² ≤ N
def task13():
    N = int(input("N = "))
    K = 0
    while (K + 1)**2 <= N:
        K += 1
    print(f"K = {K}")

# 14. Наибольшее K, где 3^K < N
def task14():
    N = int(input("N = "))
    K = 0
    power = 1
    while power * 3 < N:
        power *= 3
        K += 1
    print(f"K = {K}")

# 15. Разбиение отрезка [A, B] на N равных частей
def task15():
    A = float(input("A = "))
    B = float(input("B = "))
    N = int(input("N = "))
    
    H = (B - A) / N
    print(f"H = {H:.6f}")
    
    print("Точки разбиения:")
    for i in range(N + 1):
        point = A + i * H
        print(f"{point:.6f}")

# Демонстрация всех задач
def main():
    tasks = {
        1: task1, 2: task2, 3: task3, 4: task4, 5: task5,
        6: task6, 7: task7, 8: task8, 9: task9, 10: task10,
        11: task11, 12: task12, 13: task13, 14: task14, 15: task15
    }
    
    print("Выберите задачу (1-15):")
    choice = int(input())
    
    if choice in tasks:
        print(f"\n=== ЗАДАЧА {choice} ===")
        tasks[choice]()
    else:
        print("Неверный выбор")

if name == "__main__":
    main()
