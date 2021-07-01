
from datetime import date
from datetime import time
from datetime import datetime

# # Question no 1
# print("Hello world")

# def Calc(currency,*rates):
#     for i in rates:
#         print(currency * i)


# rates = [1,2,3]
# currency = 5
# Calc(currency, rates)

# print(Calc(4, 5, 10, 4))


# # Question no 2
# a=1
# b=2
# def func():
#     global b
#     b = a + b
#         # b = b + 1

# func()
# print(b)


# Question 3 of 12
# You have an existing class Simple() that returns the sum of two numbers using its Add(x,y) method.
# How can you leverage it to build another class that calculates the inverse of the sum of two numbers?


# class Simple():
#     def Add(self,x,y):
#         add = x + y
#         # print("X and Y")
#         return add

#     def method2(self):
#         print("ABC")


# class Advanced(Simple):
#     def Inverse(self,x,y):
#         return (1/Simple.Add(self,x,y))

# def main():
#     c = Simple()
#     # print(c.Add(5,5))
#     # c.method2()

#     c2 = Advanced()
#     print(c2.Inverse(5,5))

# if __name__ == "__main__":
#     main()


# This code has three critical issues.
# Which is not actually an issue?


# def main:
#     print(hello!)

# You are correct!
# The function must be defined with the keyword 'func', not 'def'.


# Question 5 of 12
# In Python, what is the correct way to develop a class called Person that has parameters in the initialize function called name, age, and sex?
# You are correct!
# class Person:
#   def __initialize__(self, name, age, sex):
#     self.name = name
#     self.age = age
#     self.sex = sex


# What will the following script print?

# def inc(a,b=1):
#     return(a+b)
# a=inc(1)
# a=inc(a,a)
# print(a)
# You are correct!
# 4


# Question 7 of 12
# You need to set the annual payment in one function and print the respective monthly payment in a separate function. How would you fix the suggested code to work properly?

# def SetAnnual():
#   annual=10000
# def PrintMonthly():
#   print("Your monthly payment is "+annual/12+" USD.")
# SetAnnual()
# PrintMonthly()

# You are correct!
# def SetAnnual():
#   global annual
#   annual=10000
# def PrintMonthly():
#   print("Your monthly payment is "+str(annual/12)+" USD.")
# SetAnnual()
# PrintMonthly()


# Which code snippet can you use to print the number of digits in the number variable? You can assume this number is always positive and always less than 10,000.
# You are correct!
# if (number>=1000):
#   print(4)
# elif (number>=100):
#   print(3)
# elif (number>=10):
#   print(2)
# else:
#   print(1)


# Question 9 of 12
# Which alternative code is logically equivalent to the code below?

# max=x if (x>y) else y
# You are correct!
# max=y
# if (x>y):
#     max=x

# Why is the code below often added to a Python program file?

# if __name__ == "__main__":
#   main()
# You are correct!
# It executes the main() function only if this file is executed as the main program.


# Question 11 of 12
# Which function will return the sum of the first item in the data list and every tenth item after?
# You are correct!
# def Sum10th(data):
#   sum=0
#   for i,d in enumerate(data):
#     if (i % 10 == 0): sum=sum+d
#   return sum


# def main():

# def Sum10th(data):
#         sum = 0


#         for i,d in enumerate(data):
#             if(i % 10 == 0): sum = sum + d
#         return sum


# # if __name__ == "__main__":
# #   main()

# data = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# print(Sum10th(data))


# Question 12 of 12
# Which real-world scenario is best described as a standard while loop?
# You are correct!
# Start reading a book, and stop after reading a certain number of pages.


# Quiz 02


from datetime import datetime


now = datetime.now()


# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month

# print(now.strftime("%d-%b-%Y %H:%M:%S"))
# print(now.strftime("%Y"))
# print(now.strftime("%M"))
# print(now.strftime("%c"))

# Given that now=datetime.now(), which call may produce different results on different computers?
# Answer: print(now.strftime("%c"))

# Which code will you use to generate a date and time output in the following format?
# 13-Mar-2020 16:42:58

# Answer:
# from datetime import datetime
# now=datetime.now()
# print(now.strftime("%d-%b-%Y %H:%M:%S"))

# Question 3 of 5
# What should come instead of the ??? placeholders for this code to correctly print the number of days until your birthday on Jun 30? Hint: the number of days in a timedelta object can be returned using its days attribute.

# today=date.today()
# bday=date(today.year,6,30)
# diff=???
# if diff>0:
#   print("Birthday in %d days" % diff)
# else:
#   print("Birthday in %d days" % (???))
# Answer:
# (bday-today).days; diff+365


