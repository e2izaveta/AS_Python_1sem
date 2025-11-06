# 15. Разбиение отрезка
A, B, N = 0, 10, 5
H = (B - A) / N
points = [A + i * H for i in range(N + 1)]
print("15.", f"H = {H}", *points)
