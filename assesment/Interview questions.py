#1) len of iterable
# s = "sunil"
# def _len(iterable):
#     _count = 0
#     for item in s:
#        _count += 1
#     return _count
#
# print(_len("sunil"))
# print(_len([1,2,3,4,5]))

# 2) to reverse the string
# def _reverse(_string):
#     temp = []
#     for item in _string[::-1]:   # for item in range(len(_string)-1,-1,-1)
#         temp += item
#     return ''.join(temp)
#
# print(_reverse("sunill"))

# 3) to replace the string
# s= "hello world"
# res = s.replace("world","universe")
# print(res)

### 4) convert string to list and vice-versa


# def convert_to_string(any_list):
#     return ''.join(any_list)
#
# def convert_to_list(any_string):
#     return any_string.split()
# #
# print(convert_to_string(['1','2','3','4']))    # 1234
# print(convert_to_list("sunil"))        # ['sunil']


### 5) make comma saperated string
#
# s = "hello am sunil kumar"
# temp = s.split()           # ['hello', 'am', 'sunil', 'kumar']
# res = ','.join(temp)
# print(res)                 ## hello,am,sunil,kumar


### 6)  print alternative character in a string

# s = 'hello world'
# print(s[::2])        # hlowrd

# By slicing
# res = [s[i] for i in range(len(s)) if i % 2 == 0]
# print(''.join(res))

 ####### Using loop

# for i in range(len(s)):
#     if i % 2 == 0:
#         print(s[i],end="")

### 7) print ascii values

# s = 'sunil'
# for char in s:
#     _list = ord(char)     # 115 , 117 , 110 , 105 , 108 ,

##############
# s = "sunil"     ## print ascii value amd there sum
# res = [ord(i) for i in s]
# print(sum(res))
################

### 8) convert upper to lower
#
# def _convert(any_string):
#     res = []
#     for c in any_string:
#         if "a" <= c <= "z":
#             res.append(chr(ord(c)-32))
#     return ''.join(res)
#
# print(_convert("sunil"))

##########
# s = "SUNIL"
# res = [chr(ord(i)+32) for i in s]
# print(''.join(res))
####################

# 9) write program to swap two numbers without using 3rd variable

# a = 10
# b = 20
# b,a = a, b
# print(a)
# print(b)
#################

# 10) write program to merge two different lists,

# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b]
# print(c)
# print(a+b)
####################

# 11) program to read a random line in a file (ex = 50,65 78th line)

from itertools import islice


# def read_random_line(line_no):
#     with open("the path") as f:
#         line = islice(f,line_no, line_no+1)
#         return list(line)
# print(read_random_line(2))
####################

# 12) Write program to read a random lines
# in a file. (ex. I want read all lines 10th to 15th line)

# from itertools import islice
# def read_n_lines(start_line,end_line):
#     with open("path") as f:
#         s = islice(f,start_line,end_line)
#         for line in s:
#             print(line)
# print(read_n_lines(10,15))
####################

#13) Program to print last "N" lines of a file.

# from collections import deque
# def tail(n):
#     with open('sample.txt') as f:
#         d = deque(f,n)
#         return d           # only last n lines
# print(tail(4))

# 14)Write a program to check if the given string is Palindrome or not without
# using reversed method.

# def palindrome(any_string):
#     rev = any_string[::-1]
#     if any_string == rev:
#         return True
#     else:
#         return False
#
# print(palindrome("dad"))
####################

#15) Write a program to search for a
# character in a given string and return the corresponding index.

# def search_chr(string,key):
#     for index,char in enumerate(string):
#         if char == key:
#             print(f'character {char} is at {index} index')
#
# print(search_chr("hello world", "w"))
########################

# 16) Write a program to get the below output
#
# sentence = "hello world welcome to python programming hi there"
# d = {'h': ['hello', 'hi'],
# 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }

# from collections import defaultdict
# d = defaultdict(list)
# words = sentence.split()
# for word in words:
#     d[word[0]].append(word)
# print(d)
#################

## 17) Write a to replace all the characters with - if the
# character occurs more than once in a string

