
friends = ["Kathrine", "Stefan", "Elena", "Damon", "Bonnie"]
lucky_numbers = [4, 15, 6, 23, 47, 35]

##print(friends[1:]) #with the ":" -> it starts printing all of the elements after the number
##print(friends[1:4]) #it will print the element from the first to the forth

#LISTS FUNCTIONS - TRY EACH SEPERATELY
friends.extend(lucky_numbers) #add the numbers to the numbers
friends.append("Klaus")
friends.insert(1, "Kelly") #puts the name in the first position
friends.remove("Kathrine")
lucky_numbers.sort() #puts it in order
friends.clear #delete all the elements
print(friends.index("Elena")) #check if the name is on the list and where

print(friends)
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

### TUPLES ###
#almost the same as lists, but you can't change it or modify it outside of it
coordinates = (4, 5)

coordinates[1] = 10 #ERROR - because you cant modify

#list of tuples
coord = [(4, 5), (6, 7), (8, 9), (15, 16)]

print(coordinates)
