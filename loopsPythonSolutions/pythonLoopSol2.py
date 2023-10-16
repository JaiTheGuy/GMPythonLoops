# First Coding Session:
# Output the following values using a while loop: 9,8,7,6,5
########### CODE BELOW HERE #########

num = 9

while num >= 5:
		print(num)
		num -= 1





# Second Coding Session:
# Create a list of ingredients you'd use to make a cake (minumum of 4 elements)
# As you iterate through the list, print out "We have that ingredient!"
# If you come across the ingredients of either flour or sugar, print out the statement "Wait, we don't have that!" and use the keyword break
#
# Complete this challenge with a for loop. If you have more time, try creating a while loop solution as a bonus!
########### CODE BELOW HERE #########


cake_ingredients = ["eggs", "milk", "flour", "sugar", "vanilla extract"]

# For Loop Solution 
for ingredient in cake_ingredients:
		if ingredient in ["flour", "sugar"]:
				print("Wait, we don't have that!")
				break
		else:
				print("We have that ingredient!")



# BONUS: While Loop Solution

cake_ingredients = ["eggs", "milk", "flour", "sugar", "vanilla extract"]

count = 0

while count < len(cake_ingredients):
		ingredient = cake_ingredients[count]

		if ingredient in ["flour", "sugar"]:
				print("Wait, we don't have that!")
				break
		else:
				print("We have that ingredient!")

		count = count + 1