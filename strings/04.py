
a = "malli"
def foo():
    global x
    y = "local"
    x = x * 2
    print(a)
    print(y)
foo()  