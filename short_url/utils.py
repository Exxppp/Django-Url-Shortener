import re

from faker import Faker

fake = Faker()


def generate_random_short_url() -> str:
    short_url = fake.unique.bothify(letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890',
                                    text='????')
    return short_url


def check_short_url(url: str) -> bool:
    if url not in ['links', 'admin', 'login', 'registration', 'logout', 'profile'] and \
            len(url) != 4 and \
            re.match("^[a-zA-Z0-9]*$", url):
        return True
    return False
