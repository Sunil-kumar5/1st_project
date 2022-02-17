""""""

# l = [2,3,4,5,6]
# res = []
# for item in enumerate(l):
#     res.append(item)
# print(res)


""""""
# l = [1,2,3,4,5,6,7,8]
# res = []
# for item in l:
#     if item % 2 == 0:
#         res.append(item)
# print(res)


# l = [1,2,3,4,5,6,7,8]
# even = [i for i in l if i % 2 == 0]



"""wap to create a list using the following"""
# l = ["python", 'java', "name", "exe","sunil"]
# res = []
# for i in l:
#     if len(i) % 2 == 0:
#         res.append(i)
#     else:
#         res.append(i[::-1])
# print(res)
#
# #comprehension
# res = [i if len(i) % 2 == 0 else i[::-1] for i in l]
# print(res)

"""wap to create a list from the following list  if elements is are of type string keep them as it is else reverse it"""
# l = ["python", 'java', "name", "exe","sunil",10, True,1.4]
# res = []
# for i in l:
#     if isinstance(i,str):
#         res.append(i[::-1])
#     else:
#         res.append(i)
# print(res)
#
#
# # comprehension
# res = [i[::-1]if isinstance(i,str)else i for i in l]
# print(res)


# l = ["python", 'java', "name", "exe","sunil",10, True,1.4]
# res = []
# for i in l:
#     if not isinstance(i,str):
#         res.append(str(i)[::-1])
#     else:
#         res.append(i)
# print(res)
#
#
# # comprehension
# res = [str(i)[::-1]if not isinstance(i,str)else i for i in l]
# print(res)

""""wap list comprehension to create a list with a string start with a vowles"""
# l = ["amaron", "flipkart","walmart","gmail","aeiou"]
# res = [


# l = ["python", 'java', "name", "exe","sunil",10, True,1.4]
# res = {(index, item) for index,item in enumerate(l)}
# print(res)


# files = ("python", 'java', "name", "exe","sunil")
# res = {(item,len(item)) for item in files}
# print(res)


#dict_

# str_ = "wap list comprehension to create a list with a"
# a = list(str_)
# d ={}
# d1 = {i:a.count(i) for i in a}
# print(d1)


""""""
# s = ["and",1,2,4,"kjnljl"]
# d = {}
# for index,item in enumerate(s):
#     if isinstance(item,str):
#         d[index] = item[::-1]
#     else:
#         d[index] = item
#
# print(d)

#comprehenction
# d1 = {index:item[::-1] if isinstance(item,str) else item for index,item in enumerate(s)}
# print(d1)

"""wap to create a dictionary of char and its ascii value"""
# st = "hii "
# d1 = {char:ord(char) for char in st}
# print(d1)

