def f(x, y, z):
    # do something expensive job

cache={}
def cached_f(x, y, z):
    # tuples can be dictionary keys.
    key = (x,y,z)
    if key not in cache:
        cache[key] = f(x,y,z)
    return cache[key]