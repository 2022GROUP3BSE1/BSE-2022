score = input('Enter the score: ')
try:
    score = float(score)
    if score > 1.0 or score < 0.0:
        raise ValueError
    elif score < 0.6:
        print('F')
    elif score < 0.7:
        print('D')
    elif score < 0.8:
        print('C')
    elif score < 0.9:
        print('B')
    else:
        print('A')
except:
    print('bad score')
