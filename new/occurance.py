# var = "hello happy"
# ch = "h"
# first = var.find(ch)
# print(var.find(ch,first+1))

## to print the occurance of the character
# ch = 'h'
# occ = 2
# c = 0
# for i in range(len(var)):
#     if ch == var[i]:
#         c += 1
#         if occ == c:
#             print(i)
#             break
# palindrome
# s = 'dad'
# temp = s[::-1]
# if temp == s:
#     print("palindrome")
# else:
#     print("not a palindrome")

## print the charachters

# s = 'suunil'
# a = s.replace('u','o')
# print(a)
# ch = 'u'
# for i in s:
#     if i == ch:
#         print(

## remove
# a = "Test yentra"
# for i in a[::2]:
#     print(i,end="")

## remove odd character
# a = "Test yentra"
# for i in a[1::2]:
#     print(i,end="")

## Remove 1st occurance
# a = "Test yentra"
# for i in a[1::]:
#     print(i,end="")

##Reove last occurance
# a = "Test yentra"
# for i in a[:len(a)-1]:
#     print(i,end="")


######################
# s = 'test yantra'
# occurence = 1
# c = 0
# res = ''
# ch = 't'
#
# for i in s:
#     if i == ch:
#         c += 1
#         if occurence != c:
#             res += i
#     else:
#         res += i
# print(res)
#####

# var = 'john is married'
# char = 'i'
# var1 =''
# occur = 2
# index = 0
# c = 0
# for i in range(len(var)):
#     if char == var[i]:
#         c += 1
#         if occur == c:
#             index = i
#             break
# for i in range(len(var)):
#     if i != index:
#         var1 += var[i]
# print(var1)

###
# def sleep_in(weekday, vacation):
#     if weekday == False or vacation== True:
#         return True
#     else


###
# def monkey_trouble(a_smile, b_smile):
#   if a_smile==b_smile:
#     return True
#   return False
# print(monkey_trouble(True,True))
# print(monkey_trouble(True,False))
# ## OR ###
#
# def monkey_trouble(a_smile, b_smile):
#     if (a_smile and b_smile) or (a_smile==False)


#####
# def sum_double(a,b):
#     if a == b:
#         return(a+b)*2
#     else:
#         return a+b
# print(sum_double(4,3))
# print(sum_double(4,4))

##
# def diff(n):
#     if n>21:
#         return abs(n-21)*2
#     return abs(n-21)
# print(diff(10))
# print(diff(24))
# print(diff(19))

##
# def parrot_(talking,hour):
#     if talking and (hour<7 or hour>20):
#         return True
#     else:
#         return False
# print(parrot_(True,7))

### list ###
# 1)Python example to access List Index and Values
# 2)Python example to add two Lists
# 3)Python example for Arithmetic Operations on Lists
# 4)Python example to check List is Empty or Not
# 5)Python example to Clone or Copy a List
# Python program to Count Even and Odd Numbers in a List
# 6)Python program to Count Positive and Negative Numbers in a List
# 7)Python program to Print Largest Number in a List
# 8)Python program to Print Largest and Smallest Number
# 9)Python program to find Length of a List
# 10) difference in two list
# 11)Python List Multiplication Program
# Python program to Print Elements in a List
# 12)Python program to Even Numbers in a List
# 13)Python program to Print Odd List Numbers
# 14)Python program to Print Positive Numbers
# 15)Python program to Print Negative Numbers
# 16)Python program to Put Even and odd Numbers in Separate List
# 17)Python program to Put Positive and Negative Numbers in Separate List
# 18)Python program to Remove Duplicates from List
# 19)Python program to Remove Even Numbers in a List


###
# Positive or Negative number:
# l = [-1,-8,4,5,-6,5,4,0]
# pos = []
# neg = []
# for i in l:
#     if i < 0:
#         neg.append(i)
#     else:
#         pos.append(i)
# print([pos,neg])
# # print(neg)
######################

# Even or Odd number
# l = [1,2,3,4,5,6,43,33,6,55]
# even = []
# odd = []
# for i in l:
#     if isinstance(i,int):
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
# print(even,odd)
#####################

# Sum of First N Natural numbers:
# n = 16
# sum = 0
# for i in range(0,n):
#     sum += i
# print(sum)
####################
# Sum of N natural numbers:
# Sum of numbers in a given range:
# Greatest of two numbers:
# Greatest of the Three numbers:
# Leap year or not:
# Prime number:

##Prime number within a given range:
# for num in range(0,10):
#     if num >1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

# Sum of digits of a number:

# Reverse of a number :
# Palindrome number:
# Armstrong number :
# Armstrong number in a given range :
# Fibonacci Series upto nth term :
# Factorial of a number :
# Power of a number :
# Factor of a number :

#