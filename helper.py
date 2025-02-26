import time
import numpy as np
import serial

class QuaternionData:
    def __init__(self):
        self.qw = 0.0
        self.qx = 0.0
        self.qy = 0.0
        self.qz = 0.0

def read_quaternion_data(ser: serial.Serial):
    while True:
        data = ser.readline().decode().strip()
        
        # Check if data starts with "QW:" and has the correct format
        if data.startswith("QW:") and data.count("QW:") == 1:
            try:
                # Extract quaternion values
                parts = data.split("\t")
                qw = float(parts[0][4:])
                qx = float(parts[1][4:])
                qy = float(parts[2][4:])
                qz = float(parts[3][4:])
                
                quaternion = QuaternionData()
                quaternion.qw, quaternion.qx, quaternion.qy, quaternion.qz = qw, qx, qy, qz
                return quaternion
            except (ValueError, IndexError) as e:
                print(f"Error parsing data: {e}")
        
        else:
            print("Invalid data format, skipping: ", data)
            # Continue reading the next line
            continue

def parse_quaternion(quat: QuaternionData):

    quatParsed = (f"w{quat.qw}wa{quat.qx}ab{quat.qy}bc{quat.qz}c")
    print(quatParsed)
    return quatParsed


ser = serial.Serial("COM5", 9600, timeout=1) # or 115200
quaternion_data = read_quaternion_data(ser)
# line = parse_quaternion(quaternion_data)