import pyqrcode
import png
from pyqrcode import QRCode
s=input("Enter your URL: ")
myqr=input("Enter your file name (without extension): ")
url=pyqrcode.create(s)
url.png(f"{myqr}.png", scale=8)