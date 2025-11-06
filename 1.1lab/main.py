# Задание 4 из ЕГЭ-2025 профиль [https://math-ege.sdamgia.ru/test?id=86355920]
# Игральный кубик бросают дважды. Сколько элементарных исходов опыта благоприятствуют событию «А  =  сумма очков равна 5»?
def count_favorable_outcomes(target_sum):
    """
    Подсчет количества элементарных исходов, когда сумма очков на двух кубиках равна target_sum
    
    Args:
        target_sum: целевая сумма очков
    
    Returns:
        count: количество благоприятных исходов
        outcomes: список благоприятных исходов в виде кортежей (первый бросок, второй бросок)
    """
    count = 0
    outcomes = []
    
    # Перебираем все возможные результаты первого броска (от 1 до 6)
    for first_roll in range(1, 7):
        # Перебираем все возможные результаты второго броска (от 1 до 6)
        for second_roll in range(1, 7):
            # Проверяем, равна ли сумма целевому значению
            if first_roll + second_roll == target_sum:
                count += 1
                outcomes.append((first_roll, second_roll))
    
    return count, outcomes

def analyze_probability_space():
    """
    Анализ всего пространства элементарных исходов
    """
    print("=== АНАЛИЗ ВСЕГО ПРОСТРАНСТВА ИСХОДОВ ===")
    total_outcomes = 0
    sum_distribution = {}
    
    # Анализируем все возможные исходы
    for i in range(1, 7):
        for j in range(1, 7):
            total_outcomes += 1
            current_sum = i + j
            if current_sum not in sum_distribution:
                sum_distribution[current_sum] = []
            sum_distribution[current_sum].append((i, j))
    
    print(f"Общее количество элементарных исходов: {total_outcomes}")
    print("\nРаспределение сумм:")
    for sum_value in sorted(sum_distribution.keys()):
        count = len(sum_distribution[sum_value])
        print(f"Сумма {sum_value}: {count} исходов - {sum_distribution[sum_value]}")
    
    return total_outcomes, sum_distribution

def main():
    target_sum = 5
    
    print("=== РАСЧЕТ БЛАГОПРИЯТНЫХ ИСХОДОВ ДЛЯ СУММЫ 5 ===")
    print("Условие: игральный кубик бросают дважды")
    print("Событие A: сумма очков равна 5")
    print()
    
    # Подсчитываем благоприятные исходы
    count, outcomes = count_favorable_outcomes(target_sum)
    
    # Выводим результаты
    print(f"Благоприятные исходы (сумма = {target_sum}):")
    for i, outcome in enumerate(outcomes, 1):
        print(f"  {i}. ({outcome[0]}, {outcome[1]}) - {outcome[0]} + {outcome[1]} = {target_sum}")
    
    print(f"\nКоличество благоприятных исходов: {count}")
    
    # Анализируем все пространство исходов для контекста
    total_outcomes, sum_distribution = analyze_probability_space()
    
    # Вычисляем вероятность
    probability = count / total_outcomes
    print(f"\nВероятность события A: P(A) = {count}/{total_outcomes} = {probability:.4f}")

# Дополнительная проверка комбинаторным способом
def combinatorial_verification():
    """
    Проверка комбинаторным рассуждением
    """
    print("\n=== КОМБИНАТОРНАЯ ПРОВЕРКА ===")
    print("Для суммы 5 возможны следующие комбинации:")
    print("1 + 4 = 5")
    print("2 + 3 = 5") 
    print("3 + 2 = 5")
    print("4 + 1 = 5")
    print("Всего: 4 благоприятных исхода")

if name == "__main__":
    main()
    combinatorial_verification()
