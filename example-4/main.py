#!/usr/bin/env python

from qrcode import QRCode, constants
from qrcode.image.styledpil import StyledPilImage

qr = QRCode(version=5, error_correction=constants.ERROR_CORRECT_H)
qr.add_data("example-4")

img = qr.make_image(image_factory=StyledPilImage, embeded_image_path="smile.png")
img.save("qr.png")

exit(0)
