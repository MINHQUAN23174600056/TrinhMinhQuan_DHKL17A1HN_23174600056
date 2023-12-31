 #BT 3
animals = ['ant','bear','cat','dog','elephant','fish','goat','hippo']
print("List of animals:", animals)
print("Number of animals:" , len(animals))
kqtk = input("I want to find: \n")
if kqtk in animals:
    print("There is", kqtk, "in list of animals")
else:
    print("There is no", kqtk, "in list of animals")