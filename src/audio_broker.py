import sounddevice as sd
import src.audio_recording as rec_object
from scipy.io.wavfile import write
import time
from kivy.core.audio import SoundLoader


class AudioBroker:
    def __init__(self):
        print('loading main...')
        self._fs = 44100
        self._seconds = 400  # maximum seconds of recording
        self._audio = []
        self._start = 0
        self._end = 0
        self.recording_view = None
        self.recording_count = 0
        self.recordings = {}

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
        self.recording_count += 1
        path = 'recording_' + str(self.recording_count) + '.wav'
        sl_rec = SoundLoader.load(path)
        rec = rec_object.AudioRecording(self.recording_count, path, self._audio, sl_ref=sl_rec)
        self.recordings[rec.name] = rec
        write(path, self._fs, self._audio)
        self.recording_view.add_button(rec.name, path)

    def playback_recording(self, recording_name=None):
        # check if using playback button
        if recording_name is None:
            sd.play(self._audio, samplerate=self._fs)
            return

        rec = self.recordings[recording_name]
        if rec.is_looping:
            rec.is_looping = False
            rec.sl_ref.stop()
        else:
            rec.is_looping = True
            rec.sl_ref.loop = rec.is_looping
            rec.sl_ref.play()
