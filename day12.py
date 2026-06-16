a = open("demo.txt", "r")
data = a.read()
print(data)
a.close()


a = open("demo.txt", "a")
data = a.write("\n nature  is beautiful")
print(data)
a.close()
