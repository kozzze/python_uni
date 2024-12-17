def find_max_sum(arr: list, K: int):
    N = len(arr)
    if N < 3 * K:
        return None

    # Инициализация массивов максимумов
    max_from_start = [float('-inf')] * N
    max_from_end = [float('-inf')] * N

    # Заполнение max_from_start
    for i in range(N - 2 * K):
        max_from_start[i] = max(arr[i], max_from_start[i - 1] if i > 0 else float('-inf'))

    # Заполнение max_from_end
    for i in range(N - 1, 2 * K - 1, -1):
        max_from_end[i] = max(arr[i], max_from_end[i + 1] if i < N - 1 else float('-inf'))

    # Вычисление максимальной суммы
    max_sum = float('-inf')
    for j in range(K, N - K):
        left_max = max_from_start[j - K]
        right_max = max_from_end[j + K]
        current_sum = left_max + arr[j] + right_max
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


# Загрузка массивов из файлов
try:
    array_from_file_A = list(map(int, open('27-167a.txt', 'r', encoding='UTF-8').read().split()))
    array_from_file_B = list(map(int, open('27-167b.txt', 'r', encoding='UTF-8').read().split()))

    # Извлечение задержки и самих массивов
    a_delay = array_from_file_A[1]
    b_delay = array_from_file_B[1]

    array_a = array_from_file_A[2:array_from_file_A[0] + 2]
    array_b = array_from_file_B[2:array_from_file_B[0] + 2]

    print("Максимальная сумма для массива из файла 27-167a.txt:", find_max_sum(array_a, a_delay))
    print("Максимальная сумма для массива из файла 27-167b.txt:", find_max_sum(array_b, b_delay))

except FileNotFoundError:
    print("Файл не найден. Убедитесь, что файлы 27-167a.txt и 27-167b.txt существуют.")