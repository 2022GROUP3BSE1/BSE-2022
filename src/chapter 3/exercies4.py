try:
    people = int(input('Number of guests: '))
    if people <= 50:
        print('$4,000')
    elif people <= 100:
        print('$10,000')
    elif people <= 200:
        print('$15,000')
    else:
        print('$20,000')
except:
    print('Enter integer')