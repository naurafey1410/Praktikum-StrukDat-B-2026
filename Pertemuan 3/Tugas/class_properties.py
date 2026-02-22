# kelas dengan properti
class Boyfie:
  def __init__(self, name, height):
    self.name = name
    self.height = height

p1 = Boyfie("Dannie", 190)

print(p1.name)
print(p1.height)

# akses properti
class Dannie:
  def __init__(self, height, race):
    self.height = height
    self.race = race

bf1 = Dannie(190 , "Vidyadhara")

print(bf1.height)
print(bf1.race)

# ubah nilai properti
class Boyfie:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("My boyfie's name is " + self.name)

p1 = Boyfie("Dan Heng Imbibitor Lunae", 23)
p1.age = 2000

print(p1.age)