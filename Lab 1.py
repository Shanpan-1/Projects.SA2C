class Biome:
    def __init__ (self, place):
        self.place = place
    
    def on(self):
        print(f"Hello I am on plant {self.place} Here are the biome I have.")

class Ocean(Biome):
    def __init__ (self, place, water):
        super().__init__ (place)
        self.water = water

    def on(self):
        print(f"Hello I am on the planet {self.place} and my power is {self.water}")
class Dessert(Biome):
    def __init (self, place, heat):
        super().__init__ (place)
        self.heat = heat

    def on(self):
        print(f"Hello I am the {self.place} biome and I have the {self.heat} power")
class Pasific(Ocean):
    def __init (self, place, power, type):
        super().__init__(place, power)
        self.type = type
    
    def on(self):
        print(f"Hello I am a {self.type} and I live on the planet {self.place} which has the {self.power} power")