# srt_ = "hellohai"
# res = ''.join(['_' if srt_.count(i) > 1 else i for i in srt_]) #['_', 'e', '_', '_', 'o', '_', 'a', 'i']
# print(res)         ## _e__o_ai
################

# 18) write a decorator that returns only positive values of subtraction

# def positive(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args,**kwargs)
#         return abs(result)
#     return wrapper
#
# @positive
# def add(a,b):
#     return a+b
# print(add(-80,7))
##################

# 19) How to get the count of number of instances of a class that is being created.

# class Login:
#     login_count = 0
#     def __init__(self):
#         Login.login_count += 1
#
# _1 = Login()
# _2 = Login()
# print(Login.login_count)
#####################

# 20) Write a function which takes a list of strings and integers.
# If the item is a string it should print as is and if the
# item is integer of float it should reverse it.

# list_ = ["sunil", "kumar", 'reverse', 256, 67, 89, 96]

#list comprension
# res = [item if isinstance(item, str) else str(item)[::-1] for item in list_]
# print(res)

#in function

# def spam(items):
#     for item in items:
#         if isinstance(item, str):
#             print(item)
#         else:
#             print(str(item)[::-1])
#
# print(spam(list_))
###################

# 21) Write a class named Simple and it should have iteration capability.

# class Simple:
#     def __init__(self, items):
#         self._items = items
#     def __iter__(self):
#         return iter(self._items)

# s = Simple([2,3,4,5,5])
# for i in s:
#     print(i)
######################

# 22) Write a Custom class which can access the
# values of dictionaries using d['a'] and d.a

# class mydict:
#     def __init__(self, d):
#         self.__dict__.update(d)
#     def __getitem__(self, item):
#         return self.__dict__[item]
# d = mydict({'a': 1, 'f': 4})
# print(d['a'])
# print(d.f)
###################3

# 23) Write a python program to get the below output
#
# sentence = "Hi How are you"
# o/p should be "iH woH era uoy"

# words = sentence.split()
# print(words)
# res = " ".join([item[::-1] for item in words])
# print(res)
################

#24) Write a python program to get the below output

# sentence = "Hi How are you"
# o/p should be "ouy era woH iH"

# res = sentence[::-1]
# print(res)
###############3

# 25) Write a lambda function to add two numbers (a, b)

# add = lambda a,b: a + b
#
# print(add(6,8))
######################

#26) What is the output of the following

# a = [1, 2, 3]
# b = [4, 5, 6]
# print([a, b])        ## [[1, 2, 3], [4, 5, 6]]
# print((a, b))        ## ([1, 2, 3], [4, 5, 6])

#################33

# 27) How to remove duplicates from the list without using inbuilt functions

# l = [1,2,3,4,2,5,4,2]
# res = [item for item in l if l.count(item) == 1]
# print(res)       ### [1, 3, 5]
###################

# 28) Find the longest word in the sentence

# sentence = "Hello world. Welcome to Python"
# words = sentence.split()
# d = {word: len(word) for word in words}
# res = max(d.items(), key=lambda item: item[-1])
# print(res)         #### ('Welcome', 7)

# max_len = 0
# max_word = ''
# for word in words:
#     if len(word) > max_len:
#         max_len = len(word)
#         max_word = word
# print(max_len,max_word)       ## 7 Welcome

# res = max(sentence.split(),key=len)
# print(res,len(res))               ## Welcome 7
################

# 29) write a program to reverse the values in the dictionary if the value
# is of type String
#
# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
#
# res = {key: value[::-1] if isinstance(value,str) else value for key,value in d.items()}
# print(res)
####################

# 31) How to get the elements that are in list b but not in list a
#
# a = [1, 2, 3, 2]
# b = [1, 2, 3, 4, 2]
# set_a = set(a)
# set_b = set(b)   ### {1, 2, 3, 4}
# print(set_b.difference(set_a))          ### {4}
#####
# for item in b:
#     if item not in a:
#         print(item)      ## 4

##################

# 32) A function takes variable number of positional
# arguments as input. How to check if the arguments that are passed are more than 5

# def spam(*args):
#     if len(args) > 5:
#         print('length of argumarnt passed greater than 5')
#     else:
#         print('length argument passed less then 5')
#
# print(spam(1,2,3,4,5,6,7))
####################

