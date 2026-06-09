info = {"name": "Manushka", "age": "18", "subject": "[python, java, c++]"}
print(info)
print(type(info))
print(len(info))
print(info["name"])
print(info["age"])
print(info["subject"])
info["name"] = "manu"
print(info)
info["love"] = "traveling"
print(info)
student = {
    "name": "ram ",
    "subject": {
        "physics": "90",
        "maths": "95",
        "english": "85",
        "chemistry": "80",
        "python": "100",
    },
}

print(student)
print(student["subject"]["chemistry"])
print(student.keys())
print(student["subject"].keys())
print(student.values())
print(student["subject"].values())
print(student.items())
print(student["subject"].items())
print(student.get("name"))
print(student.update({"name": "shyam"}))
print(student)
print(list(student.keys()))
