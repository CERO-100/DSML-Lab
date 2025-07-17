import pyqrcode
import png
from pyqrcode import QRCode
s=input("Enter your url:")
myqr=input("Enter your file name")
url=pyqrcode.create(s)
url.svg(myqr+'.svg',scale=6)