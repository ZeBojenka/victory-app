[app]

# Название приложения
title = VictoryApp

# Имя пакета
package.name = victoryapp

# Домен пакета
package.domain = org.example

# Версия приложения
version = 0.1

# Директория с исходным кодом
source.dir = .

# Включаемые расширения файлов
source.include_exts = py,png,jpg,kv,atlas,wav

# Требования
requirements = 
    python3,
    kivy==2.2.0,  # Используем более стабильную версию
    plyer

# Ориентация
orientation = portrait

# Настройки Android
android.api = 33
android.minapi = 21
android.ndk = 23b  # Более стабильная версия NDK
android.archs = arm64-v8a  # Только 64-битная архитектура
android.allow_backup = True

# Разрешения
android.permissions = INTERNET, VIBRATE

# Настройки сборки
p4a.branch = 2023.08.24  # Конкретная версия python-for-android
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
