x = "Cost = "
try:
    people = int(input('Number of guests: '))
    if people <= 50:
        print(x, '$4,000')
    elif people <= 100:
        print(x, '$10,000')
    elif people <= 200:
        print(x, '$15,000')
    else:
        print(x, '$20,000')
except:
    print('Enter integer')
