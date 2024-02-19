class Package:
    def __init__(self, packageID, packageDestination, packageStatus):
    # object properties
        self.packageID = packageID
        self.packageDestination = packageDestination
        self.packageStatus = packageStatus

    def __str__(self):
    # what is returned if object is string


    def getPackageStatus(self):
    # determine whether the package is at the hub, en route, or delivered
