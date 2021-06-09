from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# Set the App size
Window.size = (500, 700)

Builder.load_file("calc.kv")


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    # create a function press button
    def button_press(self, button):
        # create a variable containing the text box
        prior = self.ids.calc_input.text

        if "Error" in prior:
            prior = ''

        # determine if 0 stays
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        # add + sign
        self.ids.calc_input.text = f"{prior}{sign}"

    # Création de la décimale
    def dot(self):
        prior = self.ids.calc_input.text
        # on separe les nombres
        num_list = prior.split("+")
        # si il y a un +  et si le dernier symbole n'est pas un .
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

    # On revient une saisie en arrière
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    # Rendre un nbr pos ou neg
    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def equals(self):
        prior = self.ids.calc_input.text
        try:
            # Fait le calcul
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
        """
        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            #on boucle la liste
            for number in num_list:
                answer = answer + float(number)
            # on affiche la réponse 
            self.ids.calc_input.text = str(answer)
        """


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()

