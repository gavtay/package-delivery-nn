# Gavin Taylor
# Student ID: 011097232
# C950 - DSA2 - Task 2

# importing required files
import csv
import datetime
import Truck
from Hashtable import CreateHashTable
from Package import Package

# Open, read, and store data from delivery addresses csv file
with open("CSV/Distances.csv") as csvfile:
    CSV_Distance = csv.reader(csvfile)
    CSV_Distance = list(CSV_Distance)

# Open, read, and store data from delivery addresses csv file
with open("CSV/DeliveryAddresses.csv") as csvfile1:
    CSV_Address = csv.reader(csvfile1)
    CSV_Address = list(CSV_Address)

# Open, read, and store data from delivery addresses csv file
with open("CSV/PackageDetails.csv") as csvfile2:
    CSV_Package = csv.reader(csvfile2)
    CSV_Package = list(CSV_Package)


# load package attributes from csv
# Source:
# C950 - Webinar-3 - How to Dijkstra?
# W-3_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy_Dijkstra.py
def load_package_data(filename, hash_table):
    with open(filename) as package_info:
        packageDetails = csv.reader(package_info)

        # loop through csv file and get package details
        for package in packageDetails:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline_time = package[5]
            pWeight = package[6]
            pStatus = "At Hub"

            # package object
            pac = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline_time, pWeight, pStatus)

            # insert package data into hash table
            hash_table.insert(pID, pac)


# find distance between two addresses
def distance_in_between(x, y):
    distance = CSV_Distance[x][y]
    if distance == '':
        distance = CSV_Distance[y][x]

    return float(distance)


# get address
def extract_address(address):
    for row in CSV_Address:
        if address in row[2]:
            return int(row[0])

# 1, 2, 13, 14, 15, 19, 20, 21, 29, 30, 31, 34, 40
# 3, 6, 7, 8, 9, 10, 11, 18, 25, 26, 28, 32, 36, 38
# 4, 5, 12, 16, 17, 22, 23, 24, 27, 33, 35, 37, 39

# should be 100.5


# instantiate 3 truck objects to represent the 3 active working trucks delivering packages
truck_1 = Truck.Truck(16, 18, None, [1, 2, 13, 14, 15, 19, 20, 21, 29, 30, 31, 34, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))
truck_2 = Truck.Truck(16, 18, None, [3, 6, 7, 8, 9, 10, 11, 18, 25, 26, 28, 32, 36, 38], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))
truck_3 = Truck.Truck(16, 18, None, [4, 5, 12, 16, 17, 22, 23, 24, 27, 33, 35, 37, 39], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=5))

# instantiate package hash table
hash_table = CreateHashTable()

# Load packages into hash table
load_package_data("CSV/PackageDetails.csv", hash_table)


# function to sort packages by nearest neighbor algorithm
# also tracks mileage
def deliver_truck_packages(truck):
    # function to sort packages by nearest neighbor algorithm    # Place all packages into array of not delivered
    not_delivered = []
    # function to sort packages by nearest neighbor algorithm
    for packageID in truck.packages:
        package = hash_table.lookup(packageID)
        not_delivered.append(package)

    # function to sort packages by nearest neighbor algorithm
    truck.packages.clear()

    # function to sort packages by nearest neighbor algorithm
    while len(not_delivered) > 0:
        nextAddress = 2000
        nextPackage = None

        # function to sort packages by nearest neighbor algorithm
        for package in not_delivered:
            # if the distance for a given route is less than the previous,
            # store that address into the nextAddress variable and store package in next package, loop
            if distance_in_between(extract_address(truck.delivery_address),
                                   extract_address(package.package_delivery_address)) <= nextAddress:
                nextAddress = distance_in_between(extract_address(truck.delivery_address),
                                                  extract_address(package.package_delivery_address))
                nextPackage = package

        # add next package back to the packages array if found
        truck.packages.append(nextPackage.packageID)

        not_delivered.remove(nextPackage)

        # Takes the mileage driven to this packaged into the truck.mileage attribute
        truck.distance_traveled += nextAddress

        truck.delivery_address = nextPackage.package_delivery_address

        if truck.delivery_address == nextPackage.package_delivery_address:
            nextPackage.packageDeliveryTime = truck.time
            nextPackage.packageStatus = "En route"

        # adds the time it took to deliver the package to the truck time property of the truck class
        # math from for this was given in WGU resources
        # Updates the time it took for the truck to drive to the nearest package
        truck.time += datetime.timedelta(hours=nextAddress / 18)
        nextPackage.packageDeliveryTime = truck.time
        nextPackage.packageDepartureTime = truck.time_departed


# load the trucks
deliver_truck_packages(truck_1)
deliver_truck_packages(truck_2)
# The below line of code ensures that truck 3 does not leave until either of the first two trucks are finished
# delivering their packages
truck_3.depart_time = min(truck_1.time, truck_2.time)
deliver_truck_packages(truck_3)


class Main:
    # create an interactive CLI for the user to see the information
    menuNumber = 0
    singlePackageID = 0

    while menuNumber != 4:
        userSelectedTime = input("Please enter a time to check status of package(s). HH:MM:SS ")
        try:
            (h, m, s) = userSelectedTime.split(":")
            convert_time_delta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        except ValueError:
            print("Invalid time format. Please enter the time in HH:MM:SS.")
            continue

        print('*****--------------- WGUPS Task 2 ---------------*****')
        print('Total Truck Mileage: ' + str(truck_1.distance_traveled + truck_2.distance_traveled +
                                            truck_3.distance_traveled))
        print('Type 1 to print all Package Status and Total Mileage')
        print('Type 2 to get a Single Package Status with a time')
        print('Type 3 to get all Package Status with a time')
        print('Type 4 to exit the program')

        try:
            menuNumber = int(input())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if menuNumber == 1:
            # print all package status and total mileage
            print('Printing all package status and total mileage...')
            print('Truck, ID, Address, City, State, Zipcode, Deadline, Weight, Status, Departure Time, Delivery Time')
            for packageID in range(1, 41):
                package = hash_table.lookup(packageID)
                package.update_status(convert_time_delta)

                # added the truck to the print statement
                if packageID in truck_1.packages:
                    print('Truck 1, ' + str(package))
                elif packageID in truck_2.packages:
                    print('Truck 2, ' + str(package))
                else:
                    print('Truck 3, ' + str(package))

            print('Total mileage for route: ' +
                  str(truck_1.distance_traveled + truck_2.distance_traveled + truck_3.distance_traveled))

        if menuNumber == 2:
            # print single package status with a time
            # get input asking for what package id
            print('Printing single package status with a time of: ' + userSelectedTime)
            singlePackageID = input('What is the ID of the single package you want to search? ')
            singlePackage = hash_table.lookup(int(singlePackageID))
            singlePackage.update_status(convert_time_delta)

            # added the truck to the print statement
            if singlePackageID in truck_1.packages:
                print('Truck 1, ' + str(singlePackage))
            elif singlePackageID in truck_2.packages:
                print('Truck 2, ' + str(singlePackage))
            else:
                print('Truck 3, ' + str(singlePackage))

        if menuNumber == 3:
            # print all package status at a specific time
            print('Printing all packages status with a time of: ' + userSelectedTime)
            for packageID in range(1, 41):
                package = hash_table.lookup(packageID)
                package.update_status(convert_time_delta)

                # added the truck to the print statement
                if packageID in truck_1.packages:
                    print('Truck 1, ' + str(package))
                elif packageID in truck_2.packages:
                    print('Truck 2, ' + str(package))
                else:
                    print('Truck 3, ' + str(package))

