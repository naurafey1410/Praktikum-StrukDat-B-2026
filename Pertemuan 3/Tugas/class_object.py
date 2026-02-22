# buat kelas
class MyClass:
  x = 7

print(MyClass)

# buat objek
class MyClass:
  x = 7

p1 = MyClass()
print(p1.x)

# beberapa objek
class MyClass:
  x = 7

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# hapus objek
class Orang:
  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur

  def myfunc(self):
    print("Hello my name is " + self.nama)

p1 = Orang("Jane", 26)

del p1