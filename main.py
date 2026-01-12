"""
Simple Kivy App Template
"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        title = Label(
            text='My App',
            size_hint_y=None,
            height=100,
            font_size=24
        )
        
        button = Button(
            text='Click Me',
            size_hint_y=None,
            height=50
        )
        button.bind(on_press=self.on_button_click)
        
        layout.add_widget(title)
        layout.add_widget(button)
        
        return layout
    
    def on_button_click(self, instance):
        print("Button clicked!")


if __name__ == '__main__':
    MyApp().run()
