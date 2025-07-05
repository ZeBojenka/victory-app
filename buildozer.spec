[app]

title = VictoryApp
package.name = victoryapp
package.domain = org.example
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav
requirements = python3, kivy==2.2.0, plyer
orientation = portrait

# Android settings
android.api = 33
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a
android.permissions = INTERNET, VIBRATE

# macOS settings
osx.python_version = 3
osx.kivy_version = 2.2.0

# Build settings
android.accept_sdk_license = True
p4a.branch = master

# Ускорение сборки
android.skip_update = True
p4a.ignore_setup_py = True

# Оптимизация Gradle
android.gradle_dependencies = 
    'com.android.tools.build:gradle:7.2.2'
    'org.jetbrains.kotlin:kotlin-gradle-plugin:1.7.20'

[buildozer]
log_level = 2
warn_on_root = 1
