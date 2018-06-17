import random

def password_generator(n):
    while 1:
        pas = []
        for i in range(n):
            simb = chr(random.randint(33, 126))
            pas.append(simb)

        yield "".join(pas)