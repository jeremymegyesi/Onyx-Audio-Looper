import src.audio_broker as ab
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        self.audio_broker = ab.AudioBroker()

        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2  # Set columns for main layout

        # Add controller buttons on left side
        self.controlButtons = GridLayout()
        self.controlButtons.cols = 1
        self.record = Button(text="Record Audio")
        self.record.bind(on_press=self.record_clicked)
        self.controlButtons.add_widget(self.record)
        self.stop = Button(text="Stop Recording", disabled=True)
        self.stop.bind(on_press=self.stop_clicked)
        self.controlButtons.add_widget(self.stop)

        self.add_widget(self.controlButtons)
        self.add_widget(Label(text="recording1.wav"))

    def record_clicked(self, instance):
        self.audio_broker.start_recording()
        self.record.disabled = True
        self.stop.disabled = False

    def stop_clicked(self, instance):
        self.audio_broker.end_recording()
        self.stop.disabled = True
        self.record.disabled = False

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
