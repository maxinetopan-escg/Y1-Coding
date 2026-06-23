class Snowglobe():
    def __init__(self, d, m, s):# create the constructor, which will take in the values:
        self.diameter = d
        self.material = m
        self.scene = s

    def Shake(self):
        print(f"the {self.material} is falling over the {self.scene}")

asdaSnowglobe = Snowglobe(12.5, "fluff", "small cottage")
radSnowglobe = Snowglobe(6000000, "shards of metal", "someone surfing on lava")

asdaSnowglobe.Shake()
radSnowglobe.Shake()
    


# class Taxi():
#     def __init__(self, colour, seats, model):
#         self.colour = colour
#         self.numOfSeats = seats
#         self.model = model
#         self.passenger = ""
#         self.destination = ""

#     def PickUpPassenger(self, passengerName, passengerDestination):
#         self.passenger = passengerName
#         self.destination = passengerDestination

#     def GoToDestination(self):
#         print(f"Taking {self.passenger} to {self.destination}")


# audi = Taxi("red", 5, "audiTT")
# # audi.PickUpPassenger("Max", "Lewes")
# audi.GoToDestination()