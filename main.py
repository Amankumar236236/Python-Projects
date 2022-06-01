#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip Calculator!")
Bill=float(input("What was the total bill? In rupee\n"))
Tip = int(input("How much tip would you like to give? 10, 12, 0r 15? \n"))
split=int(input("How many people to split the bill?\n"))
Bill_with_Tip= Tip/100 *Bill + Bill
print(Bill_with_Tip)
Bill_Per_Person= (Bill_with_Tip/split)
Final_amount=round(Bill_Per_Person,2)
print(f"Each person should pay {Final_amount} rupee")