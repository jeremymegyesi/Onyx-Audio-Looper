import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import time


class AudioBroker:
    def __init__(self):
        print("loading main...")
        self._fs = 44100
        self._seconds = 400  # maximum seconds of recording
        self._audio = []
        self._start = 0
        self._end = 0

    def start_recording(self):
        print('commencing recording...')
        self._start = time.time()
        self._audio = sd.rec(int(self._seconds * self._fs), samplerate=self._fs, channels=2)

    def end_recording(self):
        sd.stop()
        self._end = time.time()
        print('completed')
        elapsed = self._end - self._start
        print(elapsed)
        self._audio = self._audio[:int(elapsed * self._fs)]
        write('output.wav', self._fs, self._audio)

    def playback_recording(self):
        sd.play(self._audio, samplerate=self._fs)
