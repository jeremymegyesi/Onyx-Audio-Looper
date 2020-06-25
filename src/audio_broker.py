import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import time


class AudioBroker:
    def __init__(self):
        print("loading main...")
        self._fs = 44100
        self._seconds = 100  # maximum seconds of recording
        self._audio = []
        self._start = 0
        self._end = 0

    def start_recording(self, instance):
        print('commencing recording...')
        self._start = time.time()
        self._audio = sd.rec(int(self._seconds * self._fs), samplerate=self._fs, channels=2)

    def end_recording(self, instance):
        sd.stop()
        self._end = time.time()
        print('completed')
        elapsed = int(self._end - self._start)
        print(elapsed)
        self._audio = self._audio[:elapsed * self._fs]
        write('output.wav', self._fs, self._audio)
