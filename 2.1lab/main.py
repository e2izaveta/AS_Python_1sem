#15
# a) Минимальное и максимальное значение
d = {'a': 1, 'b': 2, 'c': 3}
print(f"max: {max(d.values())}, min: {min(d.values())}")

# b) Ключи и значения построчно
for k, v in d.items():
    print(f"key: {k}, value: {v}")

# c) Словарь со списками
d2 = {'x': list(range(11, 21)), 
      'y': list(range(21, 31)), 
      'z': list(range(31, 41))}
for k in d2:
    print(f"пятый элемент из {k}: {d2[k][4]}")
