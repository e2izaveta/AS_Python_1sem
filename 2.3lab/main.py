# 15
def RemoveCols(A, K1, K2):
    # Если матрица пустая или K1 > количества столбцов
    if not A or K1 > len(A[0]):
        return A
    
    # Определяем, до какого столбца удалять
    end_col = min(K2, len(A[0]))
    
    # Удаляем столбцы с K1 до end_col
    result = []
    for row in A:
        new_row = []
        for j in range(len(row)):
            # j+1 - потому что в задании нумерация с 1
            if j + 1 < K1 or j + 1 > end_col:
                new_row.append(row[j])
        result.append(new_row)
    
    return result

# Пример
A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

print("Было:")
for r in A:
    print(r)

print("\nУдаляем столбцы 2-3:")
new_A = RemoveCols(A, 2, 3)
for r in new_A:
    print(r)
