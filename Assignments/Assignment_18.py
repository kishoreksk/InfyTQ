# A traveler on a visit to India is in need of some Indian Rupees (INR) but he has money belonging to another currency. He wants to know how much money he should provide in the currency he has, to get the specified amount in INR.
#
#
# Write a python program to implement a currency calculator which accepts the amount needed in INR and the name of the currency which the traveler has. The program should identify and display the amount the traveler should provide in the currency he has, to get the specified amount in INR.
#
#
# Note: Use the forex information provided in the table below for the calculation. Consider that only the currency names mentioned in the table are valid. For any invalid currency name, display -1.
#
#
# Currency	Equivalent of 1.00 INR
# Euro	0.01417
# British Pound	0.0100
# Australian Dollar	0.02140
# Canadian Dollar	0.02027
# Also identify the test data and use it to test the program.
#

# Solution:

#PF-Tryout

def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    #write your logic here
    if(current_currency_name == 'Euro'):
        current_currency_amount = amount_needed_inr*0.01417
    elif(current_currency_name == 'British Pound'):
        current_currency_amount = amount_needed_inr*0.0100
    elif(current_currency_name == 'Australian Dollar'):
        current_currency_amount = amount_needed_inr*0.02140
    elif(current_currency_name == 'Canadian Dollar'):
        current_currency_amount = amount_needed_inr*0.02027
    else:
        current_currency_amount = -1
    return current_currency_amount


#Provide different values for amount_needed_inr,current_currency_name and test your program
currency_needed=convert_currency(3500,"British Pound")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")