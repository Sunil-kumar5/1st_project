import csv

path = r'C:\Users\Sunil R D\PycharmProjects\pythonProject\1st project\files_directory\csv_files\employees.csv'
test_ =r'C:\Users\Sunil R D\PycharmProjects\pythonProject\1st project\files_directory\csv_files\test.csv'
vacci_ =r'C:\Users\Sunil R D\PycharmProjects\1st project\files_directory\csv_files\vaccination_data.csv'
from collections import defaultdict
import os
# with open("example.csv", "w") as csv_:
#     write_obj = csv.writer(csv_)
#     write_obj.writerow(["x","y","z"])


"""program to read all the names in employee.csv file"""
# with open(r'C:\Users\Sunil R D\PycharmProjects\pythonProject\1st project\files_directory\csv_files\employees.csv') as file:
#     read_obj = csv.reader(file)
#     for i in read_obj:
#         print(i[0])

""" to print only the names salaries that are > 70000"""

# with open(path) as file:
#     read_obj = csv.reader(file)
#     next(read_obj)
#     for row in read_obj:
#         if int(row[3]) > 70000:
#             print(row[0],row[3])

""" group male and female employee"""
# with open(path) as file:
#     read_obj = csv.reader(file)
#     d = {"male":[],"female":[]}
#     next(read_obj)
#     for row in read_obj:
#         if row[1] == "male":
#             d["male"] += [row[0]]
#         elif row[1] == "female":
#             d["female"] += [row[0]]
#     print(d)

""" group based on there team"""

# with open(path) as file:
#     r_obj = csv.reader(file)
#     next(r_obj)
#     dd = defaultdict(list)
#     for row in r_obj:
#         dd[row[2]] += [row[0]]
# print(dd)


""" to sort the shares in test.csv file"""
# with open(test_) as file:
#     r_obj = csv.DictReader(file)
#     l = list(r_obj)
#     res = sorted(l,key= lambda d : float(d["price"]))
#     print(list(res))

""" to add all the shares in the text.csv file"""

# with open(test_) as file:
#     r_obj = csv.reader(file)
#     sum = 0
#     next(r_obj)
#     for row in r_obj:
#         sum += int(row[1])
#
# print(sum)


""" 7)a  Total vaccination of the countries"""
# with open(vacci_) as file:
#     r_obj = csv.reader(file)
#     d = {"TOTAL_VACCINATIONS":[]}
#     next(r_obj)
#     for item in r_obj:
#         d["TOTAL_VACCINATIONS"] += [item[5]]
#     print(d)


""" 7)b total vaccination by country"""


# d = {}
# with open(vacci_) as file:
#     r_obj = csv.reader(file)
#     next(r_obj)
#     for row in r_obj:
#          d[row[0]] = row[5]
#     print(d)







