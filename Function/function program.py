"""write a function to add two number and return the result"""
# use position as well as key argument
# def add_(a,b,/):
#     a = 1
#     b = 2
#     c = a + b
#     return(c)
# print(add_(1,2))
#
# def add_(*,a,b):
#     a = 1
#     b = 2
#     c = a + b
#     return(c)
# print(add_(a=1,b=2))


"""write a function to even numbers  from given range"""
# def even_(e1,e2):
#     l = []
#     for i in range(e1,e2):
#         if i % 2 == 0:
#             l.append(i)
#     return l
#
# print(even_(1,51))

"""write a function that returns all the prime numbers in user defined range, if the user doesnot provide start index 
take it as 2 """

# def prime_(end,start=2):
#     l = []
#     for i in range(2,end+1):
#         if i > 1:
#             for j in range(2,i):
#                 if n % i == 0:
#                  break
#                 else:
#                     l.append(i)
#     return(l)
#
#
#
# print(prime_(start=1,end=50))


"""to print fibonacci series"""
# def fibo(f):
#     a = 0
#     b = 1
#     i = 0
#     while i < 10:
#         print(a)
#         c = a + b
#         a = b
#         b = c
#         i += 1
#
#
# print(fibo(10))

""" write a function to print nth fibonacci number"""

# def fibo(n):
#     if n <= 0:
#         pass
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
#
# print(fibo(10))


""" write a function that returns fibonacci series up to the number specified"""

# def fibo(num):
#
#     n1, n2 = 0, 1
#     print("Fibonacci Series:", n1, n2, end=",")
#     for i in range(2, num):
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3
#         print(n3, end=",")
#
#
# print(fibo(10))

#
# def spam(*args):
#     print(args)
#     count = 0
#     for i in args:
#         count += 1
#     return count
#
# print(spam(1,2))


""" 4) it the type string reverse it"""
# def func_(*args):
#     l = []
#     for item in args:
#         if isinstance(item,str):
#             l.append(item[::-1])
#     return l
#
#
# print(func_("hii",3,5,"gkkjj"))
""""""
#
# def prime_(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return "n is not prime"
#         return "n is prime"
#
# print(prime_(8))

""""""
# def last_(num):
#     b = str(num)
#     for i in b:
#         return b[-1]
#
# print(last_(5697))

""""""

# def func(args,n):
#     if n == 0:
#         if i == 0:
#             return args[1::2]

# def fibo(num):
#     a = 0
#     b = 1
#     while a <= num:
#         if a == num:
#             return f"{num} is fibo"
#         c = a+b
#         a = b
#         b = c
#     return f"{num} is not fibo"
#
# print(fibo(7))

"""length of iterables"""
# def var(*args):
#     for i in args:
#         if isinstance(i,(str,list,tuple,set,dict)):
#             print(i,len(i))
#
# var(1,2,"hello",[3,4,5],(3,4,5,6))
