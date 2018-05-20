from functools import wraps
import hashlib

save = 0

def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global save
        if save: 
            return func(*args, **kwargs)

        with open("token.txt") as f:
            token = f.read()
            
        n = 0
        while n < 3:
            check = make_token(input(), input())
            if token == check:
                save = 1
                return func(*args, **kwargs)
            n += 1
        return
    return wrapper
