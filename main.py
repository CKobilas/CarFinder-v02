# Define Allowed Vehicles List
Allowed_Vehicles_List = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500']

# Define function to print allowed vehicles
def print_allowed_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in Allowed_Vehicles_List:
        print(vehicle)
      
# Define function to display menu
def display_menu():
  print("\n************************************\n\
  AutoCountry Vehicle Finder v0.4\n************************************")
  print("\n1. PRINT all Authorized Vehicles")
  print("2. SEARCH for Authorized Vehicle")
  print("3. ADD Authorized Vehicle")
  print("4. DELETE Authorized Vehicle")
  print("5. Exit")

# Define function to get user input on searched vehicle
def search_vehicle():
  search = input("\nPlease Enter the full Vehicle name: ")
  if search in Allowed_Vehicles_List:
    print(search, "is an authorized vehicle")
  else:
    print(search, "is not an authorized vehicle, if you received this in error please check the spelling and try again")

# Define function to add vehicle to list
def add_vehicle():
  new_vehicle = input("\nPlease Enter the full Vehicle name you would like to add: ")
  if new_vehicle in Allowed_Vehicles_List:
    print(new_vehicle, "is already an authorized vehicle")
  else:
    Allowed_Vehicles_List.append(new_vehicle)
  return new_vehicle

# Define function to delete vehicle from list
def delete_vehicle():
  delete_vehicle = input("\nPlease Enter the full Vehicle name you would like to REMOVE: ")
  choice = input("\nAre you sure you want to remove " + delete_vehicle + " from the Authorized Vehicles list?")
  if choice.lower() in ['yes', 'y']:
    if delete_vehicle in Allowed_Vehicles_List:
        Allowed_Vehicles_List.remove(delete_vehicle)
        print("You have REMOVED " + delete_vehicle + " as an authorized vehicle")
    else:
        print(delete_vehicle, "is not in the authorized vehicles list.")
  
# Define main function
def main():
    while True:
        display_menu()
        choice = input("\nPlease Enter the following number below from the following menu: ")
        if choice == '1':
            print_allowed_vehicles()
        elif choice == '2':
            search_vehicle()
        elif choice == '3':
            new_vehicle = add_vehicle()
            print("\nYou have added " + new_vehicle + " as an authorized vehicle")
        elif choice == '4':
            delete_vehicle()
        elif choice == '5':
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
  main()
