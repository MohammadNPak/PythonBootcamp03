

# class User:
#     # class attribute or class variable
#     x = 2
#     y = 3

#     # initializer or cunstructure
#     # type hint
#     def __init__(self,username:str)-> None:
#         # u is object variable
#         self.u = username

#     def say_hello(self):
#         print("hello")

#     @staticmethod
#     def say_hello2():
#         print("hello")

#     @classmethod
#     def say_hello3():
#         print("hello")


# u1 = User("mohammad")
# u2 = User("ali")
# # u1.x
# # u1.y
# # u1.say_hello()

# u1.say_hello()
# u2.say_hello()

# print(u1.u)
# print(u2.u)


# class Car:
#     wheel_number = 4
#     max_speed = 200

#     def __init__(self, color, plate_number):
#         self.c = color
#         self.p = plate_number
#         print(id(self))

#     # def __str__(self):
#     #     return f"wheel_number:{Car.wheel_number},color:{self.c},plate number:{self.p}"

# my_car = Car("red", 123)
# car1 = Car("yellow", 321)

# # print(id(my_car))
# # print(id(car1))

# print(type(my_car))
# print(type(car1))
# print(my_car.max_speed)

# my_car.c = "blue"
# print(my_car.c)
# print(car1.c)

# Car.max_speed = 300
# my_car.max_speed = 500
# print(my_car.max_speed)
# print(car1.max_speed)

# print(my_car)
# print(car1.c,car1.p)


# class Person:
#     eyes = 2
#     feet = 2
#     hands = 2

#     def __init__(self, name, height, weight):
#         self.name = name
#         self.height = height
#         self.weight = weight

#     def __str__(self):
#         return f"name:{self.name},{self.height},{self.weight}"


# class Student(Person):
#     major = "engineering"

#     def __init__(self,id,name,height,weight):
#         super().__init__(name,height,weight)
#         self.id = id

#     def __str__(self):
#         return super().__str__()+" " + Student.major

# s1 = Student("mohammad", 185, 90)
# print(s1)

# (abstraction, inheritance, encapsulation, and polymorphism)

import sqlite3


class User:
    db_address = "db.sqlite3"

    def __init__(self, username, password, email, picture):
        self.username = username
        self.password = password
        self.email = email
        self.picture = picture
        self.create_db()

    def __str__(self):
        return f"username:{self.username},email:{self.email}"

    def save(self):
        connection = sqlite3.connect(User.db_address)
        cursor = connection.cursor()
        cursor.execute(f"""
            insert into
                user (username, password, email,picture)
                values (?,?,?,?);""",
                       (self.username, self.password, self.email, self.picture))
        connection.commit()
        connection.close()

    @classmethod
    def get(cls, username):
        connection = sqlite3.connect(User.db_address)
        cursor = connection.cursor()
        result = cursor.execute(f"""select username, password, email,picture from 
                user where username=? ;""",
                                (username,))
        # connection.commit()
        r = list(result)
        u = User(r[0][0], r[0][1], r[0][2], r[0][3])
        connection.close()
        return u

    def create_db(self):
        connection = sqlite3.connect(User.db_address)
        cursor = connection.cursor()
        cursor.execute(
            "create table if not EXISTS user(id integer primary key,username text,password text,email text,picture text);")
        connection.close()


# u1 = User("mohammad", "123", "m@gmail.com", "profile.jpg")
# u1.save()
# u2 = User.load("mohammad")

r = User.get("mohammad")
print(r)
