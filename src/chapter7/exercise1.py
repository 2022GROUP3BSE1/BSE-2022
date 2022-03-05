while True: # WHILE LOOP TO ALLOW USER TO ENTER FILE NAME CONTINUOUSLY UNTIL VALID FILE NAME IS ENTERED
    try:
        file_name = input('Enter file name: ')
        with open(file_name, 'r') as txt_file:  # OPENING THE FILE
            for i in txt_file:  # READING EACH LINE OF THE FILE
                print(i.upper())    # CONVERTING EACH LINE TO UPPER CASE
        break
    except:
        print('File not found')