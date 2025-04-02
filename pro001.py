import time
from functools import wraps

def time_of_execution(func):

    '''function decori ke zamane ejra ra mohasebe mikonad'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        t_s = time.time()
        result = func(*args, **kwargs)
        t_e = time.time()
        print(func.__name__, t_e-t_s)
        return result
    return wrapper

#estefade
@time_of_execution
def counting(n):
    while n<50000000:
        n += 1

#ham arz ast ba
'''def counting(n):
    while n<5000:
        n += 1

counting = time_of_execution(counting) '''       
        
        

        

    
