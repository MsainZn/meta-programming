from functools import partial

def func(x,y,z):
    return x*4 + 2*y + 5*z

new_add = partial(func, 2, 5)
print(new_add(3))
