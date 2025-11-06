# 15. Сумма ряда x - x³/3 + x⁵/5 - ... + (-1)ⁿx²ⁿ⁺¹/(2n+1)
def task15():
    n = int(input("n = "))
    x = float(input("x = "))
    if abs(x) >= 1:
        print("Ошибка: |x| должен быть < 1")
        return
    
    total = 0
    for i in range(n + 1):
        exponent = 2 * i + 1
        sign = 1 if i % 2 == 0 else -1
        term = sign * (x ** exponent) / exponent
        total += term
        print(f"{'+' if sign > 0 else '-'}{x}^{exponent}/{exponent} = {term:.6f}")
    print(f"Сумма = {total:.6f}")

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
