# You can use Python to read and write the contents of files.

# This is particularly useful when you need to work with a lot of data that is saved in a file. 

# For example, in data science and analytics, the data is commonly in CSV (comma-separated values) files.

# Let's start by working with text files, as they are the easiest to manipulate. 

# Before a file can be edited, it must be opened, using the open function. 

#myfile = open("filename.txt")

#write mode
open("filename.txt","w")

#read mode
open("filename.txt","r")
x = open("filename.txt")

print(x)

#binary write mode
open("filename.txt","wb")