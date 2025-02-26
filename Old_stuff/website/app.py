from flask import Flask, render_template, flash, render_template, redirect, request, session, send_file
import os

app = Flask(__name__)

# Constants
constAspects = ['Angle Orientation', 'Tourniquet time', 'Flashback']
aspects={
    'Angle Orientation': {
        'measurement' : None,
        'result' : None
    },
    'Tourniquet Time': {
        'measurement' : None,
        'result': None
    },
    'Flashback': {
        'measurement' : None,
        'result': None
    }
}

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('interface.html')




@app.route('/prepPhase', methods=["GET", "POST"])
def prepChecklist():
    if request.method == "GET":
        return render_template('prepPhase.html')


@app.route('/results', methods=["GET"])
def feedback():

    
    return render_template('results.html', aspects=aspects)

@app.route('/image')
def image():
    return send_file('output.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

