# Читаем количество строк
num_lines = int(input("Введите количество строк: "))
word_count = {}

# Читаем строки текста
for _ in range(num_lines):
    line = input()
    # Разделяем строку на слова
    words = line.split()
    for word in words:
        # Приводим слова к нижнему регистру для учета регистра
        word = word.lower()
        # Увеличиваем счетчик для слова
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# Создаем список кортежей (слово, частота)
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

# Выводим результат с частотой
for word, count in sorted_words:
    print(f"{word}: {count}")