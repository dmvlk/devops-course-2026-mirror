# validator.py
# fix typo in docstring
def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Проверка российского номера телефона."""
    return len(phone) == 11 and phone.isdigit()


def validate_snils(snils: str) -> bool:
    """Валидация СНИЛС."""
    return len(snils) == 11 and snils.isdigit()