# 33) Count the number of occurrences of "CRITICAL", "INFO"
# and "ERROR" lines in a log file.
# lines = """CRITICAL:Hello world
# INFO: This is an info\
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical"""
# from collections import defaultdict
# _errors = defaultdict(int)
# for line in lines.split('\n'):
#     error_type, other = line.strip().split(':')
#     _errors[error_type] += 1
# print(_errors)
###################
# 34) Write a function to reverse any iterable without using reverse function.
# a = [1,2,3,4,5]
# _reverse = []
# for i in range(len(a)-1,-1,-1):
#     _reverse.append(a[i])
# print(_reverse)
###################
#36) Sum all the numbers in the below string.
# s = "Sony12India567Pvt2ltd"
# import re
# r = re.findall(r'[\d]',s)
# #print(r)   ## ['1', '2', '5', '6', '7', '2']
# sum_ = 0
# for item in r:
#     sum_ += int(item)
# print(sum_)
#################

#37) Write a program to sum all the numbers in below string.
# s = "Sony12India567Pvt2ltd" # eg.12+567+2
# import re
# r = re.findall('[\d]+',s)
# # print(r)   ### ['12', '567', '2']
# sum_ = 0
# for item in r:
#     sum_ += int(item)
# print(sum_)
###################
#38) Print all the numbers in the below list

# a = ['abc', '123', 'hello', '23','5546dd','5p']
# for item in a:
#     if item.isnumeric():
#         print(item)
######## OR ##########
# for item in a:
#     for i in item:
#         if '0' <= i <= '9':
#             pass
#         else:
#             break
#     else:
#         print(item)
###############
# 42) Write a program to get square of list of number's using lambda function
# a = [1,2,3,4,5,6]
# sqr = lambda num: num ** 2
# b = [sqr(item) for item in a]
# print(b)
################

 # 43)Write a function that accepts two strings and returns
# True if the two strings are anagrams of each other.
# def is_anagram(str1,str2):
#     if str1.upper() == str2.upper():
#         return False
#     s_str1 = sorted(str1.upper())
#     s_str2 = sorted(str1.upper())
#     if s_str1 == s_str2:
#         return True
#     else:
#         False
#
# print(is_anagram('ate', 'eat'))
# print(is_anagram('racecar', 'racecar'))
##############

#46) Write a program which squares the numbers in a list using map object
# a = [1,2,3,4,5]
# def squares(item):
#     return item ** 2
# m = map(squares,a)
# for item in m:
#     print(item)
######## OR ########
# m = map(lambda item: item ** 2,a)
# for item in m:
#     print(item)
#########################
# 49) Write a Program to print the sum of entire list and sum of only internal list
# l = [[1,2,3],[4,5,6],[7,8,9]]
# internal_sum = [sum(item) for item in l]
# print(internal_sum)   ## [6, 15, 24]
# print(sum(internal_sum))  ## 45
#######
# total = [each_item for each_internal_list in l for each_item in each_internal_list]
# print(sum(total))
#########################
# 54) Grouping anagrams.
# from collections import defaultdict
# words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
# d = defaultdict(list)
# for word in words:
#     s = ''.join(sorted(word))
#     d[s].append(word)
# print(d) ## {'aet': ['eat', 'ate', 'tea'], 'ehllo': ['hello'], 'eilnst': ['silent', 'listen']})
########################
# 62) Write a program to count the number occurrences of
# each item in the list without using any inbuilt functions
# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# res = {item: names.count(item) for item in names}
# print(res)
##### OR ###########
# unique_items = set(names)
# d = {}
# for item in unique_items:
#     count_ = 0
#     for name in names:
#         if item == name:
#             count_ += 1
#     d[item] = count_
# print(d)
#################
# 63) Write a function to check if the number is Prime
# def is_prime(number):
#     return any([number % 2 != 0 for i in range(2, number)])
# print(is_prime(89))
###################
# 65) Write a program to find the largest number in the list
# without using any inbuilt funct
# numbers = [100, 20, 30, 40, 50]
# largest = 0
# for item in numbers:
#     if item > largest:
#         largest = item
# print(largest)
###################
# 66) get last digit in number
# def get_last_digit(number):
#     temp = str(number)
#     return int(temp[-1])
# print(get_last_digit(2678))
###################

#67) Write a program to find most common words in a given list.

# words = [
# 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
# 'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
# ]

# d = {item: words.count(item) for item in words}
# common_ = sorted(d.items(), key= lambda item: item[-1])
# print(common_[-1])
###### OR #######
# from collections import Counter
# c = Counter(words)
# print(c)
##################
# 68) Make a function named tail that takes a sequence (like a list, string, or tuple)
# and a number n and returns the last n elements from the given sequence, as a list.

# def tail(iterable,n):
#     if not isinstance(n,int):
#         raise TypeError('value of n should be positive Integer')
#     if n <= 0:
#         return []
#     return list(iterable)[-n:]
# print(tail([3,4,5,6,3,2,45,1,1,1,1],4))
# print(tail('sunil56',2))
###################
#70) Write a program to get all the duplicate
#items and the number of times the item is repeated in the list.
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
# res = {item: names.count(item) for item in names if names.count(item) > 1}
# print(res)
###################
#1)
# @
# @ @
# @ @ @
# @ @ @ @
# for row in range(4):
#     for col in range(row+1):
#         print("@",end=" ")
#     print()
######## OR ########
# for row in range(1,5):
#     print('@ ' * row)
###############
      #
    # #
  # # #
# # # #
# for row in range(1,5):
#     print(f'{"# " * row:>8}')
###############
#    *
#   * *
#  * * *
# * * * *
# for row in range(1,5):
#     print(f'{"* " * row:^8}')
###############
# * * * *
# * * *
# * *
# *
# for row in range(4,0,-1):
#     print("* " * row)
################

# * * * *
#   * * *
#     * *
#       *
# for row in range(4,0,-1):
#     print(f'{"* " * row:>8}')
################
# * * * *
#  * * *
#   * *
#    *
# for row in range(4,0,-1):
#     print(f'{"* " * row:^8}')
###############
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# for row in range(1,5):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()
###############
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# for row in range(4,0,-1):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()
################
# a
# a b
# a b c
# a b c d
# for row in range(ord("a"),ord("d")+1):
#     for col in range(ord("a"),row+1):
#         print(chr(col),end=" ")
#     print()
### OR #####
# x = ""
# for row in range(ord("a"),ord("d")+1):
#     x += chr(row)+ " "
#     print(x)

################
# * * * * * *
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *
# for i in range(6,0,-1):
#     print(f"{'* ' * i:>12}")
# ###############
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# for i in range(6,0,-1):
#      print(f"{'* ' * i:<6}")
#############
#77) Write a program to rotate items of the list

# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
# def rotate(iterable, n):
#     for _ in range(n):
#         f = iterable.pop()
#         iterable.insert(0, f)
#     return iterable
# print(rotate(names,2))
################

#78) Write a program to rotate characters in a string
# def rot_str(string,n):
#     string = list(string)
#     for _ in range(n):
#         f = string.pop()
#         string.insert(0, f)
#     return ''.join(string)
# print(rot_str("sunil56",2))     # 56sunil
#################
#79) Write a program to count the number of white spaces in a given string
# import re
# sentence = """Hello world welcome to Python Hi  How are you. Hi how are you"""
# space = re.findall(r'\s',sentence)
# print(len(space))
######################

#87) Write a program to count no of capital letters in a string
# sentence = "Hi How are You WelCome to PytHon"
# from collections import defaultdict
# cap_letters = defaultdict(int)
# for c in sentence:
#     if "A" <= c <= "Z":
#         cap_letters[c] += 1
# print(cap_letters)
#####################

#88) Write a program to get the below output
# for i in range(1, 5):
#     print('* '*1)
#     j = i + 1
#     print('* '*j)
#
# *
# * *
# *
# * * *
# *
# * * * *
# *
# * * * * *

# 89)
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(0, len(a), 2):
#     print(a[i:i+2])
# # o/p
# [1, 2]
# [3, 4]
# [5, 6]
# [7, 8]
# [9]
####################
# 90) To check the series or not
# a = [10, 12, 14, 16, 18]
# b = [20, 22, 24, 26, 28]
# def _series(iter1, iter2):
#     diff = a[1] - a[0]
#     c = iter1 + iter2
#     return all([True if c[i] + diff == c[i+1] else False for i in range(0,len(c)-1)]
#####################
#Write a program to count the number of occurrences of non-special characters in a
# given string

# s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
# from collections import defaultdict
# d = defaultdict(int)
# for c in s:
#     if c.isalnum():
#         d[c] += 1
# print(d)
##### or #######
# import re
# chre = re.findall(r'\w',s)
# res = {c: chre.count(c) for c in chre}
# print(res)
###############
#98) Grouping Flowers and Animals in the below list
# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
# from collections import defaultdict
# d = defaultdict(list)
# for item in items:
#     name,character = item.split('-')
#     d[character] += [name]
# print(d)
#############
#99) Grouping files with same extensions
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
# from collections import defaultdict
# d = defaultdict(list)
# for file in files:
#     name,ext = file.split('.')
#     d[ext].append(name)
# print(d)
##############
#100) Filter only those characters except digits

# s = '@hello12world34welcome!123'
# import re
# res = re.findall(r'\D',s)
# print(''.join(res))        ### @helloworldwelcome!
# ### Math only  numbers
# res = re.findall(r'[^\D]',s)
# print(''.join(res))        ## 1234123
###############
#101) Count number of words in a sentence. ignore special characters.

# sentence = "Hi there! How are you:) How are you doing today!"
# import re
# words = re.findall(r'\b\w+',sentence)
# # print(words) # ['Hi', 'there', 'How', 'are', 'you', 'How', 'are', 'you', 'doing', 'today']
# from collections import defaultdict
# d = defaultdict(int)
# for word in words:
#     d[word] += 1
# print(d) # {'Hi': 1, 'there': 1, 'How': 2, 'are': 2, 'you': 2, 'doing': 1, 'today': 1})
# #### OR ####
# from collections import Counter
# c = Counter(words)
# print(c) # ({'How': 2, 'are': 2, 'you': 2, 'Hi': 1, 'there': 1, 'doing': 1, 'today': 1})
###############
#104) Find all max length words from the below sentence

# sentence = "hello world hi apple you yahoo to you"
# max_len_word = max(sentence.split(),key=len)
# max_len_words = [word for word in sentence.split() if len(word)== len(max_len_word)]
# print(max_len_words)
###############

#105) Find the range from the following string

# sentence = '0-0, 4-8, 20-20, 43-45'
# words = sentence.split(',')
# # print(words)   # ['0-0', ' 4-8', ' 20-20', ' 43-45']
# _range =[]
# for word in words:
#     start,end = word.split('-')
#     for i in range(int(start),int(end)+1):
#         _range.append(i)
# print(_range)  # [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
####################
#121) Write a program to remove duplicates from the list without using set or empty list
# l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]
# l2 = l1[::]
# for item in l2:
#     if l1.count(item) > 1:
#         l1.remove(item)
# print(l1)












#############################################################################
# class Simple:
#     def __init__(self, items):
#         self._items = items
#
#     def __iter__(self):
#         return iter(self._items)
#
#
# s = Simple([1, 2, 3, 4, 5])
# s1 = [1, 2, 3, 4, 5]
#
# for item in s:
#     print(item)
#
# print((type(s)))
# print((type(s1)))

## to fetch only duplicate items

# s = [1, 2, 5, 6, 4, 2, 6, 9, 5, 4]
# res = []
# for i in s:
#     if s.count(i) > 1:
#         res.append(i)
# print(list(set(res)))

######################
# res = []
# _res = []
# for i in s:
#     if i not in res:
#         res.append(i)
#     else:
#         _res.append(i)
# print(res)
# print(_res)

# n = int(10)
# a = 0
# b = 1
# sum = 0
# count = 1
# print("Fibonacci Series:",end="")
# while(count <= n):
#     print(sum,end=" ")
#     count += 1
#     a = b
#     b = sum
#     sum = a + b
##
# sum = 0
# for i in range(0,15):
#     sum += i
# print(sum)
#####

# s= "sunil"
# for i in s:
