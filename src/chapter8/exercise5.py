# PROGRAM THAT READS A FILE OF MAIL BOX AND PRINTS THE NUMBER OF MAILS AND SENDERS

count = 0       # INITIATING COUNT AS 0

# WHILE LOOP TO KEEP PROMPTING USER FOR FILE NAME UNTIL USER ENTERS "done"
while True:
    try:
        filename = input("Enter a file name: ")     # PROMPTING USER FOR FILE NAME
        with  open(filename, 'r') as new:       # OPENING FILE AS READABLE
            for i in  new:
                if i.startswith('From '):
                    words = i.split()       # SEPARATING INDIVIDUAL WORDS ON EACH LINE
                    print(words[1])     # PRINTING THE SECOND WORD WHICH IS ON INDEX '1'
                    count += 1      # UPDATING COUNT
                
        print(f"There were {count} lines in the file with From as the first word")
    except:
        if filename.lower() == "done":      # BREAKING LOOP IF USER ENTERS "done"
            break
        else:
            print(f"{filename} file cannot be found!")            
