
import cv2

d=cv2.QRCodeDetector()
text, _, _ = d.detectAndDecode(cv2.imread('NCAIR.png'))
if text:
    print("yes")
print("Decoded Text is", text)


attendace ={
    "name":"988899",
    "time":"8-12",
    "monday":"",
    "tuesday":"",
    "wednesday":""    
    
    }
