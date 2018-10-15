# Calculating feet to inches. 
# 9/30/2018
# CTI-110 P5T2_FeetToInches 
# Joshua Hepburn
#

# Constant for the number of nches per foot.
INCHES_PER_FOOT = 12

# Main function
def main():
    # Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    # Convert feet to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

# The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Call the main function
main()
