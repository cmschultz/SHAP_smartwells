import time
from tellopy import Tello

def main():
    drone = Tello()

    try:
        drone.connect()
        drone.wait_for_connection(10.0)

        drone.takeoff()

        time.sleep(5)  

        drone.land()
    except Exception as e:
        print(e)
    finally:
        drone.quit()

if __name__ == '__main__':
    main()

