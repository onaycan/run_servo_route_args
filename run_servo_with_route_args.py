import RPi.GPIO as GPIO
from flask import Response
from flask import Flask
from flask_cors import CORS
from flask import request
import time

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start(7.5)
time.sleep(1)


def SetAngle(angle):
    global p , servoPIN
    duty = angle / 18 + 2.5
    GPIO.output(servoPIN, True)
    p.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servoPIN, False)

@app.route("/")
def index():
    return "0"


@app.route("/servo_socket")
def servo_socket():
    global p
    angle = request.args.get('angle', default = 90, type = int)
    SetAngle(angle)
    #SetAngle(180)
    #SetAngle(90)
    #SetAngle(0)
    #SetAngle(90)
    return "angle is set to: " + str(angle)

if __name__ == '__main__':
	app.run(host="10.42.0.1", port="5000", ssl_context=('./certs/server.crt', './certs/server.key'), debug=True, use_reloader=False)

p.stop()
GPIO.cleanup()