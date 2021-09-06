from kivy.app import App
from kivy.uix.label import Label

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

#C:\windows\Fonts

resource_add_path('D:\Desktop\pyautoGUI')
LabelBase.register(DEFAULT_FONT,'meiryo.ttc')

class TextApp(App):
    def bulid(self):
        return Label(text='コンチネンタル')

TextApp().run()