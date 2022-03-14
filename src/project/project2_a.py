# PROGRAM THAT COPIES DATA FROM MEASLES FILE FOR A GIVEN YEAR TO A FILE SELECTED BY A USER

while True:
    try:        # TRY AND EXCEPT TO CHECK IF MEASLES FILE IS IN DIRECTORY
        measles_file = open("measles.txt", "r")
    except:
        print("Measles file not found in current directory!")

    while True:
        output_file = input("\nEnter name of file or 'done' to quit: ")     # PROMPTING USER FOR FILE NAME
        
        if output_file == '':
            print("File name cannot be empty.")
        else:
            break

    if output_file.lower() == 'done':       # TERMINATING THE PROGRAM IF USER ENTERS 'done'
        quit()
    else:
        file_handle = open(output_file, "w")        # OPENING THE USER'S FILE AS WRITABLE

    year = input("Enter year: ")        # PROMPTING USER FOR YEAR TO COPY DATA FROM

    for line in measles_file:       # READING LINES FROM MEASLES FILE
        if year == "" or year.lower() == "all":
            file_handle.write(line)
        else:
            year_field = line[84:]       # STARTING INDEX FOR YEAR FIELD IS 84
            year_field = year_field.strip()       # STRIPPING TO REMOVE WHITE SPACES
            if year_field.startswith(year):
                file_handle.write(line)     # WRITING ALL LINES THAT HAVE THE INPUT YEAR IN THE OUTPUT FILE

    file_handle.close()

    # PRINTING DATA IN CREATED FILE
    with open(output_file,"r") as txt_file:
        for i in txt_file:
            print(i.strip())
    print(f"\nThe data has been copied to file '{output_file}'")