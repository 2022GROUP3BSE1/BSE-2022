try:
    Hours = input('Enter hours: ')
    Hours = float(Hours)

    Rate = input('Enter rate: ')
    Rate = float(Rate)

    if Hours > 40:
        extra_hours = Hours-40
        extra_pay = extra_hours*1.5*Rate  # For extra pay, rate is 1.5 times
        Pay = (40*Rate)+extra_pay         # Total pay = (pay for 40 hours) + extra pay
    else:
        Pay = Hours*Rate

    print('Pay:', Pay)

except:
    print('Error, please enter numeric input')
