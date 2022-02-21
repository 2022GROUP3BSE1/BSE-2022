biggest = None
smallest = None

while True:
    data = input('Enter a number: ')

    try:
        number = float(data)
        if biggest is None or number > biggest:
            biggest = number
        elif smallest is None or number < smallest:
            smallest = number
        else:
            continue
    except:
        words = data.lower()
        if words == 'done':
            break
        else:
            print('Error, invalid input')
print('Biggest:', biggest)
print('Smallest:', smallest)
