# Задание 4 из ЕГЭ-2025 профиль [https://math-ege.sdamgia.ru/test?id=86355920]
# Игральный кубик бросают дважды. Сколько элементарных исходов опыта благоприятствуют событию «А  =  сумма очков равна 5»?
def count_favorable_outcomes():
    """
    Подсчет количества исходов, где сумма двух бросков кубика равна 5
    """
    favorable = []
    
    # Перебираем все возможные результаты первого броска
    for first in range(1, 7):
        # Для каждого первого броска находим нужный второй бросок
        second = 5 - first
        
        # Проверяем, что второй бросок возможен (от 1 до 6)
        if 1 <= second <= 6:
            favorable.append((first, second))
    
    return favorable

# Решение
favorable_outcomes = count_favorable_outcomes()

print("Благоприятные исходы (сумма = 5):")
for outcome in favorable_outcomes:
    print(f"{outcome[0]} + {outcome[1]} = 5")

print(f"\nКоличество благоприятных исходов: {len(favorable_outcomes)}")
