# PROGRAM THAT READS WORDS IN AFILE AND ADDS THEM TO A LIST

list = []       # INITIATING AN EMPTY LIST

with open("romeo.txt","r") as filename:     # OPENING FILE "romeo.txt"
    for line in filename:
        words = line.split()      # SPLITTING INDIVIDUAL WORDS IN EACH LINE
        for word in words:
            if not word in list:
                list.append(word)       # ADDING UNIQUE WORD IN LIST
list.sort()     # SORTING LIST IN ALPHABETICAL ORDER
print(list)
