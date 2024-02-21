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
def loadPackageAttributes(CSVPackageDetails):
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
truck_2 = Truck.Truck(16, 18, None, [3, 6, 7, 8, 9, 10, 11, 18, 25, 26, 28, 32, 36, 38], 0.0, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))
truck_3 = Truck.Truck(16, 18, None, [4, 5, 12, 16, 17, 22, 23, 24, 27, 33, 35, 37, 39], 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))

def truckDeliverPackages(truck_1, truck_2, truck3):
    if truck_1 == "At Hub":


class Main:
# create an interactive CLI for the user to see the information
    print('*****--------------- WGUPS Task 2 ---------------*****')
    print('Truck 1: ' + 'En Route')
    print('Truck 2: ' + 'En Route')
    print('Truck 3: ' + 'Hub')
    print('ID | Address | City | State | Zipcode | Deadline | Weight | Special Note | Status | Delivery Time')
    print('2 | 123 Rod Rd | FTW | TX | 76126 | 10:00 | 12.5lbs | ... | Delivered | 08:32')
