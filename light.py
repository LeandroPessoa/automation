import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  

GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(27, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)           # set GPIO24 as an output 
GPIO.output(27, 1)
from flask import Flask
from flask import render_template
from flask import request
import netifaces as nif

app = Flask(__name__)


def mac_for_ip(ip):
    'Returns a list of MACs for interfaces that have given IP, returns None if not found'
    for i in nif.interfaces():
        addrs = nif.ifaddresses(i)
        try:
            if_mac = addrs[nif.AF_LINK][0]['addr']
            if_ip = addrs[nif.AF_INET][0]['addr']
        except IndexError: #ignore ifaces that dont have MAC or IP
            if_mac = if_ip = None
        if if_ip == ip:
            return if_mac
    return None


@app.route('/portaosocial')
def portaosocial():
    GPIO.output(21, 0)
    sleep(3)
    GPIO.output(21, 1)
    return "portao"

@app.route('/portaogaragem')
def portaogaragem():
    #GPIO.output(27, 0)
    print(mac_for_ip(request.remote_addr))

    sleep(1)
    #GPIO.output(27, 1)

    return "garagem"



@app.route("/")
def hello():  
   
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)

