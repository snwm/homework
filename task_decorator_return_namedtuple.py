from functools import wraps
from collections import namedtuple

def return_namedtuple(*keys):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, tuple):
                Parts = {v:result[i] for i,v in enumerate(keys)}
                name_tuple = namedtuple('Parts', Parts.keys())(**Parts)
                return name_tuple
        return wrapper
    return decorator
    
