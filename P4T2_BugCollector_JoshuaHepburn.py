# Calculating the total bugs for 7 days.
# 9/26/2018
# CTI-110 P4T2 - Bug Collector
# Joshua Hepburn
#

# Initialize accumulator.
total = 0

# Get the bugs collected for each day.
for day in range(1, 8):
    # Promt the user.
    print('Enter the bugs collected on day', day, ':')

    # Input the number of bugs total.
    bugs = int(input())
    total += bugs

# Display the total bugs.
print('Ypu collected a total of', total, 'bugs.')
