#!/usr/bin/env python

import qrcode

img = qrcode.make("Пример простого QR-кода")
img.save("qr.png")

exit(0)
