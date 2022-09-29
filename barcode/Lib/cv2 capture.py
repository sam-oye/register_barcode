from record import * 
import cv2




webcam=cv2.VideoCapture(0)

attend=[]
n=0

while True:
    ret, frame = webcam.read()

    if ret==True:
        cv2.imshow("Koolac",frame)
        cv2.imwrite("frame.png", frame)
        d=cv2.QRCodeDetector()
        text, _, _ = d.detectAndDecode(cv2.imread('NCAIR.png'))
        if text:
            if text not in attend:
                print("Decoded Text is", text)
                Attend(text)
                attend.append(text)
        key=cv2.waitKey(1)
        if key == ord("q"):
            break
    n+=1


webcam.release()
cv2.destroyAllWindows()
