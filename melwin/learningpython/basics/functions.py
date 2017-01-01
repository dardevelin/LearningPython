global_var_1 = 10
def func_1(arg1, arg2):
    print(arg1,arg2, global_var_1)
    # cannot use global_var_2
    return arg1+" "+arg2

print(func_1("hi", "there"))

## Pass by Reference
global_var_2 = 20
def func_ref_1(a):
    a+=1

def func_ref_2(a):
    a[1]=2

a=1
func_ref_1(a)
print(a)

a=[1,3,3]
func_ref_2(a)
print(a)

## Default Argument
def func_def(arg1, arg2=2, arg3=3):     #arg3 should also be default
    print(arg1,arg2,arg3)
    
func_def(arg3=3, arg1=1)    #call them in any order

## Variable Length Argument
def func_var(arg1, *argvar):
    for var in argvar:
        print(var)
        
func_var(1, 1,2,3)

## Keyword argument 
def func_keyword(arg1, *var_args, **kwargs):
    print(arg1)
    for var_arg in var_args:
        print("var_arg="+str(var_arg))
        
    for k in kwargs.keys():
        print("kwargs value="+str(kwargs[k]))

func_keyword(1,1,name='melwin',age=25)
    