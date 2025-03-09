from flask import Flask, render_template, jsonify
import io
import socket
import struct
from PIL import Image
from pi_imu_test.using_imu_code.imu_sensor import get_sensor_data # import made possible using __init__.py to make it a package

app = Flask(__name__)

@app.route('/')
def index():

    angle = get_angle()
    return render_template('index.html')


'''API Endpoints'''
@app.route('/getangleandorientation')
def get_angle():
    # Obtain yaw pitch roll from Pi-IMU (pi_imu_test) (done)

    return jsonify(get_sensor_data())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)