# even = lambda num: num % 2 == 0
# print(even(6))
#
# """"""
# multi = lambda a,b: a * b
# print(multi(3,4))
""" return last element in a sequense"""
# str_ = lambda s: s[-1]
# print(str_(s="function"))

# str_ = lambda s: s[-1]
# print(str_([1,2,3,4,5]))


# str_= lambda s: s == s[::-1]
# print(str_("dad"))

l = ["apple","gmail"]
def str_(l):
    for i in l:
        if i[0] in "aeiouAEIOU":
            return [i]

print(str_(l))
