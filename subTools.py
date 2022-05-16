import cv2
from pyzbar import pyzbar

def recoq_qr(name):
    file = name
    img = cv2.imread(file)
    qrcodes = pyzbar.decode(img)
    return qrcodes[0][0].decode('utf-8')