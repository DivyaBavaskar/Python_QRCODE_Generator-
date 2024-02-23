import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size= 10,
    border = 5
)

# data = "https://wondrous-queijadas-5b0bda.netlify.app "
data = "https://www.youtube.com/"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img.save("test.png")