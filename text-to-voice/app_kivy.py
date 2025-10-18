from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from dictations_file import Dictation


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dictation = Dictation()
    def build(self):
        self.title = "Text to Voice"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.text_input = TextInput(hint_text="Enter text here...", size_hint=(1, 0.6))
        layout.add_widget(self.text_input)

        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.2))

        speak_button = Button(text="Speak", on_press=self.speak_text)
        button_layout.add_widget(speak_button)

        record_button = Button(text="Record Voice", on_press=self.record_voice)
        button_layout.add_widget(record_button)

        layout.add_widget(button_layout)

        return layout

    def speak_text(self, instance):
        text = self.text_input.text
        self.dictation.tell(text)
        

    def record_voice(self, instance):
        pass  # Implement voice recording functionality here


if __name__ == "__main__":
    MyApp().run()
