import qrcode

# URL to encode
url = "https://rmit.au1.qualtrics.com/jfe/form/SV_9zev4vUiPlvK1MO"

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("rmit_qualtrics_qr.png")
