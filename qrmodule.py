import qrcode
import os

def qrsending(name, age, seats, movie, totalprice):
    output_dir = 'K:/vscode/Newones/QRS'

    # Ensure the directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Generate and save the QR code
    qr_data = f"Name: {name}\nAge: {age}\nSeats: {', '.join(seats)}\nMovie: {movie}\nTotal Price: {totalprice}"
    img = qrcode.make(qr_data)
    qr_path = os.path.join(output_dir, 'booking_qr.png')
    img.save(qr_path)

    print("QR Code saved successfully at:", qr_path)
    return qr_path  # Return the file path of the QR code
