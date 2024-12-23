import pandas as pd

# Загрузка данных из CSV файла
file_path = '6 - 1.csv'  # Укажите правильный путь к файлу
data = pd.read_csv(file_path)

# Перевод месяцев с русского на числовой формат
month_translation = {
    'Январь': '01', 'Февраль': '02', 'Март': '03', 'Апрель': '04', 'Май': '05', 'Июнь': '06',
    'Июль': '07', 'Август': '08', 'Сентябрь': '09', 'Октябрь': '10', 'Ноябрь': '11', 'Декабрь': '12'
}

def translate_date(date_str):
    if pd.isnull(date_str):
        return date_str
    for ru_month, num_month in month_translation.items():
        if ru_month in date_str:
            return date_str.replace(ru_month, num_month)
    return date_str

# Обработка столбцов с датами
data['Тест начат'] = pd.to_datetime(data['Тест начат'].apply(translate_date), format='%d %m %Y %H:%M', errors='coerce')
data['Завершено'] = pd.to_datetime(data['Завершено'].apply(translate_date), format='%d %m %Y %H:%M', errors='coerce')

# Преобразование оценки в числовой формат
data['Оценка/100,00'] = pd.to_numeric(data['Оценка/100,00'].str.replace(',', '.'), errors='coerce')

# Заданные параметры
cutoff_date = pd.to_datetime('12 05 2017', format='%d %m %Y')
min_score = 60

# Фильтрация данных
successful_attempts = data[
    (data['Тест начат'] > cutoff_date) &
    (data['Оценка/100'] >= min_score)
]

# Группировка по адресу электронной почты, выбор первой попытки
first_attempt_success = successful_attempts.sort_values(by='Тест начат').groupby('Адрес электронной почты').first()

# Вывод результата
result = first_attempt_success[['Фамилия', 'Имя', 'Учреждение (организация)', 'Тест начат', 'Оценка/100,00']]
print(result)