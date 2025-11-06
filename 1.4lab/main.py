# 1. Среднее арифметическое от K до L
lst = [1, 2, 3, 4, 5]; K, L = 2, 4; avg = sum(lst[K-1:L]) / (L-K+1); print("1.", avg)

# 2. Сумма всех элементов кроме K-L
lst = [1, 2, 3, 4, 5]; K, L = 2, 4; total = sum(lst[:K-1] + lst[L:]); print("2.", total)

# 3. Среднее арифметическое кроме K-L
lst = [1, 2, 3, 4, 5]; K, L = 2, 4; filtered = lst[:K-1] + lst[L:]; avg = sum(filtered) / len(filtered); print("3.", avg)

# 4. Четные → нечетные (по индексам)
lst = [1, 2, 3, 4, 5]; evens = [x for x in lst if x % 2 == 0]; odds = [lst[i] for i in range(len(lst)-1, -1, -1) if lst[i] % 2 != 0]; print("4.", *evens, *odds)

# 5. Четные индексы → нечетные индексы
lst = [1, 2, 3, 4, 5]; even_idx = [lst[i] for i in range(0, len(lst), 2)]; odd_idx = [lst[i] for i in range(1, len(lst), 2)]; print("5.", *even_idx, *odd_idx)

# 6. Произведение после максимума
lst = [1, 5, 3, 4, 2]; max_idx = lst.index(max(lst)); product = 1; 
for x in lst[max_idx+1:]: product *= x; print("6.", product)

# 7. Сумма между min и max
lst = [3, 1, 5, 2, 4]; min_idx, max_idx = lst.index(min(lst)), lst.index(max(lst)); 
if min_idx > max_idx: min_idx, max_idx = max_idx, min_idx; total = sum(lst[min_idx:max_idx+1]); print("7.", total)

# 8. Обнулить между min и max
lst = [3, 1, 5, 2, 4]; min_idx, max_idx = lst.index(min(lst)), lst.index(max(lst)); 
if min_idx > max_idx: min_idx, max_idx = max_idx, min_idx; 
for i in range(min_idx+1, max_idx): lst[i] = 0; print("8.", lst)

# 9. Увеличить четные
lst = [1, 2, 3, 4, 5]; n = 10; lst = [x + n if x % 2 == 0 else x for x in lst]; print("9.", lst)

# 10. Обнулить нечетные
lst = [1, 2, 3, 4, 5]; lst = [0 if x % 2 != 0 else x for x in lst]; print("10.", lst)

# 11. Минимальный с четным индексом
lst = [5, 1, 3, 2, 4]; min_even = min(lst[i] for i in range(0, len(lst), 2)); print("11.", min_even)

# 12. Больше правого соседа
lst = [5, 3, 4, 2, 1]; indices = [i for i in range(len(lst)-1) if lst[i] > lst[i+1]]; print("12.", *indices, len(indices))

# 13. Максимальная сумма соседей
lst = [1, 5, 3, 4, 2]; max_sum = max(lst[i] + lst[i+1] for i in range(len(lst)-1)); 
for i in range(len(lst)-1): 
    if lst[i] + lst[i+1] == max_sum: print("13.", lst[i], lst[i+1]); break

# 14. Поменять min и max
lst = [3, 1, 5, 2, 4]; min_idx, max_idx = lst.index(min(lst)), lst.index(max(lst)); 
lst[min_idx], lst[max_idx] = lst[max_idx], lst[min_idx]; print("14.", lst)

# 15. Список с суммой предыдущих
N, A, B = 5, 1, 2; lst = [A, B]; 
for i in range(2, N): lst.append(sum(lst)); print("15.", lst)
