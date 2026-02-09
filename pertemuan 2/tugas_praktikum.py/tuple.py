# tuple
thistuple = ("pink", "green", "blue")
print(thistuple)

# tuple length
thistuple = ("green", "pink", "purple", "blue", "gray")
print(len(thistuple))

# one tuple
thistuple = ("apple",)
print(type(thistuple))

# not a tuple
thistuple = ("apple")
print(type(thistuple))

# data type
tuple1 = ("red", 30, True, 70, "march")
print(tuple1)

# tuple didalam tuple
thistuple = tuple(("pink", "blue", "green")) 
print(thistuple)

# access
thistuple = ("green", "pink", "gray")
print(thistuple[1])

# indeks negatif
thistuple = ("green", "pink", "gray")
print(thistuple[-1])

# range index
thistuple = ("yellow", "purple", "gray", "green", "pink", "blue", "red")
print(thistuple[2:5])

thistuple = ("yellow", "purple", "gray", "green", "pink", "blue", "red")
print(thistuple[:4])

thistuple = ("yellow", "purple", "gray", "green", "pink", "blue", "red")
print(thistuple[2:])

thistuple = ("yellow", "purple", "gray", "green", "pink", "blue", "red")
print(thistuple[-4:-1])

# cek item
thistuple = ("green", "pink", "cyan")
if "pink" in thistuple:
  print("Yes, 'pink' is in the colors tuple")

# mengubah tuple menjadi list untuk mengubah item tuple
x = ("pink", "blue", "green")
y = list(x)
y[1] = "gray"
x = tuple(y)

print(x)