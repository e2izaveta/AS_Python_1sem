#15
s = input()  # читаем строку

# Ищем только буквы и проверяем их порядок
letters = [(i, char) for i, char in enumerate(s) if char.isalpha()]

for idx in range(1, len(letters)):
    if letters[idx][1] < letters[idx-1][1]:
        print(letters[idx][0] + 1)  # +1 потому что в задании номер символа (не индекс)
        break
else:
    print(0)
