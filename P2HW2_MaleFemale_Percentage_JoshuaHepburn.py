# A brief description of the project
# 9/10/2018
# CTI-110 P2HW2 - Male Female Percentage
# Joshua Hepburn
#
# Get the total amount of people males and females.
group = float(input('Enter the number of males and females: '))

# Get the total number of males.
males = float(input('Enter the number of males: '))

# Get the total number of females.
females = float(input('Enter the number of females: '))

# Calculate the percentage of males.
malepercentage = males / group

# Calculate the percentage of females.
femalepercentage = females / group

# Display the Percent of males.
print('The malepercentage is %', format(malepercentage, '%'))

# Display the Percent of females.
print('The femalepercentage is %', format(femalepercentage, '%'))
