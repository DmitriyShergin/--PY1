import random, string

def get_random_password(len_: int = 8) -> str:
    if len_ > 62:
        raise ValueError("Длина пароля превышает количество символов")
    return ''.join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, len_))


print(get_random_password(63))
