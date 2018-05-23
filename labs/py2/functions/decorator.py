# -*- coding: utf-8 -*-
def printlog(func):
    #wrapper로 기술해줘야 arg 인자를 처리할 수 있음 왜지?
    def wrapper(arg):
        print("CALLING: " + func.__name__)
        return func(arg)
    return wrapper

@printlog
def f(n):
    return n

#print(f(3))

#Masking
def check_id(func):
    def wrapper(arg):
        print("ID of func: {}".format(id(func)))
        return func(arg)
    print("ID of wrapper: {}".format(id(wrapper)))
    return wrapper

@check_id
def multiple_func(x):
    return x*3

print(multiple_func(2))
print(id(multiple_func))

#id(func) in wrapper , id(wrapper) in wrapper, bare function : multiple_func's id all differnet 