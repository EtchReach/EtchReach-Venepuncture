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
    # Obtain values from Pi-IMU (pi_imu_test)
    # Convert values to quaternion using old code
    # Convert quaternion to readable values

    # Obtain yaw pitch roll 
    yaw, pitch, roll = 0, 0, 0
    return yaw, pitch, roll


def image_server():
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(0)

    # Accept a single connection and make a file-like object out of it
    connection = server_socket.accept()[0].makefile('rb')
    try:
        while True:
            # Read the length of the image as a 32-bit unsigned int. If the
            # length is zero, quit the loop
            image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
            if not image_len:
                break
            # Construct a stream to hold the image data and read the image
            # data from the connection
            image_stream = io.BytesIO()
            image_stream.write(connection.read(image_len))
            # Rewind the stream, open it as an image with PIL and do some
            # processing on it
            image_stream.seek(0)
            image = Image.open(image_stream)
            print('Image is %dx%d' % image.size)
            image.verify()
            print('Image is verified')
    finally:
        connection.close()
        server_socket.close()


