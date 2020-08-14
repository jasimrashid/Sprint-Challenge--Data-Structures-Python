import time
from classes import BSTNode
start_time = time.time()

print()
print("*** Performing a search of duplicates using a binary search tree ***")
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

bst1 = BSTNode(names_1[0])
bst2 = BSTNode(names_2[0])
for i in range(len(names_1)):
    if i != 0:
        bst1.insert(names_1[i])
        bst2.insert(names_2[i])


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

for name_1 in names_1:
    if bst2.contains(name_1):
        duplicates.append(name_1)

# runtime: 0.14453506469726562 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# *** Converting each list to a set
print()
print()
print("*** Performing a search of duplicates after converting each list to a set (i.e. it's hash value)***")
print()
start_time = time.time()
duplicates_stretch = []
bst1_set = set(names_1)
bst2_set = set(names_2)
for name_1 in bst1_set:
    if name_1 in bst2_set:
        duplicates_stretch.append(name_1)
end_time = time.time()
print (f"{len(duplicates_stretch)} duplicates:\n\n{', '.join(duplicates_stretch)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# runtime: 0.0024368762969970703 seconds

# ** Why this approach is fast:
# When we add an object to a set, its position is determined using the hash of the object 
# to be added. When searching for a value all we need to do is look if the object is at the position 
# determined by its hash, so the speed of this operation does not depend on the size 
# of the set. For lists, in contrast, the whole list needs to be searched, which will 
# become slower as the list grows.






