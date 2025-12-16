# 15
def add(a, b, c, d):
    # a/b + c/d
    num = a * d + c * b
    den = b * d
    return num, den

def sub(a, b, c, d):
    # a/b - c/d
    num = a * d - c * b
    den = b * d
    return num, den

def mul(a, b, c, d):
    # a/b * c/d
    num = a * c
    den = b * d
    return num, den
    import fraction_operations as fo

# Пример использования
print("3/4 + 1/2 =", fo.add(3, 4, 1, 2))  # (10, 8)
print("3/4 - 1/2 =", fo.sub(3, 4, 1, 2))  # (2, 8)
print("3/4 * 1/2 =", fo.mul(3, 4, 1, 2))  # (3, 8)
