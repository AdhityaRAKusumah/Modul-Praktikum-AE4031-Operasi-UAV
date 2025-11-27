# Step 1: Import libraries
import cv2, time, traceback, ReadTelloStream
from djitellopy import Tello

# Step 2: Start
try:
    drone = Tello()
    drone.connect()
    print('Tello connected!')

    drone.streamon()
    time.sleep(10)

    # img = ReadTelloStream.ReadCamera(drone)
    drone.takeoff()
    time.sleep(2)

    img = ReadTelloStream.ReadCamera(drone)
    drone.move_forward(20)
    time.sleep(5)

    # drone.move_back(20)
    # time.sleep(5)

    img = ReadTelloStream.ReadCamera(drone)
    time.sleep(2)

    ReadTelloStream.SaveImage(img)

    # drone.move_right(20)
    # time.sleep(5)

    # drone.move_left(20)
    # time.sleep(5)

    # drone.move_up(20)
    # time.sleep(5)

    drone.move_down(20)
    time.sleep(5)

    drone.land()
    time.sleep(2)

    drone.streamoff()
except:
    try:
        drone.land()
    except:
        drone.emergency()
        
    print('An error occurred!')
    print('\n' + traceback.format_exc())

drone.end()