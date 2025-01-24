# pip install prcode
# pip install "qrcode[pil]"
# This app generates qr code for your link!

import qrcode

qr_data = "www.google.com"
qr_img = qrcode.make(qr_data)

save_path = '4. QR code generator\\' + qr_data + '.png'
qr_img.save(save_path)