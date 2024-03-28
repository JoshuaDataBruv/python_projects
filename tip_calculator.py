#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇



# Here I created the tip calculator
def bill(amount, tip, table_size):
    bill_with_tip = (amount / table_size) * (1 + tip)

    # Here I rounded and formatted the bill amount
    rounded_bill = round(bill_with_tip, 2)
    formatted_bill = "{:.2f}".format(rounded_bill)

    return print(formatted_bill)

# Here I called the function that will show the bill amount including tip in the console
bill(150, 0.12, 5)

# One way to make this more complex is to ask for amount, tip, and table_size inputs.