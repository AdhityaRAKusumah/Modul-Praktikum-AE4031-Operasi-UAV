# Step 1: Import libraries
import time, traceback
from djitellopy import Tello

def FlightControl(command):
    # Translates flight plan as drone commands
    movement, value = command.split()[0], command.split()[1]

    if movement.lower() == 'forward':
        drone.move_forward(value)
    elif movement.lower() == 'back':
        drone.move_back(value)
    elif movement.lower() == 'right':
        drone.move_right(value)
    elif movement.lower() == 'left':
        drone.move_left(value)
    elif movement.lower() == 'ccw':
        drone.rotate_counter_clockwise(value)
    elif movement.lower() == 'cw':
        drone.rotate_clockwise(value)
    elif movement.lower() == 'up':
        drone.move_up(value)
    elif movement.lower() == 'down':
        drone.move_down(value)

# Step 2: Define flight plan
FlightPlan = ['forward 20',
              'cw 90',
              'up 20',
              'left 20']

# Step 3: Start
try:
    drone = Tello()
    drone.connect()
    print('Tello connected!')

    drone.streamon()
    time.sleep(10)

    drone.takeoff()
    time.sleep(2)

    for cmd in FlightPlan:
        FlightControl(cmd)
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
