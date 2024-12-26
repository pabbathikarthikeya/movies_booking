import json

# File to store the seating arrangement and bookings
SEATING_FILE = "seats.json"
BOOKINGS_FILE = "bookings.json"

# Function to initialize or load seats
def load_seats():
    try:
        with open(SEATING_FILE, 'r') as file:
            seats = json.load(file)
        print("Seating arrangement loaded.")
    except FileNotFoundError:
        seats = [['💺' for _ in range(10)] for _ in range(10)]
        print("New seating arrangement initialized.")
    return seats

# Function to save seats to a file
def save_seats(seats):
    with open(SEATING_FILE, 'w') as file:
        json.dump(seats, file)
    print("Seating arrangement saved.")

# Function to load bookings
def load_bookings():
    try:
        with open(BOOKINGS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

# Function to save bookings
def save_bookings(bookings):
    with open(BOOKINGS_FILE, 'w') as file:
        json.dump(bookings, file, indent=4)
    print("Bookings saved.")

# Function to add a new booking
def add_booking(name, age, seats, movie):
    bookings = load_bookings()
    new_booking = {
        "name": name,
        "age": age,
        "seats": seats,
        "movie": movie
    }
    bookings.append(new_booking)
    save_bookings(bookings)
    print("Booking saved successfully!")

# Function to book tickets
def book_ticket(seats, row, start_col, end_col):
    if row < 1 or row > 10 or start_col < 1 or end_col > 10:
        print("Invalid row or column selection. Please choose within the 10x10 range.")
        return
    if start_col > end_col:
        print("Invalid column range. Start column must be less than or equal to end column.")
        return

    # Adjust for 0-based indexing
    row_index = row - 1
    start_index = start_col - 1
    end_index = end_col - 1

    # Check if any seat in the range is already booked
    for col in range(start_index, end_index + 1):
        if seats[row_index][col] == '🟥':
            print(f"Seat {row}-{col + 1} is already booked. Cannot complete booking.")
            return

    # Book the seats
    for col in range(start_index, end_index + 1):
        seats[row_index][col] = '🟥'
    print(f"Seats {row}-{start_col} to {row}-{end_col} booked successfully.")

    # Collect customer details
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    movie = input("Enter the movie name: ")
    booked_seats = [f"{row}-{i+1}" for i in range(start_index, end_index + 1)]

    # Save the booking details
    add_booking(name, age, booked_seats, movie)

    # Save updated seating arrangement
    save_seats(seats)

# Function to print seats in a grid format
def print_seats(seats):
    print("\nSeating Arrangement:")
    # Print column numbers
    print("     " + "  ".join([f"{i+1:2}" for i in range(10)]))
    print("   " + "-" * 50)  # Separator
    for i, row in enumerate(seats):
        print(f"{i+1:2} | " + "  ".join(row))

# Function to display all bookings
def display_bookings():
    bookings = load_bookings()
    if not bookings:
        print("No bookings available.")
        return

    print("\nBooking Details:")
    for i, booking in enumerate(bookings, start=1):
        print(f"\nBooking {i}:")
        print(f"  Name: {booking['name']}")
        print(f"  Age: {booking['age']}")
        print(f"  Movie: {booking['movie']}")
        print(f"  Seats: {', '.join(booking['seats'])}")

# Load the current seating arrangement
seats = load_seats()

# Display current seating arrangement
print_seats(seats)

# Menu for interaction
while True:
    print("\nOptions:")
    print("1. Book tickets")
    print("2. View bookings")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        row = int(input("Enter row number: "))
        start_col = int(input("Enter start column number: "))
        end_col = int(input("Enter end column number: "))
        book_ticket(seats, row, start_col, end_col)
        print_seats(seats)
    elif choice == '2':
        display_bookings()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
