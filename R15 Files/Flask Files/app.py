from flask import Flask, jsonify, request, render_template, Response
from flask_cors import CORS

import camerarun
import imuCode

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return

@app.route("/imu")
def imu():
    angle = imuCode.angle()
    return jsonify({"pitch": angle[0], "yaw": angle[1], "roll": angle[2]})

@app.route("/camera")
def camera():
    return Response(camerarun.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)

