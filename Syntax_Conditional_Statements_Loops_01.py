# Data types and Variables(==names): int, float, str, bool

# a=25  --> assign/присвояване/ value to 'a'
# a==25 --> compare 'a' to 25

# IF/ELIF/ELSE

# a = 5
#
# if a > 5:
#     print("It is higher than 5")
# elif a == 5:
#     print("It is equal to 5")
# else:
#     print("It is lower than 5")

# Find the largest number - 'max' function
# a = int(input())
# b = int(input())
# c = int(input())
# print(max(a, b, c))

# алгоритъм - последователност от команди, които следват една след друга в определен ред
# For and While цикли - повтарят парче от код

# for number in range(1, 10):
#     print(number)

# The break statement stops the loop before it has looped through all the items

# for number in range(1, 11):
#     print(number)
#     if number == 5:
#         break
# print("End of the loop")

# for number in range(1, 11):
#     if not number == 3:
#         continue
#     print(number)
#
# print("End of the loop")

# With a while loop we can execute a set of statements as long as the condition is true

# word = input()
# new_word = ""
#
# for i in range(len(word)-1, -1, -1):
#     new_word += word[i]
# print(new_word)

# word = input()
#
# for i in range(len(word)-1, -1, -1):
#     print(word[i], end="")

# word = input()
# print(word[::-1])

# while True:
#     number = float(input())
#     if 100 >= number >= 1:
#         break
#
# print(f"The number {number} is between 1 and 100.")

# n = int(input())
#
# for number in range(1, n+1):
#     print("*"*number)
# for number in range(n-1, -1, -1):
#     print("*"*number)