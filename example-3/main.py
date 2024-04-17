#!/usr/bin/env python

from qrcode import QRCode

qr = QRCode(version=10)
qr.add_data("example-3")
qr.make(fit=True)

img = qr.make_image(back_color=(187, 162, 222))
img.save("qr.png")

exit(0)
