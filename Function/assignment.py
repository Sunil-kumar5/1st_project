""" 1) write a decorative function to count the number of arguments passed to the function"""
# def count_(func):
#     def wrapper(*args,**kwargs):
#         print("the no of arguments are :",len(args)+ len(kwargs))
#         func(*args,**kwargs)
#     return wrapper
#
# @count_
# def add (*,a,b,c):
#     return
# add(a=1,b=2,c=3)


""" 2) wadf to return only positive values after subtraction """


# def positive_(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         print(abs(res))
#         func(*args,**kwargs)
#
#     return wrapper
# @positive_
# def sub(a,b):
#     return a-b
# sub(6,10)


""" 3) WADF to print"hello world" message if the user has not given input"""












""" 4) WADF to return the length of the given iterable"""
# def spam(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return len(res)
#     return wrapper
#
# @spam
# def len_(a):
#     return a
# print(len_([1,2,3]))


""" to find nth fibo number"""

# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return(fibo(n-1) + fibo(n-2))
# print(fibo(3))