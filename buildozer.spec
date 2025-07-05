[app]

# Название приложения
title = VictoryApp

# Имя пакета
package.name = victoryapp

# Домен пакета
package.domain = org.example

# Директория с исходным кодом
source.dir = .

# Включаемые расширения файлов
source.include_exts = py,png,jpg,kv,atlas,wav,ttf

# Требования
requirements = 
    python3,
    kivy==2.3.0,
    plyer,
    android,
    jnius

# Преслаш
presplash.filename = %(source.dir)s/images/presplash.png

# Иконка
icon.filename = %(source.dir)s/images/favicon.png

# Ориентация
orientation = portrait

# Настройки Android
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.private_storage = True
android.enable_androidx = True

# Разрешения
android.permissions = 
    INTERNET,
    VIBRATE,
    RECEIVE_BOOT_COMPLETED,
    FOREGROUND_SERVICE

# Дополнительные манифесты
android.extra_manifest_xml = 
    <application android:usesCleartextTraffic="true">
        <meta-data android:name="com.google.android.gms.version" android:value="@integer/google_play_services_version" />
        <receiver android:name="org.kivy.android.PythonService" android:process=":python_service" />
        <service android:name="org.kivy.android.PythonService" android:process=":python_service" />
    </application>
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE"/>
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
    <uses-permission android:name="android.permission.VIBRATE"/>

# Настройки сборки
android.release_artifact = aab
android.debug_artifact = apk
p4a.branch = master
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
