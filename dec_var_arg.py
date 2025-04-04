# ******************** Decorator with Variable Args ************************ #

from functools import wraps, partial

# Wraps func to a function as attr
def attach_wrapper(obj_wrp, func = None):
    if func is None:
        return partial(attach_wrapper, obj_wrp)

    # this is like writing obj_wrp.func = func
    setattr(obj_wrp, func.__name__ , func)
    return func

def logged(level=None, name = None, message = None):

    def decorate(func):
        log_name = name if name else func.__module__
        log_msg = message if message else func.__name__
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(level,' | ', log_msg,' | ', log_name)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_name(newname):
            nonlocal log_name
            log_name = newname

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel


        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal log_msg
            log_msg = newmsg
        
        return wrapper
    
    return decorate


#estefade
@logged('WARNING', name='Moe', message='Start')
def add(x,y,z):
    return x+y+z

print(add(1, 2, 3) ) # Logs at WARNING level

add.set_level('CRITICAL')  # Dynamically change log level to DEBUG

print(add(4, 5, 6))  # Now logs at DEBUG level instead of WARNING

add.set_name('MoeMan')  # Dynamically change log name

print(add(10, 15, 28))  # Now logs at DEBUG level instead of WARNING

add.set_message('This is Moe Message!')  # Dynamically change log name

print(add(10, 15, 28))  # Now logs at DEBUG level instead of WARNING