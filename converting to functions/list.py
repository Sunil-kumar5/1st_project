
""" traversing through list """
# l = ["python", 10, 3.2, "selenium", "Java"]
# def list_(l):
#     l1 = []
#     for item in l:
#         l1.append(item)
#     return l1
#
# print(list_(l))
#comprehension
# s = [i for i in l]
# print(s)


""" print index and its corresponding item in the list """
# l = ["python", 10, 3.2, "selenium", "Java"]
# def list_(l):
#     l1 = []
#     for index,item in enumerate(l):
#         l1.append((index,item))
#     return l1
#
# print(list_(l))

#comprehension

# s = [(index,item) for index,item in enumerate(l)]
# print(s)

""" traversing through a list in reversed order """

# l = ["python", 10, 3.2, "selenium", "Java"]
# def res_(l):
#     l1 = []
#     for i in l[::-1]:
#         l1.append(i)
#     return l1
#
# print(res_(l))

#comprehension

# s = [item for item in l[::-1]]
# print(s)

""" print even indexed elements in the list """

# l = ["python", 10, 3.2, "selenium", "Java"]
# def even_(l):
#     l1 = []
#     for i in l[::2]:
#         l1.append(i)
#     return l1
#
#
# print(even_(l))

#comprehension

# s = [item for item in l[::2]]
# print(s)

""" print integers in a list """

# l = ["python", 10, 3.2,23,45,67,56, "selenium", "Java"]
# def int_(l):
#     l1 = []
#     for i in l:
#         if isinstance(i,int):
#             l1.append(i)
#     return l1
#
#
# print(int_(l))

#comprehension

# s = [item for item in l if isinstance(item,int)]
# print(s)


""" print only numeric datatypes"""

# l = ["python", 10, 3.2,3+3j,56,54, "selenium", "Java"]
# def numeric_(l):
#     l1 = []
#     for i in l:
#         if isinstance(i,(int,complex,float)):
#             l1.append(i)
#     return l1
#
#
# print(numeric_(l))

# comp
# s = [item for item in l if isinstance(item,(int,float,complex))]
# print(s)

""" print length of each string in the list """

# l = ["python", "Node JS",56, "selenium", "Java"]
# def len_srt(l):
#     l1 = []
#     for i in l:
#         if isinstance(i,str):
#             l1.append((i,len(i)))
#     return l1
#
#
# print(len_srt(l))

#comp
# s = [(item,len(item)) for item in l if isinstance(item,str)]
# print(s)

""" print the strings with even length """

# l = ["python", "Node JS",45,67, "selenium","suni", "Java"]
# def even_len(l):
#     l1 = []
#     for i in l:
#         if isinstance(i,str):
#             if len(i) % 2 == 0:
#                 l1.append((i,len(i)))
#     return l1
#
#
# print(even_len(l))

#comp

# s = [item for item in l if isinstance(item,str) if len(item) % 2 == 0]
# print(s)

""" reverse string elements or else keep it as it is"""

# list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]
# def res_(list_):
#     res =[]
#     for i in list_:
#         if isinstance(i,str):
#             res.append(i[::-1])
#         else:
#             res.append(i)
#     return res
#
#
# print(res_(list_))

#comp
# s = [item[::-1] if isinstance(item,str) else item for item in list_]
# print(s)


""" print if the element is starting with vowel """

# files = ["Amazon", "flipkart", "walmart", "email", "yahoo"]
# def vowles_(files):
#     ele = []
#     for i in files:
#         if i[0] in "aeiouAEIOU":
#             ele.append(i)
#     return ele
# print(vowles_(files))

#comp
# s = [item for item in files if item[0].lower() in "aeiou"]
# print(s)

""" print all the extensions in the following list """

# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]
# def ext_(files):
#     l = []
#     for i in files:
#         a = i.split(".")
#         l.append(a[1])
#     return l
#
#
# print(ext_(files))

#comp
# s = [i.split(".")[1] for i in files]
# print(s)


""""""
s = "hello word"
# d = {}
# for char in s:
#     d[char] = s.count(char)
# print(d)
#
# res = {char:s.count(char) for char in s}
# print(res)

# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)


# s = "hello"
# def ascii_(char):
#     return char,ord(char)
#
# res = map(ascii_,s)
# print(list(res))


"""wap to print index and item pair where item is string and starting vowles"""
# list_ = ["Aython", 17, 9, "java", 19.9, 4+0j, "ruby", "e++"]
# res = {index: item for index, item in enumerate(list_) if isinstance(item, str) if item[0] in "aeiou"}
# print(res)


list_ = ["name","bike","car"]
# res = list(map(list,list_))
# print(res)

# #normal method
# l1 = []
# for i in list_:
#     l1.append([i])
# print(l1)

# a = [1,2,3,4,5]
# nums = lambda num : num ** 2
# res = list(map(nums,a))
# print(list(res))


# d = [1,2,3,4,5,6,7,8,9,10]
# def index_(num):
#     for index,item in enumerate(d):
#         if index % 2 == 0:
#             return item ** 2
#
# res = list(filter(index_,d))
# print(list(map(index_,res)))


# ind = lambda num: (num ** 2) if d.index(num) % 2 == 0 else None
#
# res = list(filter(ind,d))
# print(list(map(ind,res)))

"""to delete set of keys"""
# animals = {"name":"dog","age":"4","weight":"5","country":"us","city":"cali"}
# res = {key:animals[key] for key in animals.keys() - ["name","age"]}
# print(res)

# s = "hello  word"
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
#
# print(d)

# s = ["apple", "apple", "dd","jkjgkj","apple"]
# d = {}
# for index, item in enumerate(s):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item] += [index]
# print(d)