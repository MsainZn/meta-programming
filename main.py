import time
from functools import wraps

# ****************** Decorator ************************** #

def calc_time_of_execution(func:callable):
    '''function decori ke zamane ejra ra mohasebe mikonad'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        t_s = time.time()
        result = func(*args, **kwargs)
        t_e = time.time()
        print(t_e-t_s)
        return result
    return wrapper

@calc_time_of_execution
def do_sth(num:int)->int:
    '''calculate sth'''
    for _ in range(int(num)):
       continue
    return num

def dec_test01():
    # Using Decorator
    print(do_sth(5e8)) 
    return 
# ******************* Underlying Decorator Code ************************* #

def do_sth2(num:int)->int:
    '''calculate sth'''
    for _ in range(int(num)):
       continue
    return num

def dec_test02():
    # Passing Normal Funcs
    print(calc_time_of_execution(do_sth2)(5e8))
    return

# ******************* Multi Decorator ************************* #

def decoratorA(func:callable):
    @wraps(func)
    def wrapper (*args, **kwargs):
        print('Decorator A')
        return func(*args, **kwargs)
    return wrapper

def decoratorB(func:callable):
    @wraps(func)
    def wrapper (*args, **kwargs):
        print('Decorator B')
        return func(*args, **kwargs)
    return wrapper

# First Decorator Excecutes First
@decoratorA
@decoratorB
def do_sth3(num:int)->int:
    '''calculate sth'''
    for _ in range(int(num)):
       continue
    return num

def dec_test03():
    # Using two decorators
    print(do_sth3(5e8)) 
    return

# ******************** Decorator With Fixed Variable ************************ #

def decorator_with_args(arg1:int, action_nane:str):
    def sub_decorator(func:callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t_s = time.time()
            res = func(*args, **kwargs)
            t_e = time.time()
            print(f'{action_nane} took:{t_e-t_s:.2f} seconds')
            return res * arg1
        return wrapper
    return sub_decorator

@decorator_with_args(2, 'Darkness')
def do_sth4(num:int, som:str)->int:
    '''calculate sth'''
    for _ in range(int(num)):
       continue
    return f'Result of {som} is {num}'

def dec_test04():
    # Using decorator with args
    print(do_sth4(1e6, 'Moe')) 
    return

# ******************** Class Decorator ************************ #

class DecoratorClass:
    def __init__(self):
        print('DecoratorClass __init__')
    
    def decoratorA(self, func:callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator A')
            return func(*args, **kwargs)
        return wrapper

    def decoratorB(self, func:callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator B')
            return func(*args, **kwargs)
        return wrapper

@DecoratorClass().decoratorA
@DecoratorClass().decoratorB
def do_sth5(num:int)->int:
    '''calculate sth'''
    for _ in range(int(num)):
       continue
    return num

def dec_test05():
    # Using class decorator
    print(do_sth5(5e6)) 
    return


if __name__ == "__main__":
    dec_test05()