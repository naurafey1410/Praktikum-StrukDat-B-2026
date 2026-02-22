# akses properti menggunakan self
class Mine:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def Lovers(self):
    print("My boyfriend's name is " + self.name)

p1 = Mine("Dan Heng", 23)
p1.Lovers()

# menghubungkan metode dengan objek
class Mine:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Mine("Dan Heng")
p2 = Mine("Imbibitor Lunae")

p1.printname()
p2.printname()

# memanggil metode lain
class Boyfie:
  def __init__(self, name):
    self.name = name

  def hi(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.hi()
    print(message + "! Welcome to our website.")

p1 = Boyfie("Dan Heng")
p1.welcome()