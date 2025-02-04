n = int(input())

file = open("quiz.txt","w+")

for i in range(1,n+1):
    file.write(str(i)+"\n")

file.close()

f = open("quiz.txt","r")

print(f.read())

f.close()

