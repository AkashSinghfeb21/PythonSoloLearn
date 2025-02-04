# You are given a books.txt file, which includes book titles, each on a separate line.

# Create a program to output how many words each title contains, in the following format:

# Line 1: 3 words

# Line 2: 5 words

with open("quiz.txt") as f:
   #your code goes here
   for i,line in enumerate(f,start=1):
      print(f"Line {i}: {len(line.split())} words")

f.close()