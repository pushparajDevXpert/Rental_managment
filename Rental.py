# iInput we need from the user
# total rent of house/hotel/pg
# Total food ordered for snacking 
# total elericity bill
# total electricity spend
# charge per unit
# number person in house/hotel/pg
#  output
# Total amount to be paid by per person

rent=int(input("Enter the rent of house/hotel/pg ="))
food=int(input("Enter the amount of ordered ="))
electricity_spend=int(input("Enter the total electricity spended ="))
charge_per_unit=int(input("Enter the charge per unit = "))
persons=int(input("Enter the number of person living in house/hotel/pg ="))

total_bill=electricity_spend*charge_per_unit

output=(food+rent+total_bill)// persons

print("Each person will pay=",output)

