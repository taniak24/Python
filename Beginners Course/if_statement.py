
is_female = True
is_tall = False

if is_female and is_tall: #both true
    print("You're a female and  you're tall") 
elif is_female and not(is_tall): #female - true and tall - false
    print("You're a short female") 
elif not(is_female) and is_tall: #female - false and tall - true
    print("You're a tall male")
else:
    print("You are either not female or not tall or both") #both false