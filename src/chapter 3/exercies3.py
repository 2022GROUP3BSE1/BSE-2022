marks = input('enter marks: ')
try:
    marks = float(marks)
    if 0.0 < marks > 1.0:
        print('Bad score')

    elif marks >= 0.9:
        print("A")
    elif marks >= 0.8:
        print('B')
    elif marks >=0.7:
        print('C')
    elif marks >= 0.6:
        print('D')
    elif marks < 0.6:
        print('f')

except:
    print('Bad score')




