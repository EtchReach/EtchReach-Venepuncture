import numpy as  np
import cv2
from PIL import Image

#turn on camera
prev_bbox2 = None
flashback = 0
cap = cv2.VideoCapture(0)

while True:
    #DETECTING FLASHBACK

    #capture frame and convert into hsv
    ret, frame = cap.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #lower and upper hsv limit for RED
    lowerLimit = np.array([161,155,84])
    upperLimit = np.array([179,255,255])
    
    #setting up mask and bounding box for RED objects
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
        flashback = 1
    else:
        flashback = 0


    #TRACKING SYRINGE MOVEMENT
    #lower and upper hsv limit for GREEN
    lowerLimit2 = np.array([36,74,84])
    upperLimit2 = np.array([76,255,255])

    #setting up mask and bounding box for GREEN objects
    mask2 = cv2.inRange(hsvImage, lowerLimit2, upperLimit2)
    mask2_ = Image.fromarray(mask2)
    bbox2 = mask2_.getbbox()

    if bbox2 is not None:
        x1, y1, x2, y2 = bbox2
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

        #Checks if green object is moving
        if prev_bbox2 is not None:
            displacement = abs(x1 - prev_bbox2[0]) + abs(y2 - prev_bbox2[1])
            #Checks if green object is moving while red object is detected
            if displacement > 150 and flashback == 0:
                print("Moving")
            elif displacement > 150 and flashback == 1:
                print("!!!!!")
            else:
                print("Stopped")
    
        prev_bbox2 = (x1, y1)
        
        # Update the previous bounding box
        prev_bbox2 = bbox2    

    cv2.imshow("mask2", mask2)
    cv2.imshow("mask", mask)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()