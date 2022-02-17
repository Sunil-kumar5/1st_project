""" 1) decorativr function to delay the exicusion"""

from time import time , sleep
# def delay(func):
#     def wrapper(*args,**kwargs):
#         sleep(2)
#         return func(*args,**kwargs)
#     return wrapper
#
# @delay
# def add(a,b):
#     return a+b
# print(add(2,2))

""" 2) logging or info decorater"""

# def log(func):
#     def wrapper(*args,**kwargs):
#         print(f"you are calling {func.__name__}")
#         return func(*args,**kwargs)
#     return wrapper
# @log
# def add(a,b):
#     return a+b
# print(add(1,2))
#
# @log
# def sub(a,b):
#     return a-b
# print(sub(2,7))
#
# @log
# def greeting(name):
#     return f"helo {name}"
# print(greeting("sunil"))

""" 3) Decorator for reversing a string"""

# def reverse(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args,**kwargs)
#         if isinstance(result,str):
#             return result[::-1]
#     return wrapper
#
# @reverse
# def srt_(a):
#     return a
# print(srt_(a="sunil kumar"))

""" 4) positive decorator"""

# def positive(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         if isinstance(res,(int,float)):
#             return abs(res)
#         return res
#     return wrapper
#
# def add(a,b):
#     return a+b
# print(add(5,4))
#
# def sub(a,b):
#     return a-b
# print(sub(19,8))

""" 5) Decorator to find execution time"""

# def time_(func):
#     def wrapper(*args,**kwargs):
#         start = time()
#         sleep(2)
#         result = func(*args,**kwargs)
#         end = time()
#         print(f"execution time of function {func.__name__} is {end-start} seconds")
#         return result
#     return wrapper
#
# @time_
# def count_(a):
#     cou_ = 0
#     for i in a:
#         cou_ += 1
#     print(cou_)
# count_("sunil")

""" 6) Decorator for function count"""
# from collections import defaultdict
#
# count_ = defaultdict
#
# def func_count(func):
#     def wrapper(*args,**kwargs):
#         count_[func.__name__] += 1         xxxxxxxxxx
#         func(*args,**kwargs)
#     return wrapper
#
# @func_count
# def  add(a,b):
#     print(a+b)
# add(1,3)
###################################

# def count_(func):
#     def  wrapper(*args,**kwargs):
#         print("the number of arguments are:",len(args)+len(kwargs))
#         func(*args,**kwargs)
#     return wrapper
# @count_
# def add(a,b,c,f):
#     print(a+b+c+f)
# add(1,3,56,5)

""" 7) Decorator to find number of times function execution takes place"""

# def _func_count(func):
#
#     func.count = 0
#     def wrapper(*args,**kwargs):
#         func.count += 1
#         res = func(*args,**kwargs)
#         print(f"function {func.__name__} was invoked {func.count} times")
#         return res
#     return wrapper
#
# @_func_count
# def add(a,b):
#     return a+b
# print(add(4,3))
#
# @_func_count
# def add(a,b):
#     return a+b
# print(add(10,3))
# print(add(10,34))
# print(add(10,344))

""" 8) Decorator for maximum calls of function"""

# def max_call(func):
#     func.count = 0
#     def wrapper(*args,**kwargs):
#         func.count += 1
#         if func.count > 5:
#             raise ValueError(f"maximum calls to function {func.__name__} exceeded")
#         return func(*args,**kwargs)
#     return wrapper
#
# @max_call
# def add(a,b):
#     print(a+b)
# add(1,2)
# add(3,4)
# add(7,7)
# add(5,5)
# add(6,6)
# #add(8,9)

""" 9) repeat decorator """

# def repeat(func):
#     def wrapper(*args,**kwargs):
#         for _ in range(2):
#             func(*args,**kwargs)
#             sleep(2)
#     return wrapper
#
# @repeat
# def mul(a,b):
#     print(a*b)
# mul(4,6)

