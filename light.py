import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  

GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  



GPIO.setup(22, GPIO.OUT)           #luz


#GPIO.output(17, 1)
GPIO.output(22, 1)




from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

ips = dict()

ips['Leandro'] = list()
ips['Leandro'].append('192.168.0.245')
ips['Leandro'].append('192.168.0.152')
ips['Leandro'].append('192.168.0.192')


ips['Eliete'] = list()
ips['Eliete'].append('192.168.0.221')

ips['Garagem'] = list()
ips['Garagem'].append('192.168.0.104')






@app.route('/portaosocial/<nome>')
def portaosocial(nome):

    try:
        if str(request.remote_addr) in ips[nome]:
            GPIO.setup(17, GPIO.OUT)
            GPIO.output(17, 0)
            sleep(1)
            GPIO.output(17, 1)
            return "portao"
    except:
        return "Acesso Negado!"

    

@app.route('/portaogaragem/<nome>')
def portaogaragem(nome):

    try:
                   #portao
        
        if str(request.remote_addr) in ips[nome]:
            GPIO.setup(27, GPIO.OUT)           #garagem
            GPIO.output(27, 1)
            sleep(1)
            GPIO.output(27, 0)
        return "garagem"
    except:
        return "Acesso Negado!"

@app.route('/ligaluz/<nome>')
def ligaluz(nome):

    try:

        
        if str(request.remote_addr) in ips[nome]:
            GPIO.output(22, 0)
            
        return "ligaluz"
    except:
        return "Acesso Negado!"

@app.route('/desligaluz/<nome>')
def desligaluz(nome):

    try:

        
        if str(request.remote_addr) in ips[nome]:
            GPIO.output(22, 1)
            
        return "desligaluz"
    except:
        return "Acesso Negado!"
    
    



@app.route("/")
def hello():


    return render_template('index.html')
 

   
    



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)

