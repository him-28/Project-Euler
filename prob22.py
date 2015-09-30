import string
 
namesFile = open("names.txt","r")
names = namesFile.read()
names = names.replace('"', "") 
names = names.split(",")
names.sort()
 
 
 
totalScore = 0
for name in names:
    nameValue = 0
    for letter in name:
        nameValue += string.ascii_uppercase.index(letter) + 1
 
    totalScore += (names.index(name) + 1) * nameValue
 
print totalScore
