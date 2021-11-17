from flask import Flask
from flask import render_template
import RPi.GPIO as rpi
import time

app=Flask(__name__)

switch1 = 4
switch2 = 27
switch3 = 22
switch4 = 23

rpi.setwarnings(False)
rpi.setmode(rpi.BCM)
rpi.setup(switch1, rpi.OUT)
rpi.setup(switch2, rpi.OUT)
rpi.setup(switch3, rpi.OUT)
rpi.setup(switch4, rpi.OUT)
rpi.output(switch1, 0)
rpi.output(switch2, 0)
rpi.output(switch3, 0)
rpi.output(switch4, 0)
print("Done")

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route('/A')
def switch1on():
    rpi.output(switch1, 1)
    return render_template('webpage.html')

@app.route('/A')
def switch1on():
    rpi.output(switch1, 1)
    return render_template('webpage.html')

@app.route('/a')
def switch1off():
    rpi.output(switch1, 0)
    return render_template('webpage.html')

@app.route('/B')
def switch2on():
    rpi.output(switch1, 1)
    return render_template('webpage.html')

@app.route('/b')
def switch2off():
    rpi.output(switch1, 0)
    return render_template('webpage.html')

@app.route('/C')
def switch3on():
    rpi.output(switch1, 1)
    return render_template('webpage.html')

@app.route('/c')
def switch3off():
    rpi.output(switch1, 0)
    return render_template('webpage.html')

@app.route('/D')
def switch4on():
    rpi.output(switch1, 1)
    return render_template('webpage.html')

@app.route('/d')
def switch4off():
    rpi.output(switch1, 0)
    return render_template('webpage.html')

if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='192.168.199.110')
