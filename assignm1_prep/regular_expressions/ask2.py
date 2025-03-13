import re

def is_valid_phone(phone):
    pattern = r"\+447\d{9}$"
    return bool(re.match(pattern, phone))