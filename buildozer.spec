[app]

# (str) Title of your application
title = VictoryApp

# (str) Package name
package.name = victoryapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,wav

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = 
    python3,
    kivy==2.3.0,
    plyer

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/images/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/images/favicon.png

# (list) Supported orientations
orientation = portrait

# Android specific
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# (list) Permissions
android.permissions = INTERNET, VIBRATE

[buildozer]
log_level = 2
warn_on_root = 1
