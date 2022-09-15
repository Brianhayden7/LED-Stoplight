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

while True:
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
