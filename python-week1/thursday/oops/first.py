class Dog :
    species = "Canis familiaris"
    def __init__ (self , name , age):
        self.name = name
        self.age = age

millie = Dog("millie", 2)
print(millie.name)
print(millie.age)
print(millie.species)