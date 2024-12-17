# В порядке увеличение квадратичного отклонения частоты встречаемости самого распространенного символа в наборе строк от частоты его встречаемости в данной строке.
from collections import Counter

def most_frequent_char_in_set(strings):
    """Находит самый частый символ во всем наборе строк."""
    combined_counter = Counter("".join(strings))
    return combined_counter.most_common(1)[0][0]  # Возвращает символ с наибольшей частотой

def frequency_in_string(char, string):
    """Вычисляет частоту символа в строке."""
    return string.count(char) / len(string)

def quadratic_deviation(global_freq, string_freq):
    """Вычисляет квадратичное отклонение частот."""
    return (global_freq - string_freq) ** 2

def sort_by_quadratic_deviation(strings):
    """Сортирует строки по квадратичному отклонению частоты самого частого символа."""
    most_common_char = most_frequent_char_in_set(strings)

    # Вычисляем глобальную частоту самого частого символа
    total_occurrences = sum(s.count(most_common_char) for s in strings)
    total_length = sum(len(s) for s in strings)
    global_freq = total_occurrences / total_length

    # Сортируем строки по квадратичному отклонению
    return sorted(strings, key=lambda s: quadratic_deviation(global_freq, frequency_in_string(most_common_char, s)))

# Пример использования
strings = [
    "aaaaaa",
    "aabc",
    "bbccc",
    "xyz",
    "aaabbbccc",
    "abcdefg"
]

sorted_strings = sort_by_quadratic_deviation(strings)
print(sorted_strings)