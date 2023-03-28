import qrcode
from PIL import Image

basewidth = 75
image = ""
data = ""

def doQR():
    logo = Image.open(image)
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    qr_big = qrcode.QRCode(error_correction=qrcode.ERROR_CORRECT_H, box_size=10, border=4)
    qr_big.add_data(data)
    qr_big.make(fit=True)
    img_qr_big = qr_big.make_image(fill_color="black", back_color="white").convert("RGB")
    pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)
    img_qr_big.paste(logo, pos)
    img_qr_big.save("qrcode.png")