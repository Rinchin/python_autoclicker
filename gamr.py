from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyApp(App):
    """dockstring for MyApp"""
    def build(self):
        return Button(text="first button")

if __name__ == "__main__":
    MyApp().run()