def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)#2*2=4,4*2 = 8
		
print(power(2, 3))