# This is a normal for loop to iterate through a string.

letters = "Ashwanth"

alphabets = []

for letter in letters:
    alphabets.append(letter)

print(alphabets)

# List comprehension is a simpler way to iterate and frame a list.

alphabets = [letter + "a" for letter in letters]
print(alphabets)

# Filtering a list using list comprehension.

names = ["Ashwanth", "John", "Jane", "Jim", "Jill"]

filtered_names_that_have_more_than_4_letters = [name for name in names if len(name) > 4]

print("Names that have more than 4 letters: ", filtered_names_that_have_more_than_4_letters)

# Pair every number in a list with another list

list_a = [2,4,6,8,10]
list_b = [1,3,5,7,9]

paired_numbers = [(a,b) for a in list_a for b in list_b]

print("Paired numbers: ", paired_numbers)