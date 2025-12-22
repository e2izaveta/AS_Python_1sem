# 15
# Чтение файла
with open('f.txt', 'r') as f:
    data = f.read().split()

n = int(data[0])  # размер матрицы
k = int(data[1])   # количество матриц

matrices = []
idx = 2

# Чтение k матриц
for _ in range(k):
    matrix = []
    for i in range(n):
        row = list(map(int, data[idx:idx+n]))
        matrix.append(row)
        idx += n
    matrices.append(matrix)

# Вычисление произведений диагоналей
products = []
for matrix in matrices:
    prod = 1
    for i in range(n):
        prod *= matrix[i][i]
    products.append(prod)

# Ввод порога
threshold = int(input("Введите число: "))

# Запись подходящих матриц
with open('g.txt', 'w') as g:
    for i, matrix in enumerate(matrices):
        if products[i] > threshold:
            for row in matrix:
                g.write(' '.join(map(str, row)) + '\n')
            g.write('\n')

# Вывод содержимого файлов
print("Содержимое f.txt:")
with open('f.txt', 'r') as f:
    print(f.read())

print("\nСодержимое g.txt:")
with open('g.txt', 'r') as g:
    content = g.read()
    if content:
        print(content)
    else:
        print("Файл пуст")
