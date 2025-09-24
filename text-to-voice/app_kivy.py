from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.text_input = TextInput(hint_text="Enter your name")
        self.button = Button(text="Say Hello")
        self.button2 = Button(text="Clear")
        self.label = Label(text="")

        self.button.bind(on_press=self.say_hello)
        self.button2.bind(on_press=self.clear_text)

        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.button2)
        self.layout.add_widget(self.label)

        return self.layout

    def say_hello(self, instance):
        name = self.text_input.text
        self.label.text = f"Hello, {name}!"

    def clear_text(self, instance):
        self.text_input.text = ""
        self.label.text = ""


if __name__ == "__main__":
    MyApp().run()
