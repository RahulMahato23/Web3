import math

class Car:
    def __init__(self, make, model, year, speedx, speedy, speedz, x, y, z):
        self.make = make
        self.model = model
        self.year = year
        self.speedx = speedx
        self.speedy = speedy
        self.speedz = speedz
        self.x = x
        self.y = y
        self.z = z
    
    def accelerate(self, speed_incrementx,speed_incrementy,speed_incrementz):
        self.speedx += speed_incrementx
        self.speedy += speed_incrementy
        self.speedz += speed_incrementz
    
    def brake(self, speed_decrementx, speed_decrementy, speed_decrementz):
        self.speedx -= speed_decrementx
        self.speedy -= speed_decrementy
        self.speedz -= speed_decrementz
    
    def move(self):
        self.x += self.speedx
        self.y += self.speedy
        self.z += self.speedz
    
    def detect_collision(self, car2):
        distance = math.sqrt((self.x - car2.x)**2 + (self.y - car2.y)**2 + (self.z - car2.z)**2)
        if distance < 5: # assume collision if distance < 5 units
            return True
        else:
            return False
    
    def time_to_collision(self, car2):
        relative_speed = math.sqrt((self.speedx - car2.speedx)**2 + (self.speedy - car2.speedy)**2 + (self.speedz - car2.speedz)**2)
        if relative_speed == 0: # avoid division by zero
            return None
        else:
            time = math.sqrt((car2.x - self.x)**2 + (car2.y - self.y)**2 + (car2.z - self.z)**2) / relative_speed
            if time < 0: # cars are moving away from each other
                return None
            else:
                return time

# testing
car1 = Car("Hyundai", "Alto", 2021, 0, 0, 0, 10, 20, 15)
car2 = Car("Maruti", "Creta", 2019, 40, 100, 0, 95, 240, 103)

print("Initial positions:")
print("Car 1:", car1.x, car1.y, car1.z)
print("Car 2:", car2.x, car2.y, car2.z)

car1.accelerate(10, 20, 15)
car2.accelerate(5, 15, 20)

car1.move()
car2.move()

print("New positions after 1 second:")
print("Car 1:", car1.x, car1.y, car1.z)
print("Car 2:", car2.x, car2.y, car2.z)

collision = car1.detect_collision(car2)
time_to_collision = car1.time_to_collision(car2)

if collision:
    print("Collision detected!")
else:
    print("No collision detected.")

if time_to_collision is not None:
    print("Time to collision:", time_to_collision, "seconds.")
else:
    print("Cars are not moving towards each other.")
