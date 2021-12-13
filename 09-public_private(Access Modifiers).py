# class Robot:

#     population = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Robot.population += 1

#     def __say_hi(self):
#         print(f"Greetings, my masters call me {self.name}.")

#     def cal_add(self, a, b):
#         return a + b

#     @classmethod
#     def how_many(cls):
#         return f"We have {cls.population} robots."


# class Siri(Robot):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         print(self.name)
#         print(self.age)


# eric = Robot("Eric", 8)
# print(eric.age)
# eric.age = -100
# print(eric.age)

# ssss = Siri("iphone8", 9)

# print(ssss.age)

# -------------------------------------- #

class Robot:


    __population = 0

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        Robot.population += 1

    def __say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(self.name)
        print(self._age)


eric = Robot("Eric", 8)
eric.__say_hi()
# print(eric.age)
# eric.age = -100
# print(eric.age)

eric.__say_hi()
