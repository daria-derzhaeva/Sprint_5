import random
import string

def generate_unique_email():
    random_suffix = ''.join(random.choices(string.digits, k=6))
    return f"user{random_suffix}@test.com"

def generate_password(length=8):
    if length < 6:
        raise ValueError("Длина пароля должна быть не менее 6 символов")
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

def generate_name(length=6):
    if length < 3:
        raise ValueError("Длина имени должна быть не менее 3 символов")
    return ''.join(random.choices(string.ascii_letters, k=length)).capitalize()