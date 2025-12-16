# Читаем исходный файл
with open('input.txt', 'r') as f:
    lines = f.readlines()

# Удаляем первую и последнюю строку
if len(lines) > 2:
    lines = lines[1:-1]

# Записываем в новый файл
with open('output.txt', 'w') as f:
    f.writelines(lines)
