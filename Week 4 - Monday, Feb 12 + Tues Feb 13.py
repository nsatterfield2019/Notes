# LISTS AND LIST COMPREHENSIONS

my_list = ["Bev", "abe", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_numlist = [8, 4, 7, 5, 2, 9]

# using indicies
print(my_list[3])
my_list[3] = "Deb"
print(my_list)

# slicing
print(my_list[3:5]) # prints index 3 and 4
print(my_list[:4]) # beginning to 3
print(my_list[4:]) # 4 to end
print(my_list[:]) # prints the whole list

# copying a list
my_list_copy = my_list # NOT THIS WAY --> Doesn't make a new copy just assigns the variable to the same list
my_list_copy[-1] = "Gob" # can use negative indicies, changing "Gus" to "Gob"
print(my_list_copy)
print(my_list)


my_list_copy = my_list[:] # this copies the whole list into a new one
my_list_copy[-2] = "Feb" # can use negative indicies, changing "Gus" to "Gob"
print(my_list_copy)
print(my_list)

# METHODS FOR LISTS

# finding out if an item exists in a list
print("Deb" in my_list)

# min(list) and max(list) and sum(list)
print(min(my_numlist))
print(max(my_numlist))
print(sum(my_numlist))
print(min(my_list)) # Alphabetical (sort of) goes by ordinal number
# print(ord("A"))

# find the index
print(my_list.index("Deb"))

# find how many times an item appears in a list
print(my_list.count("Gob"))

# add to a list
my_list.append("Gob")
print(my_list.count("Gob"))

# insert a value into a list
my_list.insert(3, "Don")
print(my_list)

# sort a list
print(my_list)
my_list.sort()
print(my_list)

# reverse a list
my_list[my_list.index("abe")] = "Abe"
my_list.reverse()
print(my_list)

# clear a list
my_list.clear()
print(my_list)

my_list = my_list_copy
print(my_list)

# Pop --> removes an item from the list AND returns it
removed_name = my_list.pop() # default removes the last items (pops it off)
print(my_list)
print(removed_name)

first_name = my_list.pop(0) # you can also index it
print(first_name)
print(my_list)

# Delete an item from a list
del my_list[0]
print(my_list)
del my_list[1:]
print(my_list)

# ITERATING
# FOR EACH LOOP - Cannot change the list with this method
for item in my_numlist:
    item *= 2
    print(item)

print(my_numlist)

# Index variable LOOP
for i in range(len(my_numlist)):
    my_numlist[i] *= 2
    print(my_numlist[i])

print(my_numlist)

# CREATE LISTS
# Make a list of numbers 1 to 100
my_list = []
for i in range(1, 101):
    my_list.append(i)

print(my_list)

# Go back through the list and square everything
for i in range(len(my_list)):
    my_list[i] **= 2

print(my_list)

# make a list from 0 to 9
my_list = []
for i in range(10):
    my_list.append(i)

print(my_list)

# print each item in the list using for each
for item in my_list:
    print(item)

# add 10 to each item in the list using iteration
for i in range(len(my_list)):
    my_list[i] += 10
print(my_list)

# make a 2d list that is 10 x 10 [[0, 0], [0, 1], [0, 2] ... [9, 9]]
my_list = []
for i in range(10):
    for j in range(10):
        my_list.append([i, j])

print(my_list)

