
 #You have x no. of 5 rupee coins and y no. of 1 rupee coins.
 #You want to purchase an item for amount z.
 #The shopkeeper wants you to provide exact change.
 ##You want to pay using minimum number of coins.
##How many 5 rupee coins and 1 rupee coins will you use?
#If exact change is not possible then display -1.


#Solution

def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0

    five_needed = int(rupees_to_make // 5)
    one_needed = rupees_to_make % 5

    remaining_five = no_of_five
    remaining_one = no_of_one

    if (five_needed > remaining_five):
            one_needed += 5 * (five_needed - remaining_five)
            remaining_five = 0
    else:
            remaining_five -= five_needed
    if (one_needed > remaining_one):
            return -1
    else:
            remaining_one -= one_needed
            return "Fives {0}, Ones {1}".format(no_of_five - remaining_five,no_of_one - remaining_one)

# Use the below given print statements to display the output
# Also, do not modify them for verification to work.

# Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
print(make_amount(27, 8, 5))