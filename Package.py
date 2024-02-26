class Package:
    def __init__(self, package_id, package_delivery_address, package_delivery_city, package_delivery_state,
                 package_delivery_zip, package_delivery_deadline, package_weight, package_status):
        # object properties
        self.packageID = package_id
        self.package_delivery_address = package_delivery_address
        self.packageDeliveryCity = package_delivery_city
        self.packageDeliveryState = package_delivery_state
        self.packageDeliveryZip = package_delivery_zip
        self.packageDeliveryDeadline = package_delivery_deadline
        self.packageWeight = package_weight
        self.packageStatus = package_status
        self.packageDepartureTime = None
        self.packageDeliveryTime = None

    def __str__(self):
        # what is returned if object is string
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.packageID,
            self.package_delivery_address,
            self.packageDeliveryCity,
            self.packageDeliveryState,
            self.packageDeliveryZip,
            self.packageDeliveryDeadline,
            self.packageWeight,
            self.packageStatus,
            self.packageDepartureTime,
            self.packageDeliveryTime
        )

    # determine whether the package is at the hub, en route, or delivered
    def update_status(self, convert_timedelta):
        if self.packageDeliveryTime < convert_timedelta:
            self.packageStatus = "Delivered"
        elif self.packageDepartureTime > convert_timedelta:
            self.packageStatus = "En route"
        else:
            self.packageStatus = "At Hub"