# python set
myset = {"apple", "banana", "cherry"}
print(myset)

# jika terdapat nilai duplikat, maka yg diprint cuma satu
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# nilai True dan 1 dianggap duplikat
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# begitu juga dengan False dan 0
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# set length
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

set1 = {"cba", 34, False, 40, "male"}
print(set1)

# set didalam set
thisset = set(("apple", "banana", "cherry")) 
print(thisset)

# cek apakah banana ada didalam set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# add set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# update
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# nambahin list ke set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# remove
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# discard
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# pop
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# clear
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# del
thisset = {"apple", "banana", "cherry"}
del thisset

# loop set
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


