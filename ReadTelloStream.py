"""
A module to read Tello drone camera stream

AUTHOR(S)
    Kusumah, Adhitya R.A. (AK)

USAGE
    ReadCamera(Drone)
        Drone   - Tello drone object

        Returns numpy image data
    
    ShowFeed(frame)
        frame   - Numpy image data to be displayed

    SaveImage(frame)
        frame - Numpy image data to save

COPYRIGHT
    Flight Control System Rapid Prototyping Workshop (FCS RAPTOR)
    Faculty of Mechanical and Aerospace Engineering
    Institut Teknologi Bandung, 2025

MODULE HISTORY(S)
    20/04/2025  - Created and debugged, AK
    24/11/2025  - Added function to save captured image, AK
    07/12/2025  - Minor improvements, AK

"""

import cv2
from djitellopy import Tello

def ReadCamera(tello):
    # Capture drone feed
    frame = tello.get_frame_read().frame
    frame = cv2.resize(frame, (720, 480))

    # Convert to RGB Image
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    return frame

def ShowFeed(frame):
    cv2.imshow('Feed', frame)

def SaveImage(frame):
    cv2.imwrite(f'Captured.jpg', frame)

if __name__=='__main__':
    tello = Tello()
    tello.connect()
    print('tello connected!')

    tello.streamon()
    while True:
        frame = ReadCamera(tello)
        print(f'Drone Battery: {tello.get_battery()}%')

        lower_red = (0, 0, 100)
        upper_red = (80, 80, 255)
        mask = cv2.inRange(frame, lower_red, upper_red)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, "Red Object", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        ShowFeed(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    tello.streamoff()
    tello.end()
