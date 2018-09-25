import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  

GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(27, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)           # set GPIO24 as an output 
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/portaosocial')
def portaosocial():
    GPIO.output(27, 0)
    return "Liga"

@app.route('/portaogaragem')
def portaogaragem():
    GPIO.output(27, 0)
    sleep(1)
    GPIO.output(27, 1)

    return "Desliga"



@app.route("/")
def hello():  
   
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
