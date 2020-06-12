import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import keyboard
import time

fs = 44100
seconds = 100 # maximum seconds of recording
print('commencing recording...')
start = time.time()
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels = 2)

keyboard.read_key()
sd.stop()
end = time.time()

print('completed')
elapsed = int(end - start)
myrecording = myrecording[:elapsed*fs]
write('output.wav', fs, myrecording)