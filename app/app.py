from flask import Flask, render_template, request
import serial

ser = serial.Serial('/dev/ttyUSB0')


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/processar", methods=['GET','POST'])
def processar():
    if request.method == 'POST':
        print(request.form['submit'])
        if request.form['submit'] == 'lights_on':
            ser.write('1')
            return render_template('index.html')
        elif request.form['submit'] == 'lights_off':
            ser.write('2')
            return render_template('index.html')
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug = True)
