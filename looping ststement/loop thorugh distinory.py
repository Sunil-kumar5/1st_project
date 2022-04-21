"""wap to print keys in a distinory"""
# s = {"a": 1, "b": 2,"c": 3,"d": 4}
# #traversing through dict directly
# for key in s:
#     print(key,end=" ")
# print()
# for key in s.keys():
#     print(key,end=" ")
# print()
#
# for key,value in s.items():
#     print(key,end=" ")

"""wap to print only the values from the dictonary"""
#s = {"a": 1, "b": 2,"c": 3,"d": 4}
# for key in s:
#     print(s[key],end=" ")
#
# #get method
#
# for key in s:
#     print(s.get(key),end=" ")
#
#s.values
# for value in s.values():
#     print(value,end=" ")
#
# #s.items
# for key,value in s.items():
#     print(value,end=" ")
#
"""print items along with their indices"""
# for  s.items()
#

"""hjg"""
string = "hello world"
# d = {}
# for i in string:
#     count = 0
#     for j in string:
#         if i == j:
#             count += 1
#     d[i] = count
# print(d)

# d = {}
# for char in string:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
# print(d)


"""wap to create a distionary with words and its count pAIR"""
# s = "python is a language, pythomn programming is easy"
#
#       #by using inbuilt function
#
# string = s.split()
# d = {}
# for item in string:
#     d[item] = string.count(item)
# print(d)

      # with out using inbuilt method

# d = {}
# for item in string:
#     if item not in d:
#         d[item] = 1
#     else:
#         d[item] += 1
# print(d)

# d = {}
# for i in string:
#     count = 0
#     for j in string:
#         if i == j:
#             count += 1
#     d[i] = count
# print(d)


       # by using defaultdict method

# from collections import defaultdict
# s = "python is a language, pythomn programming is easy"
# string_ = s.split()
# dd = defaultdict(int)
# print(dd)
# for char in string_:
#     dd[char] += 1
# print(dd)

"""wap to create a dictionary with word and its length"""
# s = "python is a language, pythomn programming is easy"
# string = s.split()
# d = {}
# for item in string:
#     d[item] = len(item)
# print(d)
"""wap to create a dictionary with world and its lenght pair only if the world is of even length"""
# s = "python is a language, pythomn programming is easy"
# string = s.split()
# d = {}
# for item in string:
#     if len(item) % 2 == 0:
#         d[item] = len(item)
# print(d)

"""wap t create a dictionary with word and its length pair , only if the world is starting with vowles"""
#s = "python is a language, python programming is easy"
# string = s.split()
# d = {}
# for item in string:
#     if item[0] in "aeoiuAEIOU":
#         d[item] = len(item)
# print(d)

"""wap to create a dictionary word and its count if word is not repeated."""
# s = "python is a language, python programming is easy"
# list_ = s.split()
# d = {}
# for word in list_:
#     if list_.count(word) == 1:
#         d[word] = list_.count(word)
# print(d)
#
# list_ = s.split()
# d = {}
# for word in list_:
#     if list_.count(word) > 1:
#         pass
#     else:
#         d[word] = list_.count(word)
# print(d)

"""wap"""

# names = ["apple", "google", "gmail", "apple","gmail","google"]
# d = {}
# for name in names:
#     count = names.count(name)
#     if count > 1:
#         d[name] = count
# print(d)


"""wap to get the following output"""

# s = " hello world welcome to python programming hi there"
# #
# from collections import defaultdict
# #
# list_ = s.split()
# dd = defaultdict(list)
# #
# for word in list_:
#     #dd[word[0]] += [word]
#     dd[word[0]].append(word)
# print(dd)

"""wap to create the dictionary with element and its index pair in the given list"""

     #normal dictionary

names = ["apple", "google", "gmail", "apple","gmail","google","firefox"]
# d = {}
# for index, value in enumerate(names):
#     if value not in d:
#         d[value] = [index]
#     else:
#         d[value] += [index]
# print(d)

# using defaultdict

# from collections import defaultdict
# dd = defaultdict(list)
# for index,item in enumerate(names):
#     dd[item] += [index]
# print(dd)

# s = {"a": 1, "b": 2,"c": 3,"d": 4}
# s1 = {}
# for key in s:
#     value = s[key]
#     s1[value] = key
# print(s1)

#using d.items()
# d2 = {}
# for key,value in s.items():
#     d2[value] = key
# print(d2)


