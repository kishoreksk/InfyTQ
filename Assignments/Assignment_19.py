# FoodCorner home delivers vegetarian and non-vegetarian combos to its customer based on order.
#
# A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate. Their non-veg combo is really famous that they get more orders for their non-vegetarian combo than the vegetarian combo.
#
# Apart from the cost per plate of food, customers are also charged for home delivery based on the distance in kms from the restaurant to the delivery point. The delivery charges are as mentioned below:
#
# Distance in kms	Delivery charge in Rs per km
# For first 3kms	        0
# For next 3kms	            3
# For the remaining	        6
#
#
# Given the type of food, quantity (no. of plates) and the distance in kms from the restaurant to the delivery point, write a python program to calculate the final bill amount to be paid by a customer.
#
# The below information must be used to check the validity of the data provided by the customer:
#
#
# Distance in kms must be greater than 0.
# Quantity ordered should be minimum 1.
# If  of the input is invalid, the bill amount should be considered as -1.


#Solution

# PF-Assgn-19

def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0
    x = food_type
    y = quantity_ordered
    z = distance_in_kms
    # write your logic here
    if (x == 'V'):
        if (y > 0):
            if (z <= 3 and z>0 ):
                bill_amount = (y * 120)
            elif (z > 3 and z <= 6):
                total_km = z - 3
                bill_amount = (y * 120) + (total_km * 3)
            elif (z>6):
                remain_km = z - 6
                bill_amount = (y * 120) + (3 * 3) + (6 * remain_km)
            else:
                bill_amount =-1
        else:
            bill_amount = -1
    elif (x == 'N'):
        if (y > 0):
            if (z <= 3 and z>0):
                bill_amount = (y * 150)
            elif (z > 3 and z <= 6):
                total_km = z - 3
                bill_amount = (y * 150) + (total_km * 3)
            elif(z>6):
                remain_km = z - 6
                bill_amount = (y * 150) + (3 * 3) + (6 * remain_km)
            else:
                bill_amount = -1
        else:
            bill_amount = -1
    else:
        bill_amount = -1

    return bill_amount


# Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount = calculate_bill_amount("n", 2, 8)
print(bill_amount)
