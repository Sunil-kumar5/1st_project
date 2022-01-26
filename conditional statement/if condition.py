# # '''wap to check if the given input is even'''
# # a = int(input("enter the string: "))
# # if a % 2 == 0:
# #     print("number is even")
# # else:
# #     # print("number not even")
#
# # """check for lowercase"""
# # char = input("enter a character")
# # if "a" <= char <= "z":
# #     print(f"{char} is lowercase character")
# char = input("enter a character")
# if char.islower():
#     print(f"{char} is lowercase character")
char = "a"
d = {}
if char.lower() in "aeiou":
    d[char] = ord(char)
    print(d)