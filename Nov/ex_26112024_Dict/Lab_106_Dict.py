my_dict = {
    "name" : "Aman",
    "age" : 22,
    "role" : "SDET",
    "experience" : 3
}
print(my_dict["age"])
print(my_dict)
my_dict["role"] = "Manual tester"
print(my_dict)

for key, value in my_dict.items():
    print(key,"->", value)

print("age" in my_dict)
print("role" in my_dict)
