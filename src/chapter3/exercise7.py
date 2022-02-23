location = input("Location= ").lower()
pay = input("Pay= ")

# John's decisions
a = "Decision: Without a doubt, I can take it"
b = "Decision: Sure, I can work with this"
c = "Decision: No thanks, I can find something better"
d = "Decision: No way!"

try:
    pay = int(pay)
    pass

except:
    print("Error, enter numeric value for pay")
    exit()

# KAMPALA RESPONSE
if location == "kampala":
    if pay >= 10000000:
        print(b)
    else:
        print(d)
    exit()
else:
    pass
# MBARARA RESPONSE
if location == "mbarara":
    if pay > 4000000:
        print(a)
    else:
        print(c)
# SPACE RESPONSE
elif location == "space":
    print(a)
# ANY OTHER'S RESPONSE
else:
    if pay >= 6000000:
        print(b)
    else:
        print(c)
