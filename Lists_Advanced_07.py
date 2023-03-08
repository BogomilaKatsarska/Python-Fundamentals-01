# Лисответе са референтен тип данни. а = [1, 2, 3] b=a => a и b заемат 1 и също място в паметта
# 1. nums.append(100)
# 2. nums.insert(0, 100) --> inserts 100 on index 0
# 3. nums.extend([100, 200]) --> adds 100 and 200 at the end of the list
# 4. nums.clear() --> clears all the items in the list
# 5. nums.pop() --> removes the last element(or the mentioned index). Has return value
# 6.nums.remove(3) --> removes the element, not the index

# lambda el: int(el) ** 2
# numbers = list(map(int, numbers_as_strings))
# numbers = list(map(lambda el: int(el), nums_as_strings))
# evens = list(filter(lambda x: x%2 == 0, nums))

# You can use the set() method to extract only the unique elements from a list.
# The set() method returns a set with the unique values

nums = [1, 2, 3, 4, 1]
uniques = list(set(nums))
print(uniques)

# List slicing works like for loop - exclusive /e.g.: elements = nums[1:4:-1]/