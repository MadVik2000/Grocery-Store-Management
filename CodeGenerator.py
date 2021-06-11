import random

def gen_code():
    code = ''

    for _ in range(6):
        code = code + str(random.randint(0, 9))

    return int(code)
