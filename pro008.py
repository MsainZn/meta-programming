x = 1000

def func_out():
    x = 1

    def func_in():
        nonlocal x
        #global x
        x = 500
        print('in: ', x)

    func_in()
    print('out: ', x)
    
func_out()
print('global: ', x)


    

    

        
        
