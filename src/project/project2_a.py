# PROGRAM THAT COPIES DATA FROM MEASLES FILE FOR A GIVEN YEAR TO A FILE SELECTED BY A USER

try:        # TRY AND EXCEPT TO CHECK IF MEASLES FILE IS IN DIRECTORY
    measles_file = open("measles.txt", "r")
except:
    print("Measles file not found in current directory!")

output_file = input("Enter name of file: ")     # PROMPTING USER FOR FILE NAME TO COPY DATA TO
file_handle = open(output_file, "w")        # OPENING THE USER'S FILE AS WRITABLE

year = input("Enter year: ")        # PROMPTING USER FOR YEAR TO COPY DATA FROM

for line in measles_file:       # READING LINES FROM MEASLES FILE
    if year.lower() == "" or year == "all":
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
        print(i)
        