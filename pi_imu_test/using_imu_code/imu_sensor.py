import os
import sys
import time
import smbus
import threading # to support async requests

from imusensor.MPU9250 import MPU9250

address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()

# store in a global var
sensor_data = {
    "yaw": 0, "pitch": 0, "roll": 0,
    "accel_x": 0, "accel_y": 0, "accel_z": 0,
    "gyro_x": 0, "gyro_y": 0, "gyro_z": 0,
    "mag_x": 0, "mag_y": 0, "mag_z": 0
}

def read_imu():
    while True:
        imu.readSensor()
        imu.computeOrientation()

        print(
            "Accel x: {0} ; Accel y : {1} ; Accel z : {2}".format(
                imu.AccelVals[0], imu.AccelVals[1], imu.AccelVals[2]
            )
        )
        print(
            "Gyro x: {0} ; Gyro y : {1} ; Gyro z : {2}".format(
                imu.GyroVals[0], imu.GyroVals[1], imu.GyroVals[2]
            )
        )
        print(
            "Mag x: {0} ; Mag y : {1} ; Mag z : {2}".format(
                imu.MagVals[0], imu.MagVals[1], imu.MagVals[2]
            )
        )
        print("roll: {0} ; pitch : {1} ; yaw : {2}".format(imu.roll, imu.pitch, imu.yaw))

        # update to global var
        sensor_data = {
                "yaw": imu.yaw,
                "pitch": imu.pitch,
                "roll": imu.roll,
                "accel_x": imu.AccelVals[0],
                "accel_y": imu.AccelVals[1],
                "accel_z": imu.AccelVals[2],
                "gyro_x": imu.GyroVals[0],
                "gyro_y": imu.GyroVals[1],
                "gyro_z": imu.GyroVals[2],
                "mag_x": imu.MagVals[0],
                "mag_y": imu.MagVals[1],
                "mag_z": imu.MagVals[2]
        }
        time.sleep(0.1)

imu_thread = threading.Thread(target=read_imu, daemon=True)
imu_thread.start()

def get_sensor_data():
    return sensor_data
