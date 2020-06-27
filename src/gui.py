import src.audio_broker as ab
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class ControlButtons(Widget):
    record_button = ObjectProperty(Button)
    stop_button = ObjectProperty(Button)
    play_button = ObjectProperty(Button)

    def __init__(self, **kwargs):
        super(ControlButtons, self).__init__(**kwargs)
        self.audio_broker = ab.AudioBroker()

    def record_clicked(self):
        self.audio_broker.start_recording()
        self.record_button.disabled = True
        self.stop_button.disabled = False

    def stop_clicked(self):
        self.audio_broker.end_recording()
        self.stop_button.disabled = True
        self.record_button.disabled = False


class MainGrid(Widget):
    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)


class OnyxAudioApp(App):
    def build(self):
        return MainGrid()


if __name__ == "__main__":
    OnyxAudioApp().run()
