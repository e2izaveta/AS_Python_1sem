#15
# а) Функция change_case
def change_case(strings, to_upper=False):
    if to_upper:
        return ' '.join(s.upper() for s in strings)
    return ' '.join(s.lower() for s in strings)

# б) Функция filter_combined_lists
def filter_combined_lists(list1, list2, filter_function=None):
    combined = list1 + list2
    if filter_function:
        return [x for x in combined if filter_function(x)]
    return combined

# в) Функция unique_sorted_numbers
def unique_sorted_numbers(numbers):
    return sorted(set(numbers))

# г) Функция strings_starting_with_upper
def strings_starting_with_upper(*args):
    return [s for s in args if s and s[0].isupper()]

# Примеры использования
print(change_case(['Hello', 'World']))  # 'hello world'
print(change_case(['Hello', 'World'], to_upper=True))  # 'HELLO WORLD'

print(filter_combined_lists([2, 4], [6, 8]))  # [2, 4, 6, 8]
print(filter_combined_lists([2, 4], [6, 8], filter_function=lambda x: x > 5))  # [6, 8]

print(unique_sorted_numbers([3, 1, 2, 3, 4, 2]))  # [1, 2, 3, 4]
print(unique_sorted_numbers([5, 5, 5, 5]))  # [5]

print(strings_starting_with_upper('Apple', 'banana', 'Cherry'))  # ['Apple', 'Cherry']
print(strings_starting_with_upper('dog', 'Elephant', 'fox'))  # ['Elephant']
