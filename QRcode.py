import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "red", back_color = "black")
    filename = input("Please enter a name for the file: ")
    img.save(filename)
    print("SUCCESS")
    
url = input("Please enter URL: ")
generate_qrcode(url)
