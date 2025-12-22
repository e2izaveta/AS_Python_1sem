# 15
# а) Проверка имени
name = "Liza"
name = name.strip()
if not name:
    raise Exception("Некорректное имя")
print("Имя введено корректно")

# б) Проверка возраста
age = 18
if age < 0 or age > 120:
    raise Exception("Некорректный возраст")
print("Возраст введен корректно")

# в) Проверка пола
gender = "ж"
gender = gender.strip().lower()
assert gender in ['м', 'ж'], "Некорректный пол"
print("Пол введен корректно")
