class Veichle:
    def __init__(self,name,max_speed,mileage):
     self.name= name
     self.max_speed=max_speed
     self.mileage=mileage 
class Bus(Veichle):
        pass
School_bus=Bus("School Volvo",180,12)
print("Veichle Name:", School_bus.name,"Speed",School_bus.max_speed,
      "Mileage:", School_bus.mileage)