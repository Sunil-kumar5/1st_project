""" write a decorative to import delay before executing only function"""
# import time
# def delay(func):
#     def wrapper(*args,**kwargs):
#         time.sleep(2)
#         return func(*args,**kwargs)
#     return wrapper
# @delay
# def display():
#     return "in display"
# print(display())

""" write a decorator which takes a string a reverse it"""
# def reverse_(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return res[::-1]
#         # return func(*args,**kwargs)[::-1]
#
#     return wrapper
#
# @reverse_
# def spam(string):
#     return string
# print(spam("hello"))

"""write a decorater to execute a function for 3 times"""



