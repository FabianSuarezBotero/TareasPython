from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout

class mensaje(App):

  def build(self):
    boxl = BoxLayout()

    def tex(instance,value):
      print('Felicitaciones, se ha ganado el baloto!')

      tiquet = Label(text = 'Ha ganado', font_size = 30)
      barra = Slider(orientation = 'vertical',
                    min = -5,
                    max = 5, 
                    value = 0,
                    value_track = True,
                    value_track_color = (1,0,1,1))

      boton = Button(text='Presiona')
      boton.bind(state = tex)
      boxl.add_widget(barra)
      boxl.add_widget(boton)
      boxl.add_widget(tiquet)
    return boxl

if __name__ == "__main__":
  mensaje().run()