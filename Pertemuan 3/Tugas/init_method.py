# kelas dan metode init
class MyMine:
  def __init__(self, name, race):
    self.name = name
    self.race = race

p1 = MyMine("Dan Heng", "Vidyadhara")

print(p1.name)
print(p1.race)

# kelas tanpa init
class MyMine:
  pass

p1 = MyMine()
p1.name = "Dan Heng"
p1.race = "Vidyadhara"

print(p1.name)
print(p1.race)

# nilai default init
class MyMine:
  def __init__(self, name, age=23):
    self.name = name
    self.age = age

p1 = MyMine("Dan Heng")
p2 = MyMine("Imbibitor Lunae", 700)

print(p1.name, p1.age)
print(p2.name, p2.age)

# kelas dgn beberapa parameter
class MyMine:
  def __init__(self, name, age, height, country):
    self.name = name
    self.age = age
    self.height = height
    self.country = country

p1 = MyMine("Dan Heng", 23, 168, "Xianzhou Luofu")

print(p1.name)
print(p1.age)
print(p1.height)
print(p1.country)
