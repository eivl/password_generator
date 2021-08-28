import random
import string
import tkinter as tk

pool = string.ascii_letters + string.digits + string.punctuation


def generate_password(length=12, random_length=False):
    if random_length:
        length = random.randrange(10, 16)
    if length < 4:
        return False
    elif length > 1000:
        return False

    while True:
        password = random.choices(pool, k=length)
        password = ''.join(password)

        if not any(character in string.digits for character in password):
            continue
        if not any(character in string.punctuation for character in password):
            continue
        if not any(
                character in string.ascii_lowercase for character in password):
            continue
        if not any(
                character in string.ascii_uppercase for character in password):
            continue
        break
    return password