from kivy.app import App
from kivy.uix.button import Button

class VictoryApp(App):
    def build(self):
        my_but = Button()
        return my_but

if __name__ == '__main__':
    VictoryApp().run()
