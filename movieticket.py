import json
import ticket_price as tp
from movielist import load_movies, display_movies
from emailsending import send_email

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

def add_booking(name, age, seats, movie, totalprice):
    bookings = load_bookings()
    new_booking = {
        "name": name,
        "age": age,
        "seats": seats,
        "movie": movie,
        "totalprice": totalprice
    }
    bookings.append(new_booking)
    save_bookings(bookings)
    print("Booking saved successfully!")
    
    sender_email = input("Enter sender email: ").strip()
    receiver_email = input("Enter receiver email: ").strip()
    
    # Ensure no email details are empty
    if not sender_email or not receiver_email:
        print("Email addresses cannot be empty. Booking completed without sending email.")
        return
    
    # Constructing the subject and message
    subject = f"Booking Confirmation for {movie}"
    # message = (
    #     f"Hello {name},\n\n"
    #     f"Thank you for booking the movie {movie}.\n"
    #     f"Details:\n"
    #     f"Name: {name}\n"
    #     f"Age: {age}\n"
    #     f"Movie: {movie}\n"
    #     f"Seats: {', '.join(seats)}\n"
    #     f"Total Price: {totalprice}\n\n"
    #     f"Enjoy the show!\n"
    # )
    message = f"Hello {name},\n\n Thank you for booking the movie {movie}.\n Details:\n Name: {name}\n Age: {age}\n Movie: {movie}\n Seats: {', '.join(seats)}\n Total Price: {totalprice}\n\n Enjoy the show!\n"
    
    # Debugging the message
    print("Constructed Email Message:\n", message)
    
    # Attempt to send email
    try:
        sender_password = "auwu yimi srwa xxtj"
  # Consider fetching securely
        print("Sending email...")
        send_email(sender_email, sender_password, receiver_email, subject, message)
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", str(e))


# Function to book tickets
def book_ticket(seats, row, start_col, end_col):
    
    movies=load_movies()
    if not movies:
        print("No movies available.")
        return
    display_movies(movies)
    movie_choice=int(input("Enter the movie number: "))
    if movie_choice < 0 or movie_choice > len(movies):
        print("Invalid movie selection. Please try again.")
        return
    selected_movies=movies[movie_choice-1]
    print(f"Selected movie: {selected_movies['title']}")
    print("Available seats:")
    for i,timing in enumerate(selected_movies['show_timings'],1):
        print(f"{i}. {timing}")
    timing_choice=int(input("Enter the timing number: "))
    if timing_choice < 0 or timing_choice > len(selected_movies['show_timings']):
        print("Invalid timing selection. Please try again.")
        return
    selected_timing=selected_movies['show_timings'][timing_choice-1]
    print(f"Selected timing: {selected_timing}")



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
        
    num_tickets=end_col-start_col+1
    totalprice=tp.ticket_price(num_tickets)
    # print(f"Total Price: {totalprice}")
    confirm=input("Do you want to proceed with the booking? (yes/no): ")
    if confirm !='yes':
        print("Booking cancelled.")
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
    add_booking(name, age, booked_seats, movie,totalprice)

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
        print(f"  Total Price: {booking.get('totalprice', 'N/A')}")

# Load the current seating arrangement
seats = load_seats()

# Display current seating arrangement
print_seats(seats)

# Menu for interaction
while True:
    print("\nOptions:")
    print("1. Book tickets")
    print("2. View bookings")
    print("3. Display movies")
    print("4. Load Seats")
    print("5. Eixt")
    # print("5. Testing email")
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
        movies=load_movies()
        display_movies(movies)
    elif choice == '4':
        print_seats(load_seats())
    elif choice == '5':
        exit()
        break
    else:
        print("Invalid choice. Please try again.")


