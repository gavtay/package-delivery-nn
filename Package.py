class Package:
    def __init__(self, packageID, packageDeliveryAddress, packageDeliveryCity, packageDeliveryState, packageDeliveryZip, packageDeliveryDeadline, packageWeight, packageStatus):
    # object properties
        self.packageID = packageID
        self.packageDeliveryAddress = packageDeliveryAddress
        self.packageDeliveryCity = packageDeliveryCity
        self.packageDeliveryState = packageDeliveryState
        self.packageDeliveryZip = packageDeliveryZip
        self.packageDeliveryDeadline = packageDeliveryDeadline
        self.packageWeight = packageWeight
        self.packageStatus = packageStatus
        self.packageDepartureTime = None
        self.packageDeliveryTime = None

    def __str__(self):
    # what is returned if object is string
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.packageID,
            self.packageDeliveryAddress,
            self.packageDeliveryCity,
            self.packageDeliveryState,
            self.packageDeliveryZip,
            self.packageDeliveryDeadline,
            self.packageWeight,
            self.packageStatus,
            self.packageDepartureTime,
            self.packageDeliveryTime
        )

    # def getPackageStatus(self):
    # determine whether the package is at the hub, en route, or delivered
