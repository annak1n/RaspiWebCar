import time
import RPi.GPIO as GPIO

IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15
IN12_PWM = 18
IN34_PWM = 22

SEC_NUM = 2
PWM_FREQ = 1000
PWM_DUTY = 40

def init_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1,GPIO.OUT)
    GPIO.setup(IN2,GPIO.OUT)
    GPIO.setup(IN3,GPIO.OUT)
    GPIO.setup(IN4,GPIO.OUT)
    GPIO.setup(IN12_PWM,GPIO.OUT)
    GPIO.setup(IN34_PWM,GPIO.OUT)

def stop():
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)
    
def test():
    stop()
    fwd(2)
    stop()

def fwd(sleep_time):
    print "---- go foward ----"
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    time.sleep(sleep_time)

def main():

    init_gpio()
    
    p12 = GPIO.PWM(IN12_PWM, PWM_FREQ)
    p12.start(PWM_DUTY)
    p34 = GPIO.PWM(IN34_PWM, PWM_FREQ)
    p34.start(PWM_DUTY)
    
    test()
    
    GPIO.cleanup()

if __name__ == '__main__':
    main()