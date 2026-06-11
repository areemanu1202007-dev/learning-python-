# i = 1
# while i <= 100:
#   print(i)
#   i += 1
# i = 100
# while i >= 1:
#   print(i)
#  i -= 1

# print  table of n number
n = int(input("enter the   number:"))
i = 1
while i <= 10:
    print(n, "*", i, "=", n * i)
    i += 1

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
l = len(list1) - 1

while l >= 0:
    print(list1[l])
    l -= 1
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
i = 0

while i < len(list1):
    print(list1[i])
    i += 1


nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36
i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found at idx", i)
    i += 1
