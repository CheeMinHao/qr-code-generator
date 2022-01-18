import qrcode
import datetime
# Link for website
input_data = "https://forms.gle/Dyh7QnRovZ1297ZT9"
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')

img.save("qrcodes\{time}.png".format(time=datetime.date.today()))  