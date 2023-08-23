from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text="Welcome to Demo App", halign="center", theme_text_color="Error")
        return label


if __name__ == '__main__':
    DemoApp().run()
