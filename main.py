from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import TouchRippleButtonBehavior, ButtonBehavior
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.metrics import sp, dp 

import re


class Clav(TouchRippleButtonBehavior, Label):
    def __init__(self, *args, **kwargs):
        super(Clav, self).__init__(*args, **kwargs)
        self.font_size = sp(48)
        self.markup = True

    def click_add(self, wid, *args):        
        if self.text == "c":
            
            self.parent.parent.parent.parent.operation_obj.text = ""
            self.parent.parent.parent.parent.result_obj.text = ""
            
            self.text = "."
        else:
            wid.text += self.text      


class MainWidget(BoxLayout):
    operation_obj = ObjectProperty()
    result_obj = ObjectProperty()
    # clavier = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orientation = "vertical"

    # def get_result(self, pattern, *args):
    #     regex = re.compile(r'(^\d*|\.\d*)\+|-|/|\*(\d*|\.\d*$)')
    #     if regex.match(pattern):
    #         self.result_obj.text = str(eval(self.operation_obj.text))
    #     pass

    def click_equal(self, *args):
        if "x" not in self.operation_obj.text:
            self.result_obj.text = str(round(eval(self.operation_obj.text), 10))
        else:
            self.new_operation_obj = self.operation_obj.text.replace("x", "*")
            self.result_obj.text = str(round(eval(self.new_operation_obj), 10))

        for child in self.ids.grid.children:
            
            if child.text == ".":
                child.color = (236/255, 137/255, 116/255, 1)
                child.text = "c"


class Calculator(App):

    def advanced_function(self, *args):
        pass

    def supprim(self, wid, *args):
        l = list(wid.text)
        if l:
            l.pop()
        ch = "".join(l)
        wid.text = ch
        pass

    def build(self):
        return MainWidget()

if __name__ == "__main__":
    from kivy.config import  Config
    Config.set("graphics", "width", 380)
    Config.set("graphics", "height", 650)

    Calculator().run()
