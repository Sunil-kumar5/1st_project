path = r'C:\Users\Sunil R D\PycharmProjects\1st project\files_directory\txt_log_files\sample.txt'
path1 = r'C:\Users\Sunil R D\PycharmProjects\1st project\files_directory\txt_log_files\sample.log'
path2 = r'C:\Users\Sunil R D\PycharmProjects\1st project\files_directory\txt_log_files\football.txt'
from itertools import islice
from collections import Counter,defaultdict
# with open(path) as f:
#     data = f.read()
#     print(data)
#     print(f.tell())
#     f.seek(0)
#     print(f.read(10))

# with open(path) as file:
#     print(file.readline(10))    # reads 10 characters from the first line
#     print(file.readline(5))     # reads 5 characters after the previous output
#     print(file.readline())      # reads the left out characters in the line


# with open(path) as file:
#     print(file.readlines())
#

""" to print line number and line"""
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         print(count, line)


"""to count number of words in the given file"""

# with open(path) as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         for word in words:
#             count += 1
#     print(count)

# or

# with open(path) as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         count += len(words)
#     print(count)

""" print the lines in revers (last - first)"""
# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)


"""count number of  spaces"""
# with open(path) as file:
#     key = " "
#     count = 0
#     for line in file:
#         for i in line:
#             if i == key:
#                 count += 1
#
#     print(count)



""" number of words starting with vowles"""
# with open(path) as file:
#     count = 0
#     for line in file:
#         for word in line.split():
#             if word[0] in "aeiouAEIOU":
#                 count += 1
#     print(count)

""" create dict of words amnd its count pair"""

# with open(path) as file:
#     d = {}
#     for line in file:
#         for word in line.split():
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word] += 1
#     print(d)

# dd

# from collections import defaultdict
# with open(path) as file:
#     dd = defaultdict(int)
#     for line in file:
#         for item in line.split():
#             dd[item] += 1
#     print(dd)

path_ = r'C:\Users\Sunil R D\PycharmProjects\1st project\files_directory\txt_log_files\access-log.txt'
from collections import Counter

""" to extract all the ip adresses"""

# with open(path_) as file:
#     l = []
#     for line in file:
#         a = line.split("- -")
#         l.append(a[0])
#     # print(l)
# a = Counter(l)
# print(a)
# print(a.most_common(1))


""" to create a dict od ip adress and their count"""
# with open(path_) as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             a = line.split()
#             if a[0] not in d:
#                 d[a[0]] = 1
#             else:
#                 d[a[0]] += 1
#     print(d)


""" to print nth line in a file"""
# n = int(input("enter the number"))
# with open(path_) as file:
#     for line_no,line in enumerate(file,start=1):
#         if line_no == n:
#             print(line)


""" to print 1st n lines"""
# n = 3
# with open(path) as file:
#     res = list(islice(file,0,n))
#     print(res)

"""to print last n line"""
# n = 5
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         file.seek(0)
#     res = list(islice(file,(count-n),count))
#     print(res)


# assignment

""" 1) finding the length of each line in the text file"""

# with open(path) as file:
#     for line in file:
#         print((line,len(line)))

""" 2) extracting messages from sample.log"""

# with open(path1) as file:
#     l = []
#     for line in file:
#         if line.strip():
#             a = line.split()
#             l.append(a[2])
#     print(l)

""" 3) counting number of INFO,WARNING,TRACE message"""
# with open(path1) as file:
#     l = []
#     for line in file:
#         if line.strip():
#             a = line.split()
#             l.append(a[2])
# res = Counter(l)
# for i in res:
#     if i in ("INFO","WARNING","TRACE"):
#         print((i,res[i]),end="")

""" 4) reading countries from football.txt"""

# with open(path2,encoding="UTF_8") as file:
#     for line in file:
#         if line.strip():
#             country = line.split("\t")
#             print(country[1])
#             

""" 5) least and most occurances of the word"""

# d = defaultdict(int)
# with open(path) as file:
#     for line in file:
#         if line.split():
#             words = line.split()
#             for word in words:
#                 d[word] += 1
#
# print(d)
# c = Counter(d)
# most, *rest, least = c.most_common()
# print(most,least)



