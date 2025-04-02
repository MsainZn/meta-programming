from functools import wraps, partial
import logging


def attach_wrapper(obj, func = None):
    if func is None:
        return partial(attach_wrapper, obj)

    setattr(obj, func.__name__ , func)
    return func

def logged(level, name = None, message = None):

    def decorate(func):
        log_name = name if name else func.__module__
        log = logging.getLogger(log_name)
        log_msg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_msg)
            return func(*args, **kwargs)

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
@logged(logging.WARNING)
def add(x,y,z):
    return x+y+z

        
        
