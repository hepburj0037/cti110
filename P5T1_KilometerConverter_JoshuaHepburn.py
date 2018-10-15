# A brief description of the project
# 9/30/2018
# CTI-110 P5T1_KilometerConverter 
# Joshua Hepburn
#

# This program converts kilometers to miles.
CONVERSION_FACTOR = 0.6214

# The main function gets a distance in kilometers and calls
# the show miles function to cinvert
def main():
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Displayed the distance converted to miles.
    show_miles(kilometers)

# The show_miles function converts the parameter km from
# kilometers to miles and displays the result.
def show_miles(km):
    # Calculate miles.
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print(km, 'kilometers equals', miles, 'mile.')

# Call the main function.
main()
