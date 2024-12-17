def is_credit_card_number(card_number):

    if len(card_number) == 16 and card_number.isdigit():
        return True
    return False


def validate_credit_card(card_number):

    if not isinstance(card_number, str):
        raise ValueError("Номер карты должен быть строкой.")

    if not is_credit_card_number(card_number):
        raise ValueError("Некорректный номер кредитной карты.")

    return card_number


# Пример использования
try:
    card = "1234567890123456"
    print(validate_credit_card(card))  # Корректный номер
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    card = "1234 5678-9012-3456"  # Некорректный формат
    print(validate_credit_card(card))
except ValueError as e:
    print(f"Ошибка: {e}")