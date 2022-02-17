# 1)
# a = 10
# def fun1():
#     global a
#     a += 20          #(30)
#
#     def inner():
#         nonlocal a
#         a += 10      # error
#
# fun1()
# print(a)

# 2)

# import sys
# print(sys.setrecursionlimit(10000))       # None

# 3)

# a = map(lambda x: x%2 == 0,a)
# print(a(10))         #####  error

# 4)

# x = [2,3,4,5,6,7,8]
# s = (item if item % (item-1) == 1 else str(item) for item in x)
# print(set(s))                      ### {3, 4, 5, 6, 7, 8, '2'}
#
# 5)

# a = lambda x: x*2
# print(a((1,2)))            #(1, 2, 1, 2)

# 6)

# def display(*args):
#     print(args)
#
# display(a=1, b=2)              # Type error

# 7)

# def spam()->int:
#     return "hai"
#
# print(spam())  # hai

# 8)

# d = {"java":4, "python":6, "perl":4, "c++": 1, "ruby":4}
# print(sorted(d))         #['c++', 'java', 'perl', 'python', 'ruby']

# 9)

# a, *z, b = (1,2,3,4)
# print(a, z, b)             ####  1 [2, 3] 4

# 10)

# d = {"one": 1, "Two": 2, "three": 3, "four": 4}
# for item in d:
#     print(item, end=" ")                 ###  one Two three four

# 11)





