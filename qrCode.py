import qrcode
# Data to encode
getDoc ='https://docs.google.com/spreadsheets/d/1qVrTHswHJr_oQnkPyuLD51PIp41NngZ5/edit?usp=sharing&ouid=102714207100519339481&rtpof=true&sd=true'

# Create QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)
# Add data to the QR code
qr.add_data(getDoc)
qr.make(fit=True)
# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")
# Save the image
img.save("qrcode_example.png")
