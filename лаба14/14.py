#Найти количество банков, вывести их в алфавитном порядке, а также найти количество банков, работающих с 9:00.
import pandas as pd
import xml.etree.ElementTree as ET
import re

# Функция для извлечения времени открытия
def extract_opening_hour(opening_hours):
    if isinstance(opening_hours, str):
        match = re.search(r'\b09:00\b', opening_hours)
        return bool(match)
    return False

# Функция для извлечения банков из OSM-файла
def extract_banks_from_osm(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    banks = []
    for node in root.findall("node"):
        tags = {tag.attrib['k']: tag.attrib['v'] for tag in node.findall("tag")}
        if tags.get("amenity") == "bank":
            banks.append({
                "name": tags.get("name", "Unnamed Bank"),
                "opening_hours": tags.get("opening_hours", "Unknown")
            })
    return banks

# Чтение данных из OSM файла
file_path = "6 - 2.osm"  # Укажите путь к вашему OSM файлу
banks_data = extract_banks_from_osm(file_path)

# Преобразуем данные в DataFrame для анализа
banks_df = pd.DataFrame(banks_data)

# Подсчитаем общее количество банков
total_banks = banks_df['name'].nunique()

# Сортировка банков в алфавитном порядке
sorted_banks = banks_df['name'].drop_duplicates().sort_values().tolist()

# Подсчитаем количество банков, работающих с 9:00
banks_df['open_at_9'] = banks_df['opening_hours'].apply(extract_opening_hour)
banks_open_at_9_count = banks_df[banks_df['open_at_9']]['name'].nunique()

# Вывод результатов
print(f"Общее количество банков: {total_banks}")
print("Банки в алфавитном порядке:")
for bank in sorted_banks:
    print(f"- {bank}")
print(f"Количество банков, работающих с 9:00: {banks_open_at_9_count}")