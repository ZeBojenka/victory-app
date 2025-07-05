[app]

# (str) Название вашего приложения
title = SampleApp

# (str) Имя пакета
package.name = nfsApk

# (str) Домен пакета (необходим для сборки под Android/iOS)
package.domain = org.novfensec

# (str) Исходный код (где находится main.py)
source.dir = .

# (list) Включаемые файлы (оставьте пустым для включения всех файлов)
source.include_exts = py,png,jpg,kv,atlas

# (list) Шаблоны для включения файлов
source.include_patterns = images/*.png

# (list) Исключаемые расширения файлов
#source.exclude_exts = spec

# (list) Исключаемые директории
#source.exclude_dirs = tests, bin, venv

# (list) Шаблоны для исключения файлов
# Не используйте префикс './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Версия приложения (способ 1)
version = 0.1

# (str) Версия приложения (способ 2 - через регулярное выражение)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Зависимости приложения (добавлен plyer)
requirements = python3, kivy==2.3.1, https://github.com/kivymd/KivyMD/archive/master.zip, exceptiongroup, asynckivy, asyncgui, materialyoucolor, android, plyer

# (str) Кастомные исходники для зависимостей
# requirements.source.kivy = ../../kivy

# (str) Загрузочный экран приложения
presplash.filename = %(source.dir)s/images/presplash.png

# (str) Иконка приложения
icon.filename = %(source.dir)s/images/favicon.png

# (list) Поддерживаемые ориентации экрана
# Допустимые значения: landscape, portrait, portrait-reverse, landscape-reverse
orientation = portrait

# (list) Объявляемые сервисы (добавлен сервис для уведомлений)
services = PlyerNotification:plyer.platforms.android.notification.AndroidNotification

#
# Настройки для OSX
#

# Авторские права
# author = © Copyright Info

# Версия Python для сборки
osx.python_version = 3

# Версия Kivy
osx.kivy_version = 2.3.1

#
# Настройки для Android
#

# (bool) Полноэкранный режим (1 - да, 0 - нет)
fullscreen = 0

# (string) Цвет фона загрузочного экрана
#android.presplash_color = #FFFFFF

# (string) Анимация загрузочного экрана в формате Lottie
#android.presplash_lottie = "path/to/lottie/file.json"

# (str) Адаптивная иконка (для Android API 26+)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Требуемые разрешения (добавлены для работы уведомлений)
android.permissions = android.permission.VIBRATE, 
                      android.permission.RECEIVE_BOOT_COMPLETED,
                      android.permission.FOREGROUND_SERVICE

# (list) Особенности устройства
#android.features = android.hardware.usb.host

# (int) Целевая версия Android API (рекомендуется максимально возможная)
android.api = 35

# (int) Минимальная поддерживаемая версия Android API
android.minapi = 21

# (int) Версия Android SDK
#android.sdk = 20

# (str) Версия Android NDK
android.ndk = 25b

# (int) Минимальная версия NDK API
#android.ndk_api = 21

# (bool) Использовать приватное хранилище (True) или публичное (False)
#android.private_storage = True

# (str) Путь к Android NDK (если пусто - скачается автоматически)
#android.ndk_path =

# (str) Путь к Android SDK (если пусто - скачается автоматически)
#android.sdk_path =

# (str) Путь к ANT (если пусто - скачается автоматически)
#android.ant_path =

# (bool) Пропустить обновление Android SDK
# android.skip_update = False

# (bool) Автоматически принимать лицензии SDK
android.accept_sdk_license = True

# (str) Точка входа Android (по умолчанию подходит для Kivy)
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Полное имя класса активности Java
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Дополнительный XML для AndroidManifest.xml
# Для Android 8.0+ требуется канал уведомлений
# Создайте файл src/android/notification_channel.xml со следующим содержимым:
# <?xml version="1.0" encoding="utf-8"?>
# <channel xmlns:android="http://schemas.android.com/apk/res/android"
#     android:id="default_channel"
#     android:name="Default"
#     android:description="Default notifications"
#     android:importance="high"/>
android.extra_manifest_xml = ./src/android/notification_channel.xml

# (str) Дополнительные аргументы для тега <application>
#android.extra_manifest_application_arguments = ./src/android/extra_manifest_application_arguments.xml

# (str) Кастомный класс сервиса
#android.service_class_name = org.kivy.android.PythonService

# (str) Тема приложения
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Whitelist для всего проекта
#android.whitelist =

# (str) Файл whitelist
#android.whitelist_src =

# (str) Файл blacklist
#android.blacklist_src =

# (list) JAR-файлы для добавления в libs
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) Java-файлы для добавления в проект
#android.add_src =

# (list) AAR-архивы для добавления
#android.add_aars =

# (list) Ресурсы для добавления в assets
#android.add_assets =

# (list) Ресурсы для добавления в res
#android.add_resources =

# (list) Зависимости Gradle
#android.gradle_dependencies =

# (bool) Включить поддержку AndroidX
#android.enable_androidx = True

# (list) Опции компиляции Java
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Репозитории Gradle
#android.add_gradle_repositories =

# (list) Опции упаковки
#android.add_packaging_options =

# (list) Дополнительные активности
#android.add_activities = com.example.ExampleActivity

# (str) Категория для OUYA Console (GAME или APP)
#android.ouya.category = GAME

# (str) Иконка для OUYA (732x412 PNG)
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) Фильтры намерений (intent-filters)
#android.manifest.intent_filters =

# (list) XML-файлы для копирования в res/xml
#android.res_xml = PATH_TO_FILE,

# (str) Режим запуска активности
#android.manifest.launch_mode = standard

# (str) Ориентация активности
#android.manifest.orientation = fullSensor

# (list) Дополнительные библиотеки для разных архитектур
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Не выключать экран
#android.wakelock = False

# (list) Мета-данные приложения
#android.meta_data =

# (list) Ссылки на библиотечные проекты
#android.library_references =

# (list) Используемые shared-библиотеки
#android.uses_library =

# (str) Фильтры logcat
#android.logcat_filters = *:S python:D

# (bool) Только PID активности в logcat
#android.logcat_pid_only = False

# (str) Дополнительные аргументы adb
#android.adb_args = -H host.docker.internal

# (bool) Копировать библиотеки вместо сборки libpymodules.so
#android.copy_libs = 1

# (list) Поддерживаемые архитектуры (armeabi-v7a, arm64-v8a, x86, x86_64)
android.archs = arm64-v8a, armeabi-v7a

# (int) Кастомный versionCode
# android.numeric_version = 1

# (bool) Разрешить резервное копирование (Android API >=23)
android.allow_backup = True

# (str) Правила резервного копирования
# android.backup_rules =

# (str) Заполнители для AndroidManifest.xml
# android.manifest_placeholders = [:]

# (bool) Пропускать компиляцию .py файлов
# android.no-byte-compile-python = False

# (str) Формат релизной сборки (aab/apk/aar)
android.release_artifact = aab

# (str) Формат отладочной сборки (apk/aar)
android.debug_artifact = apk

#
# Настройки python-for-android (p4a)
#

# (str) URL репозитория p4a
#p4a.url =

# (str) Форк p4a
#p4a.fork = kivy

# (str) Ветка p4a
p4a.branch = master

# (str) Конкретный коммит p4a
#p4a.commit = HEAD

# (str) Директория клонирования p4a
#p4a.source_dir =

# (str) Локальные рецепты сборки
#p4a.local_recipes =

# (str) Хук для p4a
#p4a.hook =

# (str) Бутстрап для сборки
# p4a.bootstrap = sdl2

# (int) Порт для p4a
#p4a.port =

# (bool) Использовать setup.py
#p4a.setup_py = false

# (str) Дополнительные аргументы p4a
#p4a.extra_args = --blacklist-requirements=sqlite3,openssl

#
# Настройки для iOS
#

# (str) Путь к кастомной папке kivy-ios
#ios.kivy_ios_dir = ../kivy-ios
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# (str) Настройки ios-deploy
ios.ios_deploy_url = https://github.com/ios-control/ios-deploy
ios.ios_deploy_branch = master

# (bool) Разрешить подписание кода
ios.codesign.allowed = false

# (str) Сертификат для отладочной подписи
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) ID команды разработчиков
#ios.codesign.development_team.debug = <hexstring>

# (str) Сертификат для релизной подписи
#ios.codesign.release = %(ios.codesign.debug)s

# (str) ID команды для релиза
#ios.codesign.development_team.release = <hexstring>

# (str) URL для установки .ipa
#ios.manifest.app_url =

# (str) URL иконки (57x57) для отображения при загрузке
#ios.manifest.display_image_url =

# (str) URL иконки для iTunes (512x512)
#ios.manifest.full_size_image_url =

[buildozer]

# (int) Уровень логирования (0=только ошибки, 1=инфо, 2=дебаг)
log_level = 2

# (int) Предупреждать при запуске от root (0=False, 1=True)
warn_on_root = 1

# (str) Директория сборки
# build_dir = ./.buildozer

# (str) Директория выходных файлов
# bin_dir = ./bin
