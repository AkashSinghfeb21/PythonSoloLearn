# The function filter filters an iterable by leaving only the items 
# that match a condition (also called a predicate).

nums = [1,2,3,4,5]

res = list(filter(lambda x:x%2==0,nums))

print(res)