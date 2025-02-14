def myFun(*args):
    for arg in args:
        print(arg)


myFun('Hello', 'Welcome', 'to')



def fun(**kwargs):
    for k, val in kwargs.items():
        #print("%s == %s" % (k, val))
        print(str(k)+ " = "+str(val))


# Driver code
fun(s1='Geeks', s2='for', s3='Geeks')

def fun(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

fun(1, 2, 3, a=4, b=5)
