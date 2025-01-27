nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums # it will take common values from union of both ie 1,2,3
nums = filter(lambda x: x > 1, nums)# here it is a anoymous function creation its logic says if x is greater than one return those values as list or filter.
print(len(list(nums)))