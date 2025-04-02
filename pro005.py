def decorator(arg1, arg2):
    
    def sub_decorator(func):
        
        def wrapper(*args, **kwargs):
            print('decorating with {0} , {1}'.format(arg1, arg2))
            return func(*args, **kwargs)
        return wrapper
    return sub_decorator

@decorator('arg1', 'arg2')
def abcd(*args):
    for arg in args:
        print (arg)

        
