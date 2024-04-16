#!/usr/bin/env python

from qrcode import QRCode

qr = QRCode(version=5)
qr.add_data("example-2")
qr.make(fit=True)

img = qr.make_image()
img.save("qr.png")

exit(0)
