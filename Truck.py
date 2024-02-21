class Truck:
    def __init__(self, maxLoad, truckSpeed, loadPackages, packages, distanceTraveled, deliveryAddress, timeDeparted, truckStatus):
        # object properties
        self.maxLoad = 16
        self.truckSpeed = 18
        self.loadPackages = loadPackages
        self.packages = packages
        self.distanceTraveled = distanceTraveled
        self.deliveryAddress = deliveryAddress
        self.timeDeparted = timeDeparted
        self.truckStatus = "At Hub"

    def __str__(self):
        # what should be returned when object is represented as string
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.maxLoad,
            self.truckSpeed,
            self.loadPackages,
            self.packages,
            self.distanceTraveled,
            self.deliveryAddress,
            self.timeDeparted,
            self.truckStatus
        )
