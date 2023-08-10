
# d = {"name":["mohammad","ali"],"age":30,}

# print(d["name"])
# # d["name"]="mohmmadreza"
# print(d)

# roman_numbers = {
#     "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
#     "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10, }

# key = input()
# if key not in roman_numbers.keys():
#     print("invalid key")
# else:
#     number = roman_numbers[key]
#     print(number)


# abjad = {"ا": 1, "ب": 2, "ج": 3, "د": 4, "ه": 5, "و": 6, "ز": 7, "ح": 8, "ط": 9, "ی": 10, "ک": 20, "ل": 30, "م": 40, "ن": 50, "س": 60,
#          "ع": 70, "ف": 80, "ص": 90, "ق": 100, "ر": 200, "ش": 300, "ت": 400, "ث": 500, "خ": 600, "ذ": 700, "ض": 800, "ظ": 900, "غ": 1000, }

# name = input()
# s = 0
# for i in name:
#     s += abjad[i]
# print(s)
# a = {}
# a["name"]="mohmmad"

# [
#     {
#         "name": "mohammad",
#         "age": 16,
#         "id": "6546985645"
#     },
#     {
#         "name": "ali",
#         "age": 20,
#         "id": "dfdffd"
#     },
#     {
#         "name": "reza",
#         "age": 17,
#         "id": "sdfdfdds"
#     },    {
#         "name": "ahmad",
#         "age": 10,
#         "id": "24541545"
#     }

# ]

n = int(input())
people = []
for i in range(n):
    name = input(f"please enter person{i}'s name")
    age = int(input(f"please enter person{i}'s age"))
    Id = input(f"please enter person{i}'s id")
    person = {"name":name,"age":age,"id":Id}
    people.append(person)
    # people.append({"name":input("name"),"age":int(input("age")),"id":input("id")})

print(people)

