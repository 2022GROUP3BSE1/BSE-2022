age = input('Enter your age: ')
try:
    age = int(age)
    if age >= 18:
        print('You can vote')
    elif age < 0:
        print('You are a time traveller')
    else:
        print('Too young to vote')
except:
    print('Enter numeric input')
