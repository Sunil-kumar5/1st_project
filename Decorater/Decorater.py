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

""" 2) logging or info decorator"""

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
# count_ = defaultdict(int)
#
# def func_count(func):
#     def wrapper(*args,**kwargs):
#         count_[func.__name__] += 1
#         return func(*args,**kwargs)   # Execution part
#     return wrapper           #  returning the value
#
# @func_count
# def add(a,b):
#     return a+b
# print(add(1,3))
# print(add(4,5))
# print(count_)

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

""" 10) cache decorator"""

# def cache(func):
#     func._cache = {}   # attaching an empty dict
#     def wrapper(*args,**kwargs):
#         if args in func._cache:
#             print("getting result from cache")
#             return func._cache[args]
#         print("executing func for the first time")
#         result = func(*args,**kwargs)
#         func._cache[args] = result
#         return result
#     return wrapper
#
# @cache
# def sub(a,b):
#     return a-b
# print(sub(6,1))
# print(sub(7,4))
# print(sub(9,5))
# print(sub(6,1))

""" 11) If there are 10 numbers  add 91+ at 1st if there 12 numbers add + at second index"""

# def add_prefix(number):
#     str_number = str(number)
#     if len(str_number) == 10:
#         str_number = "+91-" + str_number
#         return str_number
#     elif len(str_number) == 12 and str_number.startswith("91"):
#         str_number = "+" + str_number[:2] + "-" + str_number[2:]
#         return str_number
#     else:
#         return str_number
# def prefix_couontry_code(func):
#     def wrapper(*args,**kwargs):
#         temp = args[0]
#         processed_numbers = [add_prefix(number) for number in temp]
#         return func(processed_numbers)
#     return wrapper
#
# @prefix_couontry_code
# # ph = [1234567890,9087654321,911234567890,119876543210]
# def print_number(ph):
#     for item in ph:
#         print(item)
# print_number([1234567890,9087654321,911234567890,119876543210])

""" 12) To validate the data types"""

# def validate_types(expected_type, actual_value):
#     for expected_type, actual_value in zip(expected_type, actual_value):
#         if not isinstance(actual_value, expected_type):
#             raise TypeError("not same data type")
#
# def validate(*expected_types):
#     def _validate(func):
#         def wrapper(*args, **kwargs):
#             validate_types(expected_types, args)
#             return func(*args, **kwargs)
#         return wrapper
#     return _validate
#
# @validate(float, float)
# def sub(a, b):
#     return a - b
# print(sub(2.2,3.3))
#
# @validate(int, float)
# def mul(a, b):
#     return a * b
# print(mul(5,2.3))

""" 13) Attaching a count attribute to the function object, to count the function call"""

# def attach(func):
#     func.count = 0
#     return func
#
# @attach
# def add(a,b):
#     add.count += 1
#     return a+b
# print(add(2,5))
# print(add(2,8))
# print(add(41,5))
# print(f"number of function calls = {add.count}")
#
# @attach
# def sub(a,b):
#     sub.count += 1
#     return a-b
# print(sub(2,5))
# print(sub(8,5))
# print(sub(255,5))
# print(f"number of function calls = {sub.count}")

""" 14)  """

# functipon decorator
#
# def log(func):
#     def wrapper(*args,**kwargs):
#         print(f'calling  {func.__name__}')
#         return func(*args,**kwargs)
#     return wrapper
#
# # class decorator
# class Log:
#     def __init__(self,func):
#         self.func = func
#         def __call__ (self,*args,**kwargs):
#             print(f'calling{self.func.__name__}')
#             return self.func(*args,**kwargs)
#
# @log
# def add(a,b):
#     print(a+b)
# add(1,2)
#
# @Log
# def sub(a,b):
#     print(a-b)
# sub(4,2)
###################
# Extract only int

L = ['2','HG3H','256','FG','95']
# for item in L:
#     for i in item:
#         if '0' <= i <= '9':
#             pass
#         else:
#             break
#     else:
#         print(item)