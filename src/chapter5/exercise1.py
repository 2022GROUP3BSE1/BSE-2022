'''A PROGRAM THAT ALLOWS A USER TO ENTER NUMBERS ONE AT A TIME
AND PRINTS OUT THE TOTAL, COUNT AND AVERAGE OF THE NUMBERS'''

# Declaring variables
total = 0
count = 0

# Initiating while-loop
while True:
    data = input('Enter a number: ')
# Using 'Try and except to capture Invalid user input
# if user enters text data that cannot be converted to float
    try:
        number = float(data)  # converting user input to float data type
        total = total + number  # calculating total of input so far
        count = count + 1  # counting number of inputs sos far
        average = total/count  # calculating average
    except:
        words = data.lower()  # converting all input to lower case
        if words == 'done':
            break
        else:
            print('Error, invalid input')
print('Total=', total)
print('Count=', count)
print('Average=', average)
