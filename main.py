class Person:
  height = 170
  name = "Name"
  is_impostor = False
  
  def __init__(self, name, height):
    self.name = name
    self.height = height

class hedgehog:
  color = "blue"
    
  def __init__(self, name):
    self.name = name

  def play(self, human):
    human.is_impostor = True

me = Person("I", 15)
sega = hedgehog("Sonic")

print(me.is_impostor)
sega.play(me)
print("Зрадник -", me.is_impostor)

  