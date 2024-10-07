# Program to store and fetch airport data

# Dictionary to store airport data
airports = {}


def add_airport():
    """Function to add a new airport to the dictionary."""
    icao_code = input("Enter the ICAO code of the airport: ").upper()
    name = input("Enter the name of the airport: ")

    # Check if the ICAO code already exists
    if icao_code in airports:
        print(f"Airport with ICAO code {icao_code} already exists.")
    else:
        airports[icao_code] = name
        print(f"Airport {name} with ICAO code {icao_code} added.")


def fetch_airport():
    """Function to fetch the name of the airport by its ICAO code."""
    icao_code = input("Enter the ICAO code of the airport: ").upper()

    # Check if the ICAO code exists
    if icao_code in airports:
        print(f"The name of the airport with ICAO code {icao_code} is {airports[icao_code]}.")
    else:
        print(f"No airport found with ICAO code {icao_code}.")


def main():
    """Main function to run the program."""
    while True:
        print("\nAirport Data Management")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            add_airport()
        elif choice == '2':
            fetch_airport()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
