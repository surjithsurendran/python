import qrcode
qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5

    )

data="Hello I'm Surjith"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",black_color="white")
img.save("2.png")