# today = date.today()
# bday = date(today.year, 6, 30)
# diff = (bday-today).days
# if diff > 0:
#     print("Birthday in %d days" % diff)
# else:
#     print("Birthday in %d days" % (diff+365))



today = date.today()
# days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
# print("Tomorrow will be "+days[(today.weekday()+1)%7])

# Question 4 of 5
# You create a simple calendar program that needs to print tomorrow's day of the week. Which code will work under all circumstances?
# Answer:
# today=date.today()
# days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# print("Tomorrow will be "+days[(today.weekday()+1)%7])

# print(today)

# today = datetime.date(datetime.now())
# print(today)


# Question 5 of 5
# Which call will return the same result like date.today()?
# Answer:
# datetime.date(datetime.now())



## Quiz 04 ##

# Question 1 of 5
# You need to print the content of the "list.txt" file to the console. Which code can you use, assuming the file must already exist and must not be overwritten or created?
# Answer:
# f=open("list.txt",'r')
# print(f.read())

# Question 2 of 5
# While _____ checks whether a path exists, _____ checks whether a path is a file.
# Answer:
# path.exists(); path.isfile()

# Question 3 of 5
# How would you improve the code below?
 
# f = open("myfile.txt", "r")
# contents = f.read()
# Answer:
# Check that f.mode == 'r' before calling f.read() to read from the file.


# Question 4 of 5
# Your program already imported the ZipFile module using from zipfile import ZipFile. How can you leverage this module to create a new zip archive and add a file to it?
# Answer:
# with ZipFile("archive.zip","w") as newzip:
#    newzip.write("file.txt")


# Question 5 of 5
# What is the difference between shutil.copy() and shutil.copystat() functions?
# Answer:
# While shutil.copy() copies the file content, shutil.copystat() copies the file metadata.


# # Quiz 05 # #

# Question 1 of 8
# Can you print all cities and states in this JSON data, and what approach will you take if you can?
 
# [ { "country": [
#         { "city": "New York", "state": "NY" },
#         { "city": "Boston", "state": "MA" }
#   ]},
#   { "country": [
#         { "city": "Quebec", "state": "QC" },
#         { "city": "Toronto", "state": "ON" }
#   ]} ]
# You are correct!
# It is possible, by using one for i in theJSON loop and within it another nested for j in i["country"] loop.


# Question 2 of 8
# The following code, which is supposed to dump the google.com homepage HTML to the console, is missing a line at the ??? placeholder. What should this line be?
 
# import urllib.request
# webUrl = urllib.request.urlopen("http://www.google.com")
# ???
# print(results)
# You are correct!
# results = webUrl.read()


# Question 3 of 8
# Given the XML below, how will you add a third item to the list that has a yellow color and a small size?
 
# <?xml version="1.0" encoding="UTF-8" ?>
# <catalog>
#   <item color="blue" size="large"/>
#   <item color="red" size="medium"/>
# </catalog>
# You are correct!
# doc = xml.dom.minidom.parse("my.xml")
# newItem = doc.createElement("item")
# newItem.setAttribute("color", "yellow")
# newItem.setAttribute("size", "small")
# doc.firstChild.appendChild(newItem)


# Question 4 of 8
# Given the following JSON data stored in a theJSON object, how can you list only the skill names?
 
# {
#     "name": "John",
#     "title": "Python Developer",
#     "skills": [{
#         "name": "coding",
#         "level": "expert"
#         },
#         {
#         "name": "documentation",
#         "level": "basic"
#     }]
# }
# You are correct!
# for i in theJSON["skills"]:
#     print(i["name"])

# Question 5 of 8
# What value should be returned by the URL request getcode() call to confirm that the specified site can be properly connected to?
# You are correct!
# 200



# Question 6 of 8
# What class does Python provide to parse HTML?
# You are correct!
# HTMLParser


# Question 7 of 8
# The statement below fails when you try to run it. Which troubleshooting step is irrelevant for this scenario?
 
# doc = xml.dom.minidom.parse("myfile")
# You are correct!
# Confirm that the file 'myfile' is first loaded to memory.

# Question 8 of 8
# For the HTML file below, how many times will the handle_starttag() and handle_endtag() methods of the Python-provided HTML parser class be called?
 
# <div class="sidebar">
#   <img src="pic.gif" height="50" width="100" />
#   <button type="button" id="btn-submit">Submit</button>
# </div>

# View full question
# You are correct!
# 3 and 3