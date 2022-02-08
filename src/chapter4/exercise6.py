def computepay(Hours,Rate):
    try:
        Hours = input('Enter hours: ')
        Hours = float(Hours)

        Rate = input('Enter rate: ')
        Rate = float(Rate)

        if Hours > 40:
            extra_hours = Hours-40
            extra_pay = extra_hours*1.5*Rate
            Pay = (40*Rate)+extra_pay
        else:
            Pay = Hours*Rate

        print('Pay:', Pay)

    except:
        print('Error, please enter numeric input')


computepay(45, 10)
