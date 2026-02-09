# dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# akses kata kunci brand
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# jika key duplikat maka yg ditampilkan adalah nilai yg terakhir
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# cetak jumlah item 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020
}
print(len(thisdict))

# dict dengan berbagai tipe data
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# mengecek tipe data dalam dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# dict constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# get keys
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) # sebelum Key diubah

car["color"] = "white"

print(x) #setelah Key diubah