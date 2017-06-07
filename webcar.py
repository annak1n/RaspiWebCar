from flask import Flask, render_template, request
from flask import jsonify
import time
import RPi.GPIO as GPIO

IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15
IN12_PWM = 16
IN34_PWM = 22

SEC_NUM = 2
PWM_FREQ = 1000
PWM_DUTY = 40

CAR_TIME_OUT = 0.05

def init_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    GPIO.setup(IN12_PWM, GPIO.OUT)
    GPIO.setup(IN34_PWM, GPIO.OUT)

def stop():
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)

def fwd(sleep_time):
    print "---- go foward ----"
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    time.sleep(sleep_time)
    stop()

def back(sleep_time):
    print "---- go back ----"
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
    time.sleep(sleep_time)
    stop()

def left(sleep_time):
    print "---- turn left ----"
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    time.sleep(sleep_time)
    stop()

def right(sleep_time):
    print "---- turn right ----"
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)
    time.sleep(sleep_time)
    stop()

def pivot_left(sleep_time):
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)
    time.sleep(sleep_time)
    stop()

def pivot_right(sleep_time):
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
    time.sleep(sleep_time)
    stop()

def p_left(sleep_time):
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    time.sleep(sleep_time)
    stop()

def p_right(sleep_time):
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
    time.sleep(sleep_time)
    stop()

app = Flask(__name__)

app.config['SECRET_KEY'] = "dfdfdffdad"

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/touchcontrol', methods=['GET', 'POST'])
def mydict():
    touch_direction = request.form.get("touch", "null")
    print(touch_direction)
    
    if touch_direction == "panup":
        print("...forward...")
        fwd(CAR_TIME_OUT)
    elif touch_direction == "pandown":
        print("...backward...")
        back(CAR_TIME_OUT)
    elif touch_direction == "panleft":
        print("...turnleft...")
        left(CAR_TIME_OUT)
    elif touch_direction == "panright":
        print("...turnright...")
        right(CAR_TIME_OUT)
    elif touch_direction == "tap":
        print("...pause...")
        stop()
    elif touch_direction == "press":
        print("...pause...")
        stop()
    else:
        print("ERROR")
        stop()
        
    d = {'touchDirection': touch_direction}
    return jsonify(d)

if __name__ == '__main__':

    init_gpio()
    p12 = GPIO.PWM(IN12_PWM, PWM_FREQ)
    p12.start(PWM_DUTY)
    p34 = GPIO.PWM(IN34_PWM, PWM_FREQ)
    p34.start(PWM_DUTY)
    stop()
    
    app.run(host='192.168.31.202', port=3000)
