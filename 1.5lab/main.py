# 1. Нечетные числа по убыванию
lst = [5, 2, 8, 1, 9, 3]
result = sorted([x for x in lst if x % 2 != 0], reverse=True)
print("1.", result)

# 2. Положительные числа по возрастанию
lst = [5, -2, 8, -1, 9, 3]
result = sorted([x for x in lst if x > 0])
print("2.", result)

# 3. Положительные числа по убыванию
lst = [5, -2, 8, -1, 9, 3]
result = sorted([x for x in lst if x > 0], reverse=True)
print("3.", result)

# 4. Четные числа по возрастанию
lst = [5, 2, 8, 1, 9, 4]
result = sorted([x for x in lst if x % 2 == 0])
print("4.", result)

# 5. Числа > k по убыванию
lst = [5, 2, 8, 1, 9, 3]; k = 4
result = sorted([x for x in lst if x > k], reverse=True)
print("5.", result)

# 6. Числа > 10 по возрастанию
lst = [15, 2, 18, 1, 9, 12]
result = sorted([x for x in lst if x > 10])
print("6.", result)

# 7. Числа кратные 5 по убыванию
lst = [15, 2, 10, 1, 25, 12]
result = sorted([x for x in lst if x % 5 == 0], reverse=True)
print("7.", result)

# 8. Числа < k по возрастанию
lst = [5, 2, 8, 1, 9, 3]; k = 6
result = sorted([x for x in lst if x < k])
print("8.", result)

# 9. Числа < 15 по убыванию
lst = [15, 2, 18, 1, 9, 12]
result = sorted([x for x in lst if x < 15], reverse=True)
print("9.", result)

# 10. Числа кратные 3 по возрастанию
lst = [15, 2, 9, 1, 12, 7]
result = sorted([x for x in lst if x % 3 == 0])
print("10.", result)

# 11. Числа кратные k по убыванию
lst = [15, 2, 10, 1, 25, 12]; k = 5
result = sorted([x for x in lst if x % k == 0], reverse=True)
print("11.", result)

# 12. Отрицательные числа по возрастанию
lst = [5, -2, 8, -1, -9, 3]
result = sorted([x for x in lst if x < 0])
print("12.", result)

# 13. Числа на нечетных позициях по убыванию
lst = [5, 2, 8, 1, 9, 3]
result = sorted([lst[i] for i in range(len(lst)) if i % 2 != 0], reverse=True)
print("13.", result)

# 14. Двузначные числа по возрастанию
lst = [5, 25, 8, 15, 99, 3]
result = sorted([x for x in lst if 10 <= x <= 99])
print("14.", result)

# 15. Числа на четных позициях по возрастанию
lst = [5, 2, 8, 1, 9, 3]
result = sorted([lst[i] for i in range(len(lst)) if i % 2 == 0])
print("15.", result)
