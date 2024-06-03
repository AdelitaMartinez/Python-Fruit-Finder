# MartinezP3
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: Provides users capability to find fruit in a string
# Python Version: 3.12.3

# List of fruits 

fruits = [
'Apricot',
'Asian Pear',
'Avocado',
'Banana',
'Blackberries',
'Blueberries',
'Boysenberries',
'Cactus Pear',
'Cantaloupe',
'Cherries',
'Coconut',
'Cranberries',
'Figs',
'Gooseberries',
'Grapefruit',
'Grapes',
'Honeydew Melon',
'Kiwifruit',
'Limes',
'Longan',
'Loquat',
'Lychee',
'Madarins',
'Malanga',
'Mandarin Oranges',
'Mangos',
'Mulberries',
'Nectarines',
'Oranges',
'Papayas',
'Passion Fruit',
'Peaches',
'Pears',
'Persimmons',
'Pineapple',
'Plums',
'Pomegranate',
'Prunes',
'Quince',
'Raisins',
'Raspberries',
'Rhubarb',
'Strawberries',
'Tangelo',
'Tangerines',
'Tomato',
'Ugli Fruit',
'Watermelon'
]
 
# Welcome

title = '**Welcome to Fruit Finder**'
width = 80 
halfway = width//2
start_at = halfway - 6 
line1 = start_at*' ' + title
print(line1)

# Introduction and Instructions

print('\nThis program allows users to enter an input and will show if any fruits in the sentence match a fruit in a premade list.')
print('Please enter a sentence or a list of words, and the program will tell you which fruits, if any, are mentioned')
#print('*Please note that fruit names are case sensitive')
print('\n')

# Get user input (.strip() method =  remove whitespaces from input)
# .lower() method to convert input to lowercase
user_input = input("Enter a sentence or list of words: ").strip().lower()

# Create empty array to store found fruits
found_fruits = []

# Iterate over input using For Loop
# Use if statement to look for fruits in input

for fruit in fruits: # For Loop
  if fruit.lower() in user_input: # if statement and .lower() to check if lowecase versions match lowercase input
    found_fruits.append(fruit) # .append() adds fruit to back of the array

# Display found fruits or no fruits found using if else statement
if found_fruits: 
  print('\n Fruits found in your input: ')
  for fruit in found_fruits:
    print(fruit)
    # Count the number of fruits found
    num_fruits = len(found_fruits) # len() = built in function that returns length
    print('\n Number of fruits found: {num-fruits}')

    # Replace instance of fruit with "Brussels Sprouts"
    first_fruit = found_fruits[0]
    new_input = user_input.replace(first_fruit.lower(), 'brussels sprouts', 1)
    print('\n Updated input: {new_input}')
else: 
  print('\n No fruits found')