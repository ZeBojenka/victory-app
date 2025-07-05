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

[buildozer]
log_level = 2
warn_on_root = 1
