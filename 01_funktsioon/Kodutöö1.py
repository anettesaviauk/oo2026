class Aircraft:
    def __init__(self, model, fuel, speed, fuel_consumption_per_km):
        self.model = model
        self.fuel = fuel
        self.speed = speed
        self.fuel_consumption_per_km = fuel_consumption_per_km

    def fly(self, destination, distance):
        fuel_needed = distance * self.fuel_consumption_per_km
        flight_time = distance / self.speed

        print(f"\n{self.model} valmistub lennuks sihtkohta {destination}.")
        print(f"Lennu kaugus: {distance} km")
        print(f"Eeldatav lennuaeg: {round(flight_time, 2)} tundi")

        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print("Lend saab toimuda!")
            print(f"Kütust kulus: {round(fuel_needed, 2)} L")
            print(f"Alles jäänud kütus: {round(self.fuel, 2)} L")
        else:
            print("Lennuks pole piisavalt kütust!")
            
plane1 = Aircraft("AirBaltic Airbus A220-300", 10000, 870, 2.4)
plane1.fly("Malaga", 3000)

plane1 = Aircraft("AirBaltic Airbus A220-300", 10000, 870, 2.4)
plane1.fly("Tenerife", 4800)