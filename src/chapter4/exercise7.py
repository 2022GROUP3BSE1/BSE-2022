def computegrade(score):
    score = input('Enter the score: ')
    try:
        score = float(score)
        if score > 1.0 or score < 0.0:
            raise ValueError
        elif score < 0.6:
            grade = 'F'
        elif score < 0.7:
            grade = 'D'
        elif score < 0.8:
            grade = 'C'
        elif score < 0.9:
            grade = 'B'
        else:
            grade = 'A'

        print(grade)
    except:
        print('bad score')

    return grade


computegrade(0.9)

