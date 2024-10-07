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

    def drive(self, hours):
        """
        Method to drive the car for a given number of hours.
        This increases the travelled distance based on the current speed.
        """
        if self.current_speed > 0:
            distance_travelled = self.current_speed * hours
            self.travelled_distance += distance_travelled
            print(f"Driven for {hours} hours at {self.current_speed} km/h, travelled {distance_travelled:.1f} km.")
        else:
            print("The car is not moving, current speed is 0 km/h.")

    def __str__(self):
        """
        String representation of the car's properties.
        """
        return (f"Car details:\n"
                f"Registration Number: {self.registration_number}\n"
                f"Maximum Speed: {self.max_speed} km/h\n"
                f"Current Speed: {self.current_speed} km/h\n"
                f"Travelled Distance: {self.travelled_distance:.1f} km")


# Main program
def main():
    # Create a new car object with the specified properties
    new_car = Car("ABC-123", 142)

    # Accelerating the car
    new_car.accelerate(60)
    print(f"After accelerating, current speed is: {new_car.current_speed} km/h")

    # Driving the car for 1.5 hours
    new_car.drive(1.5)
    print(f"Total travelled distance: {new_car.travelled_distance:.1f} km")

    # Driving again after accelerating further
    new_car.accelerate(40)  # Speed up to 100 km/h
    new_car.drive(2)  # Drive for 2 hours
    print(f"Total travelled distance: {new_car.travelled_distance:.1f} km")

    # Emergency brake and try driving at 0 speed
    new_car.accelerate(-200)
    new_car.drive(1)  # Drive for 1 hour at 0 speed
    print(f"Total travelled distance: {new_car.travelled_distance:.1f} km")


if __name__ == "__main__":
    main()
