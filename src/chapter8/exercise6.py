# PROGRAM THAT STORES NUMBERS IN A LIST AND PRINTS OUT MAXIMUM AND MINIMUM

num_list = []
while True:     # WHILE LOOP TO KEEP PROMPTING USER FOR NUMBERS UNTIL USER ENTERS "done"
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)        # CONVERTING NUMBER TO INTEGER SO THAT ONLY NUMBERS ARE ALLOWED
        num_list.append(number)     # APPENDING NUMBERS IN THE LIST
    except:
        if user_input == "done":
            break
        else:
            print("invalid input!")

print(f"maximum: {max(num_list)}\nminimum: {min(num_list)}")        # PRINTING OUT MAXIMUM AND MINIMUM IN THE LIST