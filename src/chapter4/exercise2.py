# Defining a new function that calculates investment with parameters c, r, n, t
def investment(c, r, n, t):

    # Parameters are:
    # c-initial amount of investment
    # r-yearly rate of interest
    # n-number of times interest is compounded per year
    # t-number of years until maturation

    # Calculating p-the final value of investment
    p = c*(1+r/n)**(t*n)

    print('Final value of investment = ', round(p, 2))
    return round(p, 2)

# calling the investment function with arguments of c, r, n, t
investment(1000, .01, 1, 1)
