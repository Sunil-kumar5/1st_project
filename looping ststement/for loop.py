# """1 to 10"""
# for num in range(1,11):
#     print(num)
#
# """10 to 1"""
# for num in range(10,0,-1):
#     print(num)

# """-1 to-10"""
# for num in range(-1,-11,-1):
#     print(num)
#
# """-10 to -1"""
# for num in range(-10,0):
#     print(num)

# """even numbers from 1 to 10"""
# for num in range(1,11):
#     if num % 2 == 0:
#         print(num)

# """travelsing through a string"""
# string = "sunil"
# for chr in range(len(string)):
#     print(string[chr])
# string = "sunil"
# for char in string:
#     print(char, end=" ")
#
# """travelsing through list"""
# list_ = [2,4,6,8]
# for item in range(len(list_)):
#     print(list_[item])
#
# """travelsing through tuple"""
# num = (3,2,3,1,4)
# for item in range(len(num)):
#     print(num[item], end=" ")
# print()
# for ele in num:
#     print(ele, end= " ")

# """travelsing through set"""
# set_ = {"hii", "bye", "good", "bad"}
# for ele in set_:
#     print(ele, end=" ")
#
# """travelsing through dictionary"""
# h = {"one":1, "two":2, "three":3}
# for key in h:
#     print(key, h[key], sep="-->")
#
"""wap to print index and the element in a string"""
s = "hello"
# for item in range(len(s)):
#     print(item, s[item])
#
# for item in enumerate(s):
#     print(item)

# for item in enumerate(s):
#     print(item[0], item[1])

# """wap to traverse through a string in reverse ordee"""
# string = "baby"
# for item in range(len(string)-1,-1,-1):
#     print(string[item],end=" ")
# print()
# for char in  string[::-1]:
#     print(char,end=" ")
# print()
#
# for item in reversed(string):
#     print(item, end=" ")

# """wap to count the number of character present in a string"""
# string = "sunil"
# count = 0
# for item in string:
#     count += 1
# print(count)

# string = "sunil"
# count = 0
# for_ in string:
#     count += 1
# print(count)

# """wap to print index character in the string"""
# string = "good moring"
# for item in range(0,len(string),2):
#     print(string[item])
#
# for ele in string[::2]

# """wap to print the digit in string"""
# s = "djk2551512"
# for char in s:
#     if "0" <= char <="9":
#     # if char.isdigit():
#         print(char,end=" ")
#
# s = "djk2551512"
# count = 0
# for char in s:
#     if char.isdigit():
#         count += 1
# print(count)

# a = []
# b = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
# for i in range(4):
#     a.append([row[i] for row in b])
# print(a)
# o/p [[0,4,8],[1,5,9],[2,6,10],[3,7,11]]



