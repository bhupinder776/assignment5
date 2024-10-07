# Car class definition
class Car:
    def __init__(self, registration_number, max_speed):
        """
        Class initializer that sets registration number and maximum speed.
        Current speed and travelled distance are set to zero initially.
        """
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        """
        Method to change the speed of the car by a given value.
        Speed cannot exceed max_speed or go below zero.
        """
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def __str__(self):
        """
        String representation of the car's properties.
        """
        return (f"Car details:\n"
                f"Registration Number: {self.registration_number}\n"
                f"Maximum Speed: {self.max_speed} km/h\n"
                f"Current Speed: {self.current_speed} km/h\n"
                f"Travelled Distance: {self.travelled_distance} km")


# Main program
def main():
    # Create a new car object with the specified properties
    new_car = Car("ABC-123", 142)

    # Accelerating the car
    new_car.accelerate(30)
    print(f"After accelerating by +30 km/h, current speed is: {new_car.current_speed} km/h")

    new_car.accelerate(70)
    print(f"After accelerating by +70 km/h, current speed is: {new_car.current_speed} km/h")

    new_car.accelerate(50)
    print(f"After accelerating by +50 km/h, current speed is: {new_car.current_speed} km/h")

    # Emergency brake
    new_car.accelerate(-200)
    print(f"After emergency brake (-200 km/h), current speed is: {new_car.current_speed} km/h")


if __name__ == "__main__":
    main()
