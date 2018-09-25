import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  

GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(25, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)           # set GPIO24 as an output 
GPIO.output(27, 1)
GPIO.output(25, 1)
from flask import Flask
from flask import render_template
from flask import request
import netifaces as nif

app = Flask(__name__)

ips = dict()

ips['Leandro'] = list()
ips['Leandro'].append('192.168.0.245')
ips['Leandro'].append('192.168.0.152')

ips['Eliete'] = list()
ips['Eliete'].append('192.168.0.221')





@app.route('/portaosocial/<nome>')
def portaosocial(nome):

    try:
        if str(request.remote_addr) in ips[nome]:
            GPIO.output(25, 0)
            sleep(3)
            GPIO.output(25, 1)
            return "portao"
    except:
        return "Acesso Negado!"

    

@app.route('/portaogaragem/<nome>')
def portaogaragem(nome):

    try:

        
        if str(request.remote_addr) in ips[nome]:
            GPIO.output(27, 0)
            sleep(1)
            GPIO.output(27, 1)
        return "garagem"
    except:
        return "Acesso Negado!"

    



@app.route("/")
def hello():


    return render_template('index.html')
 

   
    



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True, port=int('80'))

