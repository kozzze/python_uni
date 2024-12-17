#1) В порядке увеличения разницы между частотой наиболее часто
#встречаемого символа в строке и частотой его появления в алфавите.
from collections import Counter
import string

def get_char_frequency_in_alphabet():
    # Создаем словарь с частотой символов в английском алфавите
    english_text = (
        "ETAOINSHRDLCUMWFGYPBVKJXQZ"  # Пример частот на английском
    ).lower()
    total_letters = len(english_text)
    return {char: english_text.count(char) / total_letters for char in string.ascii_lowercase}

def most_frequent_char_difference(line, alphabet_freq):
    # Считаем частоту символов в строке
    line_counter = Counter(line.lower())
    total_chars = sum(line_counter.values())

    # Находим наиболее частый символ и его частоту
    most_common_char, most_common_freq = line_counter.most_common(1)[0]
    freq_in_line = most_common_freq / total_chars
    freq_in_alphabet = alphabet_freq.get(most_common_char, 0)

    # Возвращаем разницу частот
    return abs(freq_in_line - freq_in_alphabet)

def sort_strings_by_difference(lines):
    # Получаем частоту символов в алфавите
    alphabet_freq = get_char_frequency_in_alphabet()

    # Сортируем строки по разнице частот
    return sorted(lines, key=lambda line: most_frequent_char_difference(line, alphabet_freq))

# Пример использования
lines = [
    "hello",
    "world",
    "frequency",
    "sorted",
    "text",
]

sorted_lines = sort_strings_by_difference(lines)
print(sorted_lines)