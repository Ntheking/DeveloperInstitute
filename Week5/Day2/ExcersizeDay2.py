
# excersize 1
# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
# class Lion(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# myCats = []
# myCats.append(Bengal("WhoCares", 1))
# myCats.append(Chartreux("WhoCares1", 2))
# myCats.append(Lion("WhoCares2", 3))
# pets = Pets(myCats)

# for pet in pets.animals:
#     print(pet.walk())

#Excersize2
# import random

# class Dog():
#     name = ""
#     age = 0
#     weight = 0
#     def __init__(self, name, age, weight):
#         self.name = name;
#         self.age = age;
#         self.weight = weight;
#     def bark(self):
#         print("barkbarkbarkabarkbark")
#     def run_speed(self):
#         print(self.weight/self.age * 10)
#     def fight(self, other):
#         if self.weight/self.age * 10>other.weight/other.age * 10:
#             print(self.name + ' won!')
#         elif other.weight/other.age * 10>self.weight/self.age * 10:
#             print(other.name + ' won!')

# doga = Dog("WhoCares", 5, 4)
# dogb = Dog("WhoCares2", 5, 2)
# doga.run_speed()
# dogb.bark()
# doga.fight(dogb)

# Excerzise3

# class PetDog(Dog):
#     trained = false
#     def train(self):
#         self.trained= true;
#         print("barkbarkbarkabarkbark")
#     def play(self,*dogFriends)
#         dogPrint = ""
#         for dog1 in dogFriends:
#             dog1.trained = false;
#             dogPrint += dog1 + ' '
#         print(dogPrint + ' play together')
#     def doATrick(self)
#         r = random.randint(0, 100)
#         if r >= 0 and r < 25:
#             print(self.name + " does trick one")
#         if r >= 25 and r < 50:
#             print(self.name + " does trick two")
#         if r >= 50 and r <= 100:
#             print(self.name + " does trick three")

#Excersize 4

class Family():
    familymembers = [ {'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False} ]

    def born(self, **kwargs):
        self.familymembers.append(kwargs)
        print("Congratulations")
    def is_18(self, name):
        for member in self.familymemebers:
            if member['name'] == name:
                if member['age'] > 18:
                    return true;
                return false;
    def present(self):
        for member1 in self.familymemebers:
            print(member1['name'] + ' is ' + member1['age'] + ' years old')
#excersize 5
class Incredibles(Family):
    familymembers = [{'name':'Michael','age':35,'gender':'Male','is_child':False, 'power':'yay', 'incredibleName' : 'whocares'}, {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power':'yay', 'incredibleName' : 'whocares'}]

    def usePower(self, name):
        for member in self.familymemebers:
            if member['name'] == name:
                if member['age'] > 18:
                    print(member['power'])
                else:
                    print("NO")
    def presentI(self):
        for member1 in self.familymemebers:
            print(member1['incredibleName'] + ' has ' + member1['power'])






