def some_function(abc):
    print(abc)

#some_function("test")
#some_function("ind vs eng")
#some_function("sa vs pak")

def variable_arguments(*args):

    print(type(args))
    for i in args:
        print(i)
        #print ("Hi")

#variable_arguments(1,3,4,5,6,"rd")

def keyword_varaible_arguments(**kwargs):
    for k,v in kwargs.items():
        print(k)
        print(v)

keyword_varaible_arguments(a=4,b=5,c=9)