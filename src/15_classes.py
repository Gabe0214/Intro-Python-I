# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def myFunc(self):
        print(f"lat is: {str(self.lat)} lon is: {str(self.lon)}")

myLats = LatLon(32, 55)
myLats.myFunc()
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return(f"{self.name}, {str(self.lat)}, {str(self.lon)}")

myWaypoint = Waypoint(25, 65, "Disney")
print(myWaypoint.lon)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return(f"{self.name}, {str(self.difficulty)}, {str(self.size)}, {str(self.lat)}, {str(self.lon)}") 
myGeocache = Geocache(45,45,"Mountains","Hard", 10)
print(myGeocache.name)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint = Waypoint(41.70505, -121.51521, "Catacombs")

# print(f"{myWaypoint.name}, {str(myWaypoint.lat)}, {str(myWaypoint.lon)}")
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache(44.052137, -121.4155, "Newberry Views", 1.5, 2)

# YOUR CODE HERE

# Print it--also make this print more nicely
print(geocache)
