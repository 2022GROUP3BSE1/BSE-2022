prompt = 'Enter Celcius Temperature: '

celcius = input(prompt)
celcius = float(celcius)

fahrenheit = (celcius * 1.8) + 32.00

print('Temperature in fahrenheit = ',fahrenheit, 'F')