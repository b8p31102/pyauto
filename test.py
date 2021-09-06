from kivy.app import App

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

#C:\windows\Fonts

resource_add_path('c:/Windows/Fonts')  # 追加分
LabelBase.register(DEFAULT_FONT, 'msgothic.ttc')  # 追加分

class TestApp(App):
    pass

if __name__ =='__main__':
    TestApp().run()


