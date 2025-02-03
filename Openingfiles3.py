# file = open("filename.txt")

# cont = file.read()
# print(cont)

# file.close()

file = open("filename.txt")

print(file.read(3))
print(file.read(2))
print(file.read())

file.close()