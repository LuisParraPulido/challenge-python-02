# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here
    minus = chr(random.randint(97,122)) + chr(random.randint(97,122))
    mayus = chr(random.randint(65,90)) + chr(random.randint(65,90))
    num = chr(random.randint(48,57)) + chr(random.randint(48,57))
    simbol = SYMBOLS[random.randint(0, len(SYMBOLS) - 1)] + SYMBOLS[random.randint(0, len(SYMBOLS) - 1)]
    password = minus + mayus + num + simbol
    print(password)
    return password

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
