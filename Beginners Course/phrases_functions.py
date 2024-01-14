#create the name in lower case or in upper case
phrase = "Tania Kioseva"
print(phrase.lower())
print(phrase.upper())

#you can also check what case it is
print(phrase.isupper()) 
#this makes it upper case and after that checks
print(phrase.upper().isupper())

#check the length of the phrase
print(len(phrase))

#replaces the current word (the first coord is the word that you want to replace)
print(phrase.replace("Tania", "Borislavova"))
