import random

def generate_email():
    login = ''
    for _ in range(3):
        login += random.choice('qwertyuiopasdfghjklzxcvbnm1234567890')
    domain = random.choice(['yandex.ru', 'gmail.com'])
    email = f'{login}@{domain}'
    return email