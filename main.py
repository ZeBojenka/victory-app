from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from plyer import notification

class VictoryApp(App):
    def build(self):
        # Создаем кнопку
        self.button = Button(
            text="НАЖМИ МЕНЯ!",
            font_size=50,
            background_color=(0, 1, 0, 1),  # Зеленый цвет
            size_hint=(0.8, 0.5),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.button.bind(on_press=self.play_victory)
        
        # Размещаем кнопку
        layout = BoxLayout()
        layout.add_widget(self.button)
        return layout

    def play_victory(self, instance):
        # Воспроизводим звук
        sound = SoundLoader.load('victory.wav')
        if sound:
            sound.play()
        
        # Показываем уведомление
        notification.notify(
            title='УСПЕХ!',
            message='Мы создали рабочее Android приложение!',
            timeout=5  # Показывать 5 секунд
        )

if __name__ == '__main__':
    VictoryApp().run()