import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(18, GPIO.OUT)           # set GPIO24 as an output 
GPIO.setup(23, GPIO.OUT)
from flask import Flask
app = Flask(__name__)

@app.route('/pcliga')
def ligapc():
    GPIO.output(23, 0)
    return "Liga"

@app.route('/pcdesliga')
def desligapc():
    GPIO.output(23, 1)
    return "Desliga"

@app.route('/liga')
def liga():
    GPIO.output(18, 1)
    return "Liga"

@app.route('/desliga')
def desliga():
    GPIO.output(18, 0)
    return "Desliga"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
