# 6 What is the meaning of the word global inside a function?

#Answer: Global keyword is used when we want to read or write any global variable value inside the function.

# What is the disadvantage of using global as part of a function? What will this require in the future...

#Answer: It creates difficulty in debugging and maintenance.

# Why do we get an error here?

#Answer: We get the unbound local error because the valor assigned to x in this case 4 was assigned inside the fucntion but not yet executed when we print(x), due to this "x" value is unknow.

x : int = 1
def foo():
    print(x)
    x = 4
foo()