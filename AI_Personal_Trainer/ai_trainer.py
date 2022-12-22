import cv2
from cv2 import waitKey
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)
detector = pm.poseDetection()
count = 0
dir = 0
pTime = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1200, 720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) !=0:
        #right arm
        angle = detector.findAngle(img, 12,14,16)
        #left arm
        detector.findAngle(img, 11,13,15)
        #left leg
        detector.findAngle(img, 23,25,27)
        #right leg
        detector.findAngle(img, 24,26,28)

        per = np.interp(angle, (210,310), (0,100))
        bar = np.interp(angle, (220,310), (650, 100))
        # print(per)

        #check for the dumbell curl
        color = (255,0,255)
        if per == 100:
            if dir == 0:
                color = (0,255,0)
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                color = (0,255,0)
                count += 0.5
                dir = 0

        #bar
        cv2.rectangle(img, (1100, 100), (1175,650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175,650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)


        cv2.rectangle(img, (0, 450), (250,720), (0,255,0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (35, 670), cv2.FONT_HERSHEY_PLAIN, 10, (255,0,0), 20)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0), 5)


    cv2.imshow("image", img)
    key = cv2.waitKey(1)
    if key == 113 or key == 81:
        break