from functools import wraps
import logging

def logged(level, name = None, message = None):

    def decorate(func):
        log_name = name if name else func.__module__
        log = logging.getLogger(log_name)
        log_msg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_msg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

#estefade
@logged(logging.DEBUG, 'car', 'salam')
def add(x,y,z):
    return x+y+z

        
        
