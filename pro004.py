from functools import wraps

def first_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('First Decorator')
        return func(*args, **kwargs)
    return wrapper


def second_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Second Decorator')
        return func(*args, **kwargs)
    return wrapper

@first_decorator
@second_decorator
def add(x, y):
    return x + y





        
    
