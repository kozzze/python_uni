#6. В порядке увеличения медианного значения выборки строк

import statistics


def calculate_median(values):
    """Вычисляет медиану для списка строк."""
    lengths = [len(s) for s in values]
    return statistics.median(lengths)


def sort_by_increasing_median(strings):
    """Сортирует строки в порядке увеличения медианы с пересчетом."""
    result = []
    working_set = strings[:]

    while working_set:
        # Находим медиану для текущего набора
        current_median = calculate_median(working_set)

        # Сортируем строки по отклонению от медианы
        working_set.sort(key=lambda s: abs(len(s) - current_median))

        # Удаляем строку, соответствующую текущей медиане
        median_string = working_set.pop(0)
        result.append(median_string)

    return result


# Пример использования
strings = [
    "short",
    "muchlongerstring",
    "mediumlength",
    "longish",
    "veryverylongstring"
]

sorted_strings = sort_by_increasing_median(strings)
print(sorted_strings)