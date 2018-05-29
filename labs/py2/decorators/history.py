def history(func):
    return_vals = set()
    def wrapper(*args, **kwargs):
        return_val = func(*args, **kwargs)
        return_vals.add(return_val)
        print("Return Vals : " + str(sorted(return_vals)))
    return wrapper

@history
def foo(x):
    return x+2

foo(3)
foo(1)
foo(5)