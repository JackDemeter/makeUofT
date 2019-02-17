# takes in how many cars are at a certain location and determines if a switch is required.

"""
Required functions:
    - Determine if a light switching is required
    - Determine pedestrians currently present
    - Object format?
"""


class Light:
    def __init__(self, pair = [], opposite=[]):
        self.pair = pair
        self.opposites = opposite
        self.persons = 0
        self.cars = 0
        self.light = False

    # accessors
    def getCars(self):
        return self.cars
    def crossing(self):
        return humans != 0

    def switch(self):
        self.light = not self.light

    # in case any issues occur, link to button feed?
    def reset(self):
        self.light = False
        for light in self.pair:
            light.setLow()
        for light in self.opposite:
            light.setHigh()
    # Set the lights manually, helper methods for reset
    def setHigh(self):
        self.light = True
    def setLow(self):
        self.light = False

    def operate(self):
        self.light()