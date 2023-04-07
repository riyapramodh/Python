#lambda or anonymous functions
#EXAMPLE 1
#normal function
def add(x,y):
    return x+y
print(add(10,5))

#lambda function
sub = lambda x,y :x-y
print(sub(10,5))

#EXAMPLE 2
#normal way:
def func(a):
    return a[1]

a = [[1,14], [20,3], [2,44]]
a.sort(key = func )
print(a)

#lambda function way
a = [[1,14], [20,3], [2,44],[2,2]]
a.sort(key = lambda a:a[1])
print(a)
