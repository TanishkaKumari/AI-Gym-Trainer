import cv2
import mediapipe as mp
import time
import math

from numpy import angle

class poseDetection():
    def __init__(self, mode= False, upBody =False, smooth = True, detectionCon = 0.5, trackingCon = 0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackingCon)

    def findPose(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
            
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw = True):
        self.lmlist = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                #print(lm, id)
                cx, cy = int(lm.x*w), int(lm.y*h)
                self.lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx,cy), 5, (255,0,25), cv2.FILLED)
        return self.lmlist

    def findAngle(self, img, p1, p2, p3, draw = True):

        #get the landmarks
        x1,y1 = self.lmlist[p1][1:]
        x2,y2 = self.lmlist[p2][1:]
        x3,y3 = self.lmlist[p3][1:]

        #Calculate the angles
        angle = math.degrees(math.atan2(y3-y2, x3-x2)-math.atan2(y1-y2, x1-x2))

        if angle < 0:
            angle += 360

        #Draw
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255,255,255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255,255,255), 3)
            cv2.circle(img, (x1,y1), 10, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x1,y1), 15, (0,0,255), 2)
            cv2.circle(img, (x2,y2), 10, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x2,y2), 15, (0,0,255), 2)
            cv2.circle(img, (x3,y3), 10, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x3,y3), 15, (0,0,255), 2)
            cv2.putText(img, str(int(angle)), (x2-50,y2+50), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)

            return angle
            
        

def main():
    cap = cv2.VideoCapture('pedestrian_video.mp4')
    ptime = 0
    detector = poseDetection()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmlist = detector.findPosition(img, draw = False)
        if len(lmlist) !=0:  
            print(lmlist[14])
        cv2.circle(img, (lmlist[14][1], lmlist[14][2]), 15, (0,0,255), cv2.FILLED)

        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_COMPLEX, 3, (255,0,0), 3)
        
        cv2.imshow('Image', img)
        key = cv2.waitKey(1)
        if key == 113 or key == 81:
            break


if __name__ == '__main__':
    main()