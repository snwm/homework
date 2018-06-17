def fibonacci(n):
    a = 1
    b = 0
    while n:
        c = a + b
        yield c
        a = b
        b = c

        n -= 1