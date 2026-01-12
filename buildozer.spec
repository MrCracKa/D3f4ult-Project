[app]
title = D3f4ult
package.name = d3f4ult
package.domain = org.godfather
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# المتطلبات اللي بتخلي السكريبت "فتاك" وقادر يتعامل مع النظام
requirements = python3,kivy==2.1.0,pyjnius==1.4.0,requests,urllib3

orientation = portrait

# --- Android specific ---
fullscreen = 0
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,FOREGROUND_SERVICE,WAKE_LOCK

# المعمارية الأهم للموبايلات الحديثة
android.archs = arm64-v8a

# نسخ الـ API اللي بتعدي من حماية الأندرويد
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31

# السطر ده هو "كلمة السر" عشان البناء يكمل للاخر
android.accept_sdk_license = True

android.private_storage = True
android.release_artifact = apk
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
