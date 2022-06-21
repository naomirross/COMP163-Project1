# Author: Naomi Ross
# COMP163, Section 001
#
#
# CONSTANTS set below
WAREHOUSE_LOCATION = 0
MAX_PICKUP_DISTANCE_AT_WAREHOUSE = 5
MIN_PICKUP_DISTANCE_AT_WAREHOUSE = -5
MAX_PICKUP_DISTANCE_NOT_AT_WAREHOUSE = 10
MIN_PICKUP_DISTANCE_NOT_AT_WAREHOUSE = -10
MAX_RETURNS_TO_WAREHOUSE = 3
TOTAL_MOVING_TRUCK_CAPACITY = 1600.0
# variables set below
truck_is_at_warehouse = True
num_current_warehouse_storage = 0
times_returned_to_warehouse = 0
num_remaining_truck_storage = 0
current_truck_location = 0
next_pickup_distance = 0
next_pickup_size = 0
# rest of code below
while times_returned_to_warehouse < MAX_RETURNS_TO_WAREHOUSE:

    while truck_is_at_warehouse == True:
        next_pickup_distance = float(input("Where is the next pickup? "))
        next_pickup_size = float(input("How large is the next pickup? "))

        if MIN_PICKUP_DISTANCE_AT_WAREHOUSE <= next_pickup_distance <= MAX_PICKUP_DISTANCE_AT_WAREHOUSE:
            num_current_warehouse_storage += next_pickup_size
            num_remaining_truck_storage = TOTAL_MOVING_TRUCK_CAPACITY - next_pickup_size
            current_truck_location = next_pickup_distance
            truck_is_at_warehouse = False
            print(f"Pickup at: {next_pickup_distance}, Size: {next_pickup_size:.1f} cubic feet")

        else:
             print("Declined.")
             
    while truck_is_at_warehouse == False:
        next_pickup_distance = float(input("Where is the next pickup? "))
        next_pickup_size = float(input("How large is the next pickup? "))
        num_remaining_truck_storage -= next_pickup_size

        if num_remaining_truck_storage < 0 or next_pickup_distance > MAX_PICKUP_DISTANCE_NOT_AT_WAREHOUSE or next_pickup_distance < MIN_PICKUP_DISTANCE_NOT_AT_WAREHOUSE:
            num_remaining_truck_storage += next_pickup_size
            times_returned_to_warehouse += 1
            truck_is_at_warehouse = True
            print("Declined.")
            print(f"Drop-off Size: {1600-num_remaining_truck_storage:.1f} cubic feet")

        elif next_pickup_distance < (current_truck_location - 2) or next_pickup_distance > (current_truck_location + 2):
            # if the next pickup distance is greater than/less than the warehouse location ( 0 ) and on
            # the way to the warehouse(in between the current truck location and the warehouse) do the following
            if (current_truck_location > WAREHOUSE_LOCATION and WAREHOUSE_LOCATION <= next_pickup_distance <= current_truck_location) or (current_truck_location < WAREHOUSE_LOCATION and current_truck_location <= next_pickup_distance <= WAREHOUSE_LOCATION):
                num_current_warehouse_storage += next_pickup_size
                current_truck_location = next_pickup_size
                print(f"Pickup at: {next_pickup_distance}, Size: {next_pickup_size:.1f} cubic feet")
                continue
            else:
                num_remaining_truck_storage += next_pickup_size
                times_returned_to_warehouse += 1
                truck_is_at_warehouse = True
                print("Declined.")
                print(f"Drop-off Size: {1600-num_remaining_truck_storage:.1f} cubic feet")
                
        else:
            num_current_warehouse_storage += next_pickup_size
            current_truck_location = next_pickup_distance
            print(f"Pickup at: {next_pickup_distance}, Size: {next_pickup_size:.1f} cubic feet")
print(f"All Done. Total storage amount: {num_current_warehouse_storage} cubic feet")
