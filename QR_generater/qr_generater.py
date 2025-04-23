import qrcode
import qrcode.constants

# data = "https://example.com"

data = '''
    name: gautam,
    coll: reck,
    no: 12345678
'''

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color = "black", back_color="white")


image.save("my_qr_code3.png")
print("QR cide generated and saved as 'my_qr_code.png'")