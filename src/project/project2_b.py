# A PROGRAM THAT DISPLAYS A SUMMARY REPORT TO THE  USER

# DEFINING A FUNCTION THAT WILL OPEN THE USER'S FILE
def open_file():
    while True:
        input_file = input("Enter the file name: ")     # PROMPTING USER FOR FILE NAME
        try:
            file_object = open(input_file, "r")     # OPENING FILE AS READABLE
            break
        except:
            print(f"{input_file} file not found!")      # CATCHING ERROR IF FILE IS NOT IN DIRECTORY
    return file_object      # RETURNING FILE OBJECT TO MAIN PROGRAM

# DEFINING A FUNCTION THAT WILL PROCESS THE FILE OBJECT FROM THE OPEN FILE FUNCTION
def process_file(file_object):
    year = input("Enter year: ")

    # PRINTING A MENU FOR ENTRY VALUES FOR INCOME LEVEL
    print('''Menu of entries for income level:
            1-Low income
            2-Lower middle income
            3-Upper middle income
            4-High income''')
    
    while True:     # WHILE LOOP TO KEEP PROMPTING UNTIL CORRECT INPUT FOR INCOME LEVEL IS ENTERED
        try:
            income_level = input("Enter income level: ")

            if income_level == '1':
                income_level = 'WB_LI'
                break
            elif income_level == '2':
                income_level = 'WB_LMI'
                break
            elif income_level == '3':
                income_level == 'WB_UMI'
                break
            elif income_level == '4':
                income_level = 'WB_HI'
                break
            else:
                raise ValueError        # RAISING AN ERROR FOR ANY INPUT WHICH DOES NOT MATCH MENU OF ENTRIES

        except:     # CATCHING AN ERROR IF INPUT DOES NOT MATCH MENU OF ENTRIES
            print("Invalid input!")

    for line in file_object:        # READING INDIVIDUAL LINES IN THE FILE
        
        # READING THE FIELDS OF YEAR AND INCOME LEVEL
        year_field = line[88:]
        income_field = line[50:58]

        # STRIPING TO REMOVE WHITE SPACES
        year_field = year_field.strip()
        income_field = income_field.strip()
        
        # PRINTING LINES WITH CORRESPONDING YEARS AND INCOME LEVELS
        if year_field == year and income_field == income_level:
            print(line)


# DEFINING MAIN FUNCTION TO CALL THE open_file FUNCTION AND process_file FUNCTION
def main():
    file_name = open_file()
    process_file(file_name)

# CALLING MAIN FUNCTION
main()
