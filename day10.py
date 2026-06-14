num = int(input("enter the number"))
fact = 1
a = 1
while a <= num:
    fact *= a
    a += 1
print("the factorial of", num, "is", fact)


N = int(input("enter nos."))
total_sum = 0
i = 1
while i <= N:
    total_sum += i
    i += 1
print(f"the sum of the nos.{N}numbers is :{total_sum}")


# even and odd
for i in range(1, 21):
    if i % 2 == 0:
        print("even numbers:", i)
    else:
        print("odd numbers:", i)


# Solution C: Summing Until Zero
total_sum = 0
while True:
    num = float(input("Enter a number (0 to quit): "))
    if num == 0:
        break
    total_sum += num
print(f"Total Sum: {total_sum}")

# Solution D: Vowel Counter
text = "Python Programming is Fun"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1
print(f"Vowel count: {count}")


# nummber pyramid
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
