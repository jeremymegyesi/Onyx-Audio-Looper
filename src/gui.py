import src.audio_broker as ab
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class ControlButtons(GridLayout):
    def __init__(self, **kwargs):
        super(ControlButtons, self).__init__(**kwargs)
        self.audio_broker = ab.AudioBroker()
        self.cols = 1
        self.record = Button(text="Record Audio", background_color=[0, 0.3, 0, 1], background_normal='')
        self.record.bind(on_press=self.record_clicked)
        self.add_widget(self.record)
        self.stop = Button(text="Stop Recording", disabled=True, background_color=[0.3, 0, 0, 1], background_normal='')
        self.stop.bind(on_press=self.stop_clicked)
        self.add_widget(self.stop)
        self.playback = Button(text="Playback", background_color=[0, 0.2, 0.5, 1], background_normal='')
        self.playback.bind(on_press=self.audio_broker.playback_recording)
        self.add_widget(self.playback)

    def record_clicked(self, instance):
        self.audio_broker.start_recording()
        self.record.disabled = True
        self.stop.disabled = False

    def stop_clicked(self, instance):
        self.audio_broker.end_recording()
        self.stop.disabled = True
        self.record.disabled = False

class MainGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)
        self.cols = 2  # Set columns for main layout

        # Add controller buttons on left side
        self.control_buttons = ControlButtons()

        self.add_widget(self.control_buttons)
        self.add_widget(Label(text="recording1.wav"))

class MyApp(App):
    def build(self):
        return MainGrid()


if __name__ == "__main__":
    MyApp().run()
