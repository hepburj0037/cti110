# This project will tell if the user went over, under or equal to their budget
# 9/26/2018
# CTI-110 P4HW1 - Budget Analysis
# Joshua Hepburn
#

# Ask the user for their budget.
budget = float(input("What is your budget for the month: "))

# Create an extra expenes code.
extraexpenses = "y"

# Crate a total for how much they spend.
finalexpense = 0

# Create a loop to ask if there are extra expenses.
while extraexpenses == "y":
    expense = float(input("Enter the expense: "))
    
    # Continue to add the numbers up.
    finalexpense += expense

    # Ask if there are anymore epenses.
    extraexpenses = input("Do you have anymore expenses? Hit y for yes, n for no: ")

#Give feedback if the user has gone under, over, or matched exactly with their budget.
if finalexpense > budget:
    print("You were over your budget of $",format(budget,",.2f"),"by $",format(finalexpense - budget,",.2f"),".")
elif budget > finalexpense:
    print("You were under your budget of $",format(budget,",.2f"),"by $",format(budget - finalexpense,",.2f"),".")
else:
    print("You spent the exact amount equal to your budget of",format(budget,",.2f"),".")
