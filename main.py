from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from plyer import notification
from kivy.utils import platform
from kivy.clock import Clock
import os

class VictoryApp(App):
    def build(self):
        self.sound = None
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

    def on_start(self):
        # Загрузка звука при старте приложения
        self.sound = SoundLoader.load('victory.wav')
        
        # Запрос разрешений для Android
        if platform == 'android':
            from android.permissions import request_permission, Permission
            permissions = [
                Permission.INTERNET,
                Permission.VIBRATE,
                Permission.RECEIVE_BOOT_COMPLETED
            ]
            request_permission(permissions)

    def play_victory(self, instance):
        # Воспроизведение звука
        if self.sound:
            self.sound.play()
        else:
            print("Звуковой файл не загружен")
        
        # Показ уведомления
        try:
            notification.notify(
                title='УСПЕХ!',
                message='Мы создали рабочее Android приложение!',
                timeout=5
            )
        except Exception as e:
            print(f"Ошибка уведомления: {str(e)}")
            # Попытка показать уведомление через Android API
            if platform == 'android':
                self.show_android_notification()

    def show_android_notification(self):
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Context = autoclass('android.content.Context')
            NotificationManager = autoclass('android.app.NotificationManager')
            NotificationBuilder = autoclass('android.app.Notification$Builder')
            NotificationChannel = autoclass('android.app.NotificationChannel')
            
            context = PythonActivity.mActivity.getApplicationContext()
            manager = context.getSystemService(Context.NOTIFICATION_SERVICE)
            
            # Создаем канал для Android 8+
            channel_id = "victory_channel"
            channel_name = "Victory Notifications"
            importance = NotificationManager.IMPORTANCE_HIGH
            channel = NotificationChannel(channel_id, channel_name, importance)
            manager.createNotificationChannel(channel)
            
            # Создаем уведомление
            builder = NotificationBuilder(context, channel_id)
            builder.setContentTitle("УСПЕХ!")
            builder.setContentText("Мы создали рабочее Android приложение!")
            builder.setSmallIcon(context.getApplicationInfo().icon)
            builder.setAutoCancel(True)
            
            # Показываем уведомление
            manager.notify(1, builder.build())
        except Exception as e:
            print(f"Ошибка создания уведомления: {str(e)}")

    # Обработка жизненного цикла Android
    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ == '__main__':
    VictoryApp().run()
