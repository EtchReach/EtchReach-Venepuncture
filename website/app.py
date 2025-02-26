from flask import Flask, render_template
import io
import socket
import struct
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():

    angle = get_angle()
    return render_template('index.html')


'''API Endpoints'''
@app.route('/getangleandorientation')
def get_angle():
    # Obtain yaw pitch roll from Pi-IMU (pi_imu_test) (done)

    # Obtain yaw pitch roll 
    yaw, pitch, roll = 0, 0, 0
    return yaw, pitch, roll


def image_server():



