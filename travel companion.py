# 1- display a welcome message to the user
print("welcome to your travel companion !")
# 2- ask the user to enter the number of passengers and trip distance
num_of_passengers=int(input("enter number of passengers :"))
trip_distance=int(input("enter trip_distance :"))
# 3- calculate the base cost of the trip
rate_per_km=0.5
Base_cost=trip_distance*rate_per_km*num_of_passengers
# 4- ask the user if there is any cargo or not
has_cargo=input("Is there any cargo ? (yes/no) ")
# 5- check for cargo and calculate extra luggage fees if applicable
if has_cargo=="yes":
    num_of_luggage=int(input("enter the total number of luggage :"))
    free_allowance=23
    extra_fee_per_kg=10
    total_luggage_fee=0
    #loop through each back to check its weight
    for bag in range(1,num_of_luggage+1):
        bag_weight=float(input("enter the weight of the bag in kg:"))
        if bag_weight>free_allowance:
            extra_weight=bag_weight-free_allowance
            total_luggage_fee+=extra_weight*extra_fee_per_kg
else:
    total_luggage_fee=0
# 6- calculate and display the final total cost
total_cost=Base_cost+total_luggage_fee
print("total cost is $",total_cost)





