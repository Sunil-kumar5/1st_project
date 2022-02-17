
""""""
# def num_(start, end):
#     if start < end:
#         return
#     print(start)
#     num_(start-1,end)
#
#
# num_(10,1)


"""program to add the digits of a number"""
# def num_(n):
#     a = str(n)
#     count = 0
#     if i in a:
#         count += int(i)
#         print(count)
#     return
#
#
# num_(56)
#
# print()


# num =56
# count = 0
# a = str(num)
# for i in a:
#     count += int(i)
# print(count)


# num = 12367
# sum = 0
# while num > 0:
#     last = num % 10
#     sum += last
#     num = num//10
# print(sum)
#
# def num(n):
#     if n > 0:
#         last = num % 10
#         sum += last
#         num =

"""to count the digits in the number"""
# def sum_(n,sum=0):
#     if n > 0:
#         n = n//10
#         sum += 1
#         return sum_(n,sum)
#     else:
#         return sum
#
#
# print(sum_(3456))

""" reverse a string"""
# def str_(s,i=0,res=""):
#     if i < len(s):
#         res = s[i] + res
#         return str_(s,i+1,res)
#     return res
#
#
# print(str_("haiii"))
