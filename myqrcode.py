# This is a python script to create a QR code 
import qrcode
from PIL import Image

data = "https://erp.isbatuniversity.ac.ug/frmStudentLogin.aspx"

qr = qrcode.QRCode(version=2, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
Image = qr.make_image(fill="black", back_color="white")

Image.save("Isbat.png")
Image.show()


# You must make sure you have the qrcode and pillow libraries installed in your python environment.

# And this is how to have it installed
# pip install qrcode[pil]