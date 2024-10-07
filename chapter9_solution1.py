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

    # Print all properties of the new car
    print(new_car)


if __name__ == "__main__":
    main()
