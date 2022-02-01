c = int(input('initial amount of investment: '))
r = float(input('yearly rate or interest '))
t = float(input('number of years until maturation '))
n = float(input(' number of times the interest is compounded per year '))
x = t*n
p = round(c*(1+r/n)**x, 2)
print('p', p)
