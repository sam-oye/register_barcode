
import cv2

d=cv2.QRCodeDetector()
text, _, _ = d.detectAndDecode(cv2.imread('frame.jpg'))
if text:
    print("yes")
print("Decoded Text is", text)
