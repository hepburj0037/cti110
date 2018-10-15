# A brief description of the project
# 9/10/2018
# CTI-110 P2HW1 - Celsius Fahrenheit Converter 
# Joshua Hepburn
#
# Get the temperature in celcius.
Ctemp = float(input('Enter the tempreature in Celsius: '))

#Calculate the temperature in Celsius to Fahrenheit
Ftemp = 9/5 * Ctemp + 32

#Display the Temperature in Fahrenheit
print('The temperature in Fahrenheit is', format(Ftemp, ',.2f'))
