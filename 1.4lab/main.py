# 15. Список с суммой предыдущих
N, A, B = 5, 1, 2; lst = [A, B]; 
for i in range(2, N): lst.append(sum(lst)); print("15.", lst)
