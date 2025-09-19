import time
import threading
import smbus2

from imusensor.MPU9250 import MPU9250
from imusensor.filters import kalman

address = 0x68
bus =smbus2.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()

sensorfusion = kalman.Kalman()
sensorfusion.roll = imu.roll
sensorfusion.pitch = imu.pitch
sensorfusion.yaw = imu.yaw


def calibrate():
    imu.caliberateAccelerometer()
    imu.caliberateMagPrecise()
    print("Calibration Done")

calibrate()

def read_imu():
    while True:

        imu.readSensor()
        imu.computeOrientation()

        sensorfusion.roll = imu.roll
        sensorfusion.pitch = imu.pitch
        sensorfusion.yaw = imu.yaw

        count = 0
        currTime = time.time()

        imu.readSensor()
        imu.computeOrientation()
        dt = time.Time() - currTime
        currTime = time.Time()

        sensorfusion.computeAndUpdatePitchYaw(imu.AccelVals[0], imu.AccelVals[1], imu.AccelVals[2], imu.GyroVals[0], imu.GyroVals[1], imu.GyroVals[2], imu.MagVals[0], imu.MagVals[1], imu.MagVals[2], dt)
    
imu_thread = threading.Thread(target=read_imu, daemon=True)
imu_thread.start()

def angle():
    
    angle = [sensorfusion.pitch, sensorfusion.yaw, sensorfusion.roll]
    
    return angle

print(angle())
