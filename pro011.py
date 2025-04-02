from functools import wraps

class A:

    def first_decorator(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('first_decorator')
            return func(*args, **kwargs)
        return wrapper

    def second_decorator(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('second_decorator')
            return func(*args, **kwargs)
        return wrapper


a = A()

@a.first_decorator
def abcd():
    pass

@a.second_decorator
def dcba():
    pass




    
