def fun1():
    print("normal funnction")
fun1()

def fun2(a):
    print("parameterized function ",a)
fun2(5)

def fun3(a,b=5,c=2):
    print("default value function",a,b,c)
fun3(10,20)

def fun4(a,b,c):
    print("keyword argument function",a,b,c)
fun4(5,5,c=7)

def fun5(a,*b):
    print("variable length argument",b)
fun5(5,5,5,4,6,4)

#advanced function=lambda
a1=lambda a:a*5
print(a1(5))

lst=[1,5,8,45,4,55,45,4,48,31,3]
def ages(x):
    if x>=18:
        return True
    else:
        return False
adults=filter(ages,lst)#lst values will go to x of ages
print(adults)#itla pedthe output filter and its location osthadi so convert it to string <filter object at 0x0000024D8A629850>
print(list(adults))#[45, 55, 45, 48, 31]

def mapfunction(x):
    return x**2 #returns exponents of
numbers=(1,2,3,4,5)
exp=map(mapfunction,numbers)
print(list(exp))

def yieldfuncton():
    yield 1
    yield 22
    yield 3
x=yieldfuncton()
print(x.__next__())#1
print(x.__next__())#22
print(x.__next__())#3