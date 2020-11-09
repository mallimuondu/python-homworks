def foo():
    x = 20
    
    def bar():
        global(x)
        x = 25
            print("Before calling bar: ", x)
            print("x in main : ", x)  print("Calling bar now")
            bar()
            print("After calling bar: ", x)
            foo()