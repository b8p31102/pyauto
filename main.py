import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from kivy.app import App

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.config import Config #縦横の高さ指定
Config.set('graphics', 'width','640')
Config.set('graphics','height','480')
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import random
#C:\windows\Fonts

resource_add_path("font")  # 追加分
LabelBase.register(DEFAULT_FONT, 'meiryo.ttc')  # 追加分

resource_add_path('/image')

class ImageWidget(Widget): #全体のwidget,image表示
    source = StringProperty('image/00.jpg')

    def __init__(self, **kwargs): #これは定型文
        super(ImageWidget,self).__init__(**kwargs)
        pass
 
    def buttonStarted(self): #初めに戻るボタンイベント
        import auto
        auto.auto_main()
    
    def buttonRandom(self):
        self.source='image/0' + str(random.randint(1, 9)) +'.jpg'
    

class HigurashiApp(App):
    def __init__(self,**kwargs):
        super(HigurashiApp,self).__init__(**kwargs)
        self.title = 'ひぐらしのなく頃にの画像'

if __name__ =='__main__': #↑classと同じ名前に
    HigurashiApp().run()


