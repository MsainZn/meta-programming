from functools import partial

x = 1000

def func_out():
    x = 1

    def func_in():
        nonlocal x
        # global x
        x = 500
        print('in: ', x)

    func_in()
    print('out: ', x)
    
func_out()
print('global: ', x)
    
def func(x,y,z):
    return x*4 + 2*y + 5*z

new_add = partial(func, 2, 5)
print('hello')
print(new_add(3))

        
        
