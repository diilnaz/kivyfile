from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random



class MainApp(App):
    def build(self):
        layout = BoxLayout(padding=20, orientation='vertical')
        colors = ['pink', 'blue', 'purple', 'green']
        for i in range(5):
            btn = Button(text='Кнопка №%s' % (i + 1), background_color=random.choice(colors))
            layout.add_widget(btn)
        return layout


if __name__ == '__main__':
    MainApp().run()
