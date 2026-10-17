
import random

def calculate_fare(cab_rate, distance):
    return cab_rate * distance


while True:
    print("\n===== CAB BOOKING CHATBOT =====")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        # Select cab type
        print("\nChoose Cab Type:")
        print("1. Auto - Rs.12/km")
        print("2. Sedan - Rs.18/km")
        print("3. SUV - Rs.25/km")

        cab_choice = input("Enter cab choice: ")

        if cab_choice == "1":
            cab_type = "Auto"
            rate = 12
        elif cab_choice == "2":
            cab_type = "Sedan"
            rate = 18
        elif cab_choice == "3":
            cab_type = "SUV"
            rate = 25
        else:
            print("Invalid cab choice. Please try again.")
            continue

        # Predefined routes
        print("\nChoose Route:")
        print("1. Pune Station to Shivajinagar (5 km)")
        print("2. Swargate to Kothrud (8 km)")
        print("3. Hinjawadi to Wakad (10 km)")

        route_choice = input("Enter route choice: ")

        if route_choice == "1":
            source = "Pune Station"
            destination = "Shivajinagar"
            distance = 5
        elif route_choice == "2":
            source = "Swargate"
            destination = "Kothrud"
            distance = 8
        elif route_choice == "3":
            source = "Hinjawadi"
            destination = "Wakad"
            distance = 10
        else:
            print("Invalid route choice. Please try again.")
            continue

        # Calculate fare
        fare = calculate_fare(rate, distance)

        print("\n===== BOOKING DETAILS =====")
        print("Cab Type:", cab_type)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: Rs.", rate, "/km")
        print(f"Total Fare: Rs. {fare:.2f}")

        # Confirm booking before sharing OTP
        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirm = input("Enter your choice: ")

        if confirm == "2":
            print("Ride cancelled successfully. No OTP shared.")
            continue

        elif confirm == "1":
            otp = random.randint(1000, 9999)

            print("\nYour OTP is:", otp)
            print("Booking confirmed successfully!")
            print("Cancellation is not allowed after OTP sharing.")

        else:
            print("Invalid choice. Booking cancelled. No OTP shared.")

    elif choice == "2":
        print("Thank you for using Cab Booking Chatbot. Goodbye!")
        break

    else:
        print("Invalid menu choice. Please select 1 or 2.")
