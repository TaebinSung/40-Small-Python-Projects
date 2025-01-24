import os
import qrcode

file_path = "4. QR code generator\\qrCodeCollection.txt"
with open(file_path, 'rt', encoding='UTF8') as f :
    read_lines = f.readlines()

for line in read_lines:
    line = line.strip()
    qr_data = line
    qr_img = qrcode.make(qr_data)

    folder_path = "4. QR code generator\\QRcodeCollection\\"
    os.makedirs(folder_path, exist_ok=True)
    save_path = folder_path + qr_data + ".png"
    qr_img.save(save_path)