# 15. Числа на четных позициях по возрастанию
lst = [5, 2, 8, 1, 9, 3]
result = sorted([lst[i] for i in range(len(lst)) if i % 2 == 0])
print("15.", result)
