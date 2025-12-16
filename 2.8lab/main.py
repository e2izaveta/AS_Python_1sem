# 15
# Открываем файлы
with open('f.txt', 'r') as f:
    numbers = [int(x) for x in f.read().split()]

# Разделяем на положительные и отрицательные
positive = [x for x in numbers if x > 0]
negative = [x for x in numbers if x < 0]

# Формируем новый список
result = []
for i in range(0, len(positive), 2):
    result.extend(positive[i:i+2])
    result.extend(negative[i:i+2])

# Записываем результат
with open('g.txt', 'w') as g:
    g.write(' '.join(map(str, result)))
