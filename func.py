def hello():
    print("Hello")

hello()

def multiple_items(*args):
    print(args)
    print(type(args))
          
multiple_items(1, 2, 3, 4, 5)


def multiple_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
          
multiple_named_items(a=1, b=2, c=3, d=4, e=5)