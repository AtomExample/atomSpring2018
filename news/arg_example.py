def foo(*args, **kwargs):
    for arg in args:
        print (arg)
    for key, val in kwargs.items():
        print(key.split('__'))
        print(val)

foo(age__gt=18, second='s2')
