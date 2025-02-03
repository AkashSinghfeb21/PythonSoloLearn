a = int(input())

with open("filename.txt","r") as file:
    c = file.read(a)
    print(c)

file.close()