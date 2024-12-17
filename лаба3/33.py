#В порядке увеличения квадратичного отклонения между средним весом ASCII-кода символа в строке и максимально среднего ASCIl-кода тройки подряд идущих символов в строке.
def average_ascii(s):
    """Вычисляет среднее значение ASCII-кодов символов в строке."""
    return sum(ord(c) for c in s) / len(s)

def max_average_ascii_of_triplets(s):
    """Находит максимальное среднее значение ASCII-кодов для троек подряд идущих символов."""
    if len(s) < 3:
        return average_ascii(s)  # Если строка меньше 3 символов, берем среднее всей строки
    return max(
        (ord(s[i]) + ord(s[i+1]) + ord(s[i+2])) / 3
        for i in range(len(s) - 2)
    )

def quadratic_deviation(s):
    """Вычисляет квадратичное отклонение между средним ASCII строки и максимальным средним ASCII тройки."""
    avg_ascii = average_ascii(s)
    max_triplet_ascii = max_average_ascii_of_triplets(s)
    return (avg_ascii - max_triplet_ascii) ** 2

def sort_by_quadratic_deviation(strings):
    """Сортирует строки в порядке увеличения квадратичного отклонения."""
    return sorted(strings, key=quadratic_deviation)

# Пример использования
strings = [
    "abcde",
    "hello",
    "world",
    "aaa",
    "zzz",
    "python",
]

sorted_strings = sort_by_quadratic_deviation(strings)
print(sorted_strings)