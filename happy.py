import scipy.io.wavfile as wavfile
import numpy as np
import pylab as pl
import time
import os
import sys
import subprocess
from scipy import mean
from random import randint


FILE = "karaoke.wav"
rate, data = wavfile.read(FILE)
t_total = len(data[:, 0]) / rate
display_rate = 1500
sample_size = 120
max_display = 90
data_length = len(data)
_min = min([abs(x) for x in data[:, 0]])
_max = max([abs(x) for x in data[:, 0]])


correction = 0.645


cols=15
display_char = "8"
cake_size = 50


flame_flutter_rate = 50
FLAMES = [" . ", ".  ", "  ."]
current_flame = ""




os.system("start "+FILE)
time.sleep(0.86)

for _f in range(int(data_length / display_rate)):


    if _f % flame_flutter_rate == 0:
        current_flame = (" " * int((cols / 2 - cake_size / 2))) + ((" " + FLAMES[randint(0, 2)] + " ") * int((cake_size / 5)))
    print
    current_flame


    print(" " * int((cols / 2 - cake_size / 2)) + ("  |  " * int((cake_size / 5))))

    print(" " * int((cols / 2 - cake_size / 2)) + ("-" * cake_size))

    bucket = []
    mug = []

    for value in data[:, 0][_f * display_rate + 1:(_f + 1) * display_rate]:
        mug.append(abs(value))
        if len(mug) == sample_size:
            bucket.append(mean(mug))
            mug = []
    bucket = [(float)((x - _min) * max_display) / (_max - _min) for x in bucket]


    for value in bucket:
        print((" " * int((cols / 2 - cake_size / 2))) + "| " + ("8" * int((value % (cake_size - 2)))) + (" " * int((cake_size - value - 2))) + "|")


    print((" " * int((cols / 2 - cake_size / 2))) + ("-" * cake_size))


    print("Happy Birthday, Qsho!")


    time.sleep(((float)(display_rate * t_total) / data_length) * correction)

    
    if _f != data_length / display_rate - 1:
        os.system("cls")

raw_input()
