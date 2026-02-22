# buat method dalam kelas
class MyKisah:
  def __init__(self, name):
    self.name = name

  def hello(self):
    print("Hello, my name is " + self.name)

p1 = MyKisah("Dan Heng")
p1.hello()

# method dengan parameter
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(6, 7))

# beberapa method
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Let The World Burn")
my_playlist.add_song("Breakin' Dishes")
my_playlist.show_songs()