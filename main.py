from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from plyer import notification
from kivy.utils import platform
from kivy.clock import Clock

class VictoryApp(App):
    def build(self):
        self.sound = None
        # Загружаем звук при запуске
        self.load_sound()
        
        self.button = Button(
            text="НАЖМИ МЕНЯ!",
            font_size=50,
            background_color=(0, 1, 0, 1),
            size_hint=(0.8, 0.5),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.button.bind(on_press=self.play_victory)
        
        layout = BoxLayout()
        layout.add_widget(self.button)
        return layout

    def load_sound(self):
        # Загрузка звука при старте
        try:
            self.sound = SoundLoader.load('victory.wav')
            if not self.sound:
                print("Ошибка загрузки звука")
        except Exception as e:
            print(f"Ошибка загрузки звука: {str(e)}")

    def play_victory(self, instance):
        # Воспроизведение звука
        if self.sound:
            try:
                self.sound.play()
            except Exception as e:
                print(f"Ошибка воспроизведения: {str(e)}")
        else:
            print("Звук не загружен")
        
        # Показ уведомления
        try:
            notification.notify(
                title='УСПЕХ!',
                message='Мы создали рабочее Android приложение!',
                timeout=5
            )
        except Exception as e:
            print(f"Ошибка уведомления: {str(e)}")

    # Обработка паузы для Android
    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ == '__main__':
    VictoryApp().run()
