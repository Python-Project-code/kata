
def add10(x): return x + 10
def mul30(x): return x * 30



def chain(init_val, functions):
  
    for f in functions:
       init_val= f(init_val)
       return init_val



print(chain(50, [add10, mul30]))




