class Person:
  height = 170
  name = "Name"
  
  def __init__(self, name, height):
    self.name = name
    self.height = height
  
  def walk_out(self, pet):
    pet.wants_pee = False

class Dog:
  color = "white"
  wants_pee = True
  
  def __init__(self, name):
    self.name = name

me = Person("I", 15)
pet = Dog("Bob")

print(pet.wants_pee)
me.walk_out(pet)
print("Собака хоче пі -", pet.wants_pee)

  