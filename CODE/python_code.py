from flask import Flask
from flask import render_template
import RPi.GPIO as rpi
import time
import os
import asyncio
import subprocess

app= Flask(__name__)

led1,led2,led3= 3,5,7

rpi.setwarnings(False)
rpi.setmode(rpi.BOARD)
rpi.setup(led1, rpi.OUT)
rpi.setup(led2, rpi.OUT)
rpi.setup(led3, rpi.OUT)
rpi.output(led1, 0)
rpi.output(led2, 0)
rpi.output(led3, 0)
looping = True
print("Done")

#loop = asyncio.new_event_loop()
#asyncio.set_event_loop(loop)

async def loopy():
    while looping:
        rpi.output(led1,0)
        rpi.output(led2,0)
        rpi.output(led3,1)
        time.sleep(1)
        rpi.output(led3,0)
        rpi.output(led1,1)
        time.sleep(1)
        rpi.output(led1,0)
        rpi.output(led2,1)
        time.sleep(1)




@app.route('/')
def index():
    os.system("pkill -f Stoplight.py")
    return render_template('webpage.html')

@app.route('/A')
def led1on():
    os.system("pkill -f Stoplight.py")
    looping = False
    rpi.output(led3,0)
    rpi.output(led2,0)
    rpi.output(led1,1)
    return render_template('webpage.html')

@app.route('/B')
def led2on():
    os.system("pkill -f Stoplight.py")
    looping = False
    rpi.output(led1,0)
    rpi.output(led3,0)
    rpi.output(led2,1)
    return render_template('webpage.html')

@app.route('/E')
def led2off():
    looping = True
    subprocess.Popen(["/home/briguy97/Desktop/CODE/stop.sh"])
    #asyncio.run(loopy())
    #asyncio.ensure_future(loopy())
    #loop.run_forever()
    return render_template('webpage.html')

@app.route('/C')
def led3on():
    os.system("pkill -f Stoplight.py")
    looping = False
    rpi.output(led1,0)
    rpi.output(led2,0)
    rpi.output(led3,1)
    return render_template('webpage.html')

@app.route('/D')
def led3off():
    os.system("pkill -f Stoplight.py")
    #looping = False
    #loop.stop()
    rpi.output(led1,0)
    rpi.output(led2,0)
    rpi.output(led3,0)
    return render_template('webpage.html')

if __name__=="__main__":
    print("Start")
    
    app.run(debug=True, host='192.168.33.162')
