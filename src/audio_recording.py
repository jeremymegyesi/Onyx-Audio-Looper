class AudioRecording:
    def __init__(self, recording_id, path, arr, sl_ref=None):
        self.id = recording_id
        self.name = 'recording_' + str(recording_id)
        self.path = path
        self.audio_array = arr
        self.is_looping = False
        self.sl_ref = sl_ref  # SoundLoader reference
