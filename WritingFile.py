# file = open("Demo.txt","w")
file = open("Demo.txt","a") # this "a" operation will append a new line in existing file
file.write("\n U a Gay")
file.close()

file = open("Demo.txt","r")
print(file.read())
file.close()