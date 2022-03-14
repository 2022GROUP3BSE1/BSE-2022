# A PROGRAM THAT DISPLAYS A SUMMARY REPORT TO THE  USER

# DEFINING A FUNCTION THAT WILL OPEN THE USER'S FILE
def open_file():
    while True:
        input_file = input("\nEnter the file name: ")     # PROMPTING USER FOR FILE NAME
        try:
            file_object = open(input_file, "r")     # OPENING FILE AS READABLE
            break
        except:
            print(f"{input_file} file not found!")      # CATCHING ERROR IF FILE IS NOT IN DIRECTORY
    return file_object      # RETURNING FILE OBJECT TO MAIN PROGRAM

# DEFINING A FUNCTION THAT WILL PROCESS THE FILE OBJECT FROM THE OPEN FILE FUNCTION
def process_file(file_object):
    count = 0       # INITIATING COUNT FOR RECORDS AS 0
    total_percent = 0
    year = input("Enter year: ")

    # PRINTING A MENU FOR ENTRY VALUES FOR INCOME LEVEL
    print('''Menu of entries for income level:
            1-Low income
            2-Lower middle income
            3-Upper middle income
            4-High income''')
    
    while True:     # WHILE LOOP TO KEEP PROMPTING UNTIL CORRECT INPUT FOR INCOME LEVEL IS ENTERED
        income_level = input("Enter income level: ")

        if income_level == '1':
            income_level = 'WB_LI'
            break
        elif income_level == '2':
            income_level = 'WB_LMI'
            break
        elif income_level == '3':
            income_level = 'WB_UMI'
            break
        elif income_level == '4':
            income_level = 'WB_HI'
            break
        else:
            print("Invalid input!")
    # INITIATING MAX AND MIN PERCENTAGES AND THEIR CORRESPONDING COUNTRIES
    max_percent = None
    min_percent = None
    max_country = ''
    min_country = ''
    
    for line in file_object:        # READING INDIVIDUAL LINES IN THE FILE
        
        # READING THE FIELDS OF YEAR AND INCOME LEVEL
        year_field = line[88:]
        income_field = line[50:58]
        percentage_field = line[59:62]
        country_field = line[:49]

        # STRIPING TO REMOVE WHITE SPACES
        year_field = year_field.strip()
        income_field = income_field.strip()
        percentage_field = percentage_field.strip()
        country_field = country_field.strip()
        
        # PRINTING LINES WITH CORRESPONDING YEARS AND INCOME LEVELS
        if (year == "" or year.lower() == "all") and income_field == income_level:
            count = count + 1
            total_percent = total_percent + int(percentage_field)

            if max_percent is None or percentage_field > max_percent:
                max_percent = percentage_field  # UPDATING MAXIMUM PERCENTAGE
                max_country = country_field     # UPDATING COUNTRY WITH MAXIMUM PERCENT
            elif min_percent is None or percentage_field < min_percent:
                min_percent = percentage_field
                min_country = country_field
            else:
                pass
        
        elif year_field.startswith(year) and income_field == income_level:
            count = count + 1
            total_percent = total_percent + int(percentage_field)

            if max_percent is None or percentage_field > max_percent:
                max_percent = percentage_field  # UPDATING MAXIMUM PERCENTAGE
                max_country = country_field     # UPDATING COUNTRY WITH MAXIMUM PERCENT
            elif min_percent is None or percentage_field < min_percent:
                min_percent = percentage_field
                min_country = country_field
            else:
                pass
    if count != 0:
        print(f"\n>>>Count for records: {count}")
        print(f">>>Average percent: {round((total_percent/count),1)}")
        print(">>>Country with highest percentage:", max_country, max_percent)
        print(">>>Country with lowest percentage:", min_country, min_percent)
    else:
        print("No records.")

# DEFINING MAIN FUNCTION TO CALL THE open_file FUNCTION AND process_file FUNCTION
def main():
    file_name = open_file()
    process_file(file_name)
    file_name.close()

# CALLING MAIN FUNCTION
main()
