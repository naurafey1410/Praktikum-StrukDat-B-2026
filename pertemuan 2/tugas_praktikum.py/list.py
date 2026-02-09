# list
mylist = ["strawberry", "anggur"]
print(mylist)

thislist = ["pisang", "apel", "jeruk", "pisang", "apel"]
print(thislist)

# list length
mylist = ["anggur", "cery", "pisang"]
print(len(mylist))

# list items - data types
list1 = ["abc", 33, True, 70, "female" ]
print(list1)

mylist = ["kiwi", "pisang", "apel"]
print(type(mylist))

# list()
thislist = list(("bery", "pisang", "anggur"))
print(thislist)

# access items
thislist = ["stawberry", "bery", "blueberry"]
print(thislist[1])

thislist = ["pisang", "mangga", "jeruk"]
print(thislist[-1])

# range of indexes
thislist = ["jeruk", "bery", "naga", "apel", "kiwi", "melon", "mangga"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# range of negative indexes
thislist = ["naga", "pisang", "apel", "bery", "kiwi", "melon", "jeruk"]
print(thislist[-4:-1])

# checks if items exsist 
thislist = ["stawberry", "bery", "cherry"]
if "bery" in thislist:
  print("Yes, 'bery' is in the fruits list")

# changes list items
thislist = ["stawberry", "pisang", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apel", "naga", "cherry", "jeruk", "kiwi", "mangga"]
thislist[1:3] = ["blackcurrant", "semangka"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# insert items
thislist = ["bery", "peach", "cherry"]
thislist.insert(2, "stawberry")
print(thislist)

#add list items (append)
thislist = ["peach", "bery", "cherry"]
thislist.append("jeruk")
print(thislist)

thislist = ["pisang", "melon", "bery"]
thislist.insert(1, "mangga")
print(thislist)

thislist = ["jambu", "nanas", "peach"]
tropical = ["mangga", "apel", "pepaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["peach", "semangka", "bery"]
thistuple = ("kiwi", "apel")
thislist.extend(thistuple)
print(thislist)

#remove list items
thislist = ["bery", "semangka", "peach"]
thislist.remove("semangka")
print(thislist)

thislist = ["apel", "peach", "cherry", "peach", "kiwi"]
thislist.remove("peach")
print(thislist)

# pop
thislist = ["peach", "kiwi", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["peach", "kiwi", "cherry"]
thislist.pop()
print(thislist)

# delete
thislist = ["semangka", "melon", "kiwi"]
del thislist[0]
print(thislist)

thislist = ["semangka", "melon", "kiwi"]
del thislist

# clear
thislist = ["peach", "bery", "anggur"]
thislist.clear()
print(thislist)

#loop list
thislist = ["anggur", "pisang", "bery"]
for x in thislist:
  print(x)

thislist = ["anggur", "pisang", "bery"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["anggur", "pisang", "bery"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["anggur", "pisang", "bery"]
[print(x) for x in thislist]

#list Comprehension
fruits = ["anggur", "stawberry", "peach", "kiwi", "melon"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# ex
fruits = ["anggur", "strawberry", "peach", "kiwi", "melon"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# !=
fruits = ["anggur", "strawberry", "peach", "kiwi", "melon"]

newlist = [x for x in fruits if x != "kiwi"]

print(newlist)

# upper
fruits = ["anggur", "strawberry", "peach", "kiwi", "melon"]

newlist = [x.upper() for x in fruits]

print(newlist)

# helo
fruits = ["anggur", "strawberry", "peach", "kiwi", "melon"]

newlist = ["helo" for x in fruits]

print(newlist)

# ganti nilai
fruits = ["anggur", "strawberry", "peach", "kiwi", "melon"]

newlist = [x if x != "melon" else "bery" for x in fruits]

print(newlist)

# sort lists
thislist = ["bery", "anggur", "kiwi", "nanas", "peach"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# reverse
thislist = ["bery", "anggur", "kiwi", "nanas", "peach"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)

# key
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# huruf besar dan kecil
thislist = ["bery", "Peach", "Strawberry", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["semangka", "Apel", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)