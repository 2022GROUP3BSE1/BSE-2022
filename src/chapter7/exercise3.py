count = 0
total = 0
while True: # WHILE LOOP TO ALLOW CONTINUOUS INPUT OF DATA UNTIL USER ENTERS DONE
    try:
        file_name = input('Enter file name: ')
        with open(file_name, 'r') as txt_file:  # OPENING FILE AS READABLE
            for i in txt_file:
                if i.startswith('X-DSPAM-Confidence:'):
                    colon_position = i.find(':')
                    x = float(i[colon_position + 1:])   # STRING SLICING AND FLOAT CONVERSION
                    count = count + 1   # UPDATING COUNT NUMBER FOR EACH ITERATION
                    total = total + x   # UPDATING TOTAL
        print('Average spam confidence: ', total/count)     # CALCULATING AND PRINTING AVERAGE
    except:
        if file_name.lower() == 'done':
            break
        elif file_name.lower() == "entebbe":
            print("Ohhh! You're from Entebbe too? :)")   # EASTER EGG!
        elif file_name.lower() == "na na boo boo":
            print("NA NA BOO to you - You have been punk'd!")   # EASTER EGG 2!
        else:
            print("file not found!")

