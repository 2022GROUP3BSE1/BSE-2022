c=input('Enter Initial amount of investment: ')
c=float(c)

r=input('Enter yearly rate of interest: ')
r=float(r)

t=input('Enter number of Years until maturation: ')
t=float(t)

n=input('Enter number of times interest is compounded per year: ')
n=float(n)

p=c*(1+r/n)**(t*n)

print('>>> Final value of investment = ',round(p,2))