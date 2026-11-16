class car:
    def move(self):
        print("The car drives on the road.")

class boat:
    def move(self):
        print("The boat sails on water")


class Drone:
    def move(self):
        print("The drone flies in the sky ")


def start_trip(vehicle):
    vehicle.move()


automobile = [car(),boat(),Drone()]

for vehicle in automobile:
    start_trip(vehicle)