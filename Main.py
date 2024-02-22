# Student ID: 011097232

# importing required files
import csv
import datetime
import Hashtable
import Package
import Truck

# Open, read, and store data from deliveryaddresses csv file
with open('CSV/DeliveryAddresses.csv') as csvfile:
    CSVAddresses = csv.reader(csvfile)
    CSVAddresses = list(CSVAddresses)

# Open, read, and store data from distances csv file
with open('CSV/Distances.csv') as csvfile:
    CSVDistances = csv.reader(csvfile)
    CSVDistances = list(CSVDistances)

# Open, read, and store data from packagedetails csv file
with open('CSV/PackageDetails.csv') as csvfile:
    CSVPackageDetails = csv.reader(csvfile)
    CSVPackageDetails = list(CSVPackageDetails)

# instantiate hash table
hash_table = Hashtable.CreateHashTable()

# load package attributes from csv
# Source:
# C950 - Webinar-3 - How to Dijkstra?
# W-3_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy_Dijkstra.py
def loadPackageAttributes(CSVPackageDetails, hash_table):
    with open(CSVPackageDetails) as csvfile:
        packageDetails = csv.reader(csvfile)

        # loop through csv file and get package details
        for package in packageDetails:
            pacID = int(package[0])
            pacAdd = package[1]
            pacCity= package[2]
            pacState = package[3]
            pacZip = package[4]
            pacDeadline = package[5]
            pacWeight = package[6]
            pacStatus = "At Hub"

            # package object
            pac = Package(pacID, pacAdd, pacCity, pacState, pacZip, pacDeadline, pacWeight, pacStatus)

            # insert package details into hash table
            CSVPackageDetails.insert(pacID, pac)

# load hash table with package details
loadPackageAttributes('CSV/PackageDetails.csv', hash_table)



def getDistance(x, y):
# get the distance from Distances.csv
    distanceBetween = CSVDistances[x][y]
    if distanceBetween == '':
        distanceBetween == CSVDistances[y][x]

    return float(distanceBetween)

def getAddress(address):
# get the row from DeliveryAddresses.csv string literal
    for row in CSVAddresses:
        if address in row[2]:
            return int(row[0])


# instantiate 3 truck objects to represent the 3 active working trucks delivering packages
truck_1 = Truck.Truck(16, 18, None, [1, 2, 13, 14, 15, 19, 20, 21, 29, 30, 31, 34, 40], 0.0, "4001 South 700 East", datetime.timedelta(hours=8))
truck_2 = Truck.Truck(16, 18, None, [3, 6, 7, 8, 9, 10, 11, 18, 25, 26, 28, 32, 36, 38], 0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=21))
truck_3 = Truck.Truck(16, 18, None, [4, 5, 12, 16, 17, 22, 23, 24, 27, 33, 35, 37, 39], 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))

# function to sort packages by nearest neighbor algorithm
def truckDeliverPackages(truckx):
    #create an empty array that the packages will temporarily be placed in to be sorted
    notDeliveredArray = []
    #loop through the packages in the truck objects packages attribute, append the package to notDeliveredArray
    for packageID in truck.packages:
        package = hash_table.lookup(packageID)
        notDeliveredArray.append(package)

    # clear the trucks package list so the packages can be placed in the correct order
    truck.packages.clear()

    # loop through notDeliveredArray, sorting packages until the array is empty
    while len(notDeliveredArray) > 0:
        nextAddressDistance = 2000
        nextPackage = None

        # loop through the notDeliveredArray which is populated with each trucks packages
        for package in notDeliveredArray:
            # if the distance for a given route is less than the previous, store that address into the next_address variable and store package in next package, loop
            if getDistance(getAddress(truck.deliveryAddress), getAddress(package.packageDeliveryAddress)) <= nextAddressDistance:
                nextAddressDistance = getDistance(getAddress(truck.deliveryAddress), getAddress(package.packageDeliveryAddress))
                nextPackage = package

        # add next package back to the packages array
        truck.packages.append(nextPackage.ID)

        # remove next package from notDeliveredArray
        notDeliveredArray.remove(nextPackage)

        # add the distance to the next address to the distanceTraveled property of the truck class
        truck.distanceTraveled += nextAddressDistance

        # change the trucks current location to the address that it is going to
        truck.currentLocation = nextPackage.address

        # adds the time it took to deliver the package to the truck time property of the truck class
        # math from for this was given in WGU resources
        truck.truckTime += datetime.timedelta(hours=nextAddressDistance / 18)
        nextPackage.packageDeliveryTime = truck.truckTime
        nextPackage.packageDepartureTime = truck.timeDeparted

# load the trucks
truckDeliverPackages(truck_1)
truckDeliverPackages(truck_2)

#load the third truck after truck_1 or truck_2 return back to the hub
truck_3.timeDeparted = min(truck_1.truckTime, truck_2.truckTime)
truckDeliverPackages(truck_3)

class Main:
# create an interactive CLI for the user to see the information
    print('*****--------------- WGUPS Task 2 ---------------*****')
    print('Truck 1: ' + 'En Route')
    print('Truck 2: ' + 'En Route')
    print('Truck 3: ' + 'Hub')
    print('ID | Address | City | State | Zipcode | Deadline | Weight | Special Note | Status | Delivery Time')
    print('2 | 123 Rod Rd | FTW | TX | 76126 | 10:00 | 12.5lbs | ... | Delivered | 08:32')
