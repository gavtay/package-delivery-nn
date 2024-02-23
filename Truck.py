class Truck:
    def __init__(self, max_load, truck_speed, load_packages, packages, distance_traveled, delivery_address,
                 time_departed):
        # object properties
        self.max_load = 16
        self.truck_speed = 18
        self.load_packages = load_packages
        self.packages = packages
        self.distance_traveled = distance_traveled
        self.delivery_address = delivery_address
        self.time_departed = time_departed
        self.time = time_departed

    def __str__(self):
        # what should be returned when object is represented as string
        return "%s, %s, %s, %s, %s, %s, %s" % (
            self.max_load,
            self.truck_speed,
            self.load_packages,
            self.packages,
            self.distance_traveled,
            self.delivery_address,
            self.time_departed
        )
