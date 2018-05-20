from functools import wraps
import time

def pause(t):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(t)
            return func(*args, **kwargs)
        return wrapper
    return decorator
