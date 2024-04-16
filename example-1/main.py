#!/usr/bin/env python

import qrcode

img = qrcode.make("Пример простого QR-кода")
img.save("example-1.png")

exit(0)
