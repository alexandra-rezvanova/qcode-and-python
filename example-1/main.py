#!/usr/bin/env python

import qrcode

img = qrcode.make("example-1")
img.save("qr.png")

exit(0)
