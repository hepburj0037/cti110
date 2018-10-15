# Changing Celsius to Farenheit.
# 9/26/2018
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Joshua Hepburn
#

# This will show the converted table.
print("This table shows the Celsius temperatures 0 through 20.")

# Seperate each side.
print("Celcius temperature\tFarenheit Equal")
print("----------------------------------------")

# Set up range to be changed.
for celciustemperature in range(21):

    # Type formula to convert.
    farenheittemperatureexchange = ( 9 / 5 ) * celciustemperature + 32

    # Show celcius and farenheit converted on the table.
    print(celciustemperature,"\t\t\t\t", format(farenheittemperatureexchange,".1f"))
