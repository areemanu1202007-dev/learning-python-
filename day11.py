# waf to print the length of a list.
cities = ["deldi", "gurgaon", "noida", "mumbai"]
hero = ["thor", "ironman", "superman", "batman", "spiderman"]


def print_len(items):
    length = len(items)
    print(length)


print_len(cities)
print_len(hero)


def print_list(list):
    for item in list:
        print(item, end=" ")


print(cities)
print(hero)


def fact(n):
    f = 1
    a = 1
    while a <= n:
        f *= a
        a += 1
    print("factorial of", n, "is", f)


fact(4)


def convert(usd):
    inr_val = usd * 95
    print("usd=", inr_val)


convert(5)
