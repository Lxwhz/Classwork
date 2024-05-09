# Bendjy St - Paul
# 2024-05-08

# creating an empty list
lst = []

# using a for loop to add numbers 1-100 to the list
for b in range(1,101):
    lst.append(b)

# printing the list lst
print(lst)

# create an empty list named odd
odd = []

# using a for loop to add odd numbers 1-100 to the list odd
for a in range(1,101,2):
    odd += [a]

# printing the list odd
print(odd)

# create an empty list named even
even = []

# using a for loop to add even numbers 1-100 to the list even
for c in range(2,101,2):
    even += [c]

# printing the list even
print(even)

# create a variable named b that points to the first list that you created
b = lst

# create a variable named joined that joines even and odd lists using a opperator
joined =  even + odd

# print joinedprint(joined)