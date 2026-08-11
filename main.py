from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import TouchRippleButtonBehavior, ButtonBehavior
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.metrics import sp, dp 

import re


class Clav(TouchRippleButtonBehavior, Label):
    def __init__(self, **kwargs):
        super(Clav, self).__init__(**kwargs)
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

    def _validate_expression(self, expression):
        """Valide que l'expression ne contient que des caractères autorisés"""
        if not expression:
            return False
        # Autorise uniquement les chiffres, opérateurs, parenthèses et points
        allowed_pattern = r'^[\d+\-*/().\s]+$'
        return bool(re.match(allowed_pattern, expression))

    def click_equal(self, *args):
        try:
            expression = self.operation_obj.text
            
            # Remplacer 'x' par '*' pour la multiplication
            if "x" in expression:
                expression = expression.replace("x", "*")
            
            # Valider l'expression avant évaluation
            if not self._validate_expression(expression):
                self.result_obj.text = "Erreur: Caractères invalides"
                return
            
            # Évaluer l'expression en toute sécurité
            result = eval(expression)
            
            # Arrondir le résultat pour éviter les problèmes de virgule flottante
            if isinstance(result, float):
                result = round(result, 10)
            
            self.result_obj.text = str(result)
            
        except ZeroDivisionError:
            self.result_obj.text = "Erreur: Division par zéro"
        except SyntaxError:
            self.result_obj.text = "Erreur: Expression invalide"
        except Exception as e:
            self.result_obj.text = "Erreur"

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
    from kivy.config import Config
    Config.set("graphics", "width", 380)
    Config.set("graphics", "height", 750)

    Calculator().run()
