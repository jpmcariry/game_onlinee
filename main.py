import requests
from kivy.app import App
from kivy.uix.image import Image, AsyncImage
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.core.window import Keyboard
from kivy.clock import Clock
#from sys import platform
from kivy.metrics import *
from kivy.lang import Builder
from kivy.core.window import Window
import uuid
import time
import sqlite3
ip = str(uuid.getnode())
path = r'Database'
conn = sqlite3.connect(path + '/data.db')
cursor = conn.cursor()
cursor.execute("""
create table if not exists cadastro(
    restart integer default 0
);
""")
#Window.fullscreen = True
'''from kivy.core.image import Image as CoreImage
data = io.BytesIO(open("img/Mapa.jpg", "rb").read())
im = CoreImage(data, ext="jpg",pos_hint={'x':0.0, 'y':0.0})'''
from kivy.utils import platform
if platform == 'android':
    system = "android"
elif platform == "linux" or platform == "linux2" or platform == "darwin":
    system = "linux"
elif platform == "win32":
    system = "Win"
size_map=[3000,2000]
canwalk_map=[[000,-200,000,-300]]
anim_forward=int(time.time())
system="android"

def xc():
    print("bt")
Window.size=(800,600)
print(20*Window.size[0]/600)
class Opcoes(FloatLayout):
    cancel = ObjectProperty(None)
class Main(Screen):
    def jogar(self,btn):
        screen_manager.current = selecao.name

    def dismiss_popup(self,btn):
        self._popup.dismiss()
    def resolution(self,op):
        if(self.res.text=="800x600"):
            self.res.text="1080x720"
        elif(self.res.text=="1080x720"):
            self.res.text = "1920x1080"
        else:
            self.res.text = "800x600"
    def opcoes(self,d):
        self.op=Opcoes()
        #gd.add_widget(Button(text="gd"))
        self.lb=Label(text="resolução", size_hint= (None,None))
        self.btn=Button(text="confirmar",size_hint=(0.4,0.2),background_color=(0.5,1,0.5,0.5),on_press=self.dismiss_popup)
        self.btn.pos_hint={"x":(0.5-(self.btn.size_hint[0]/2)),"y":0.0}
        self.btn.background_normal=""
        self.gd = GridLayout(cols=2, size_hint=(0.8, 1-self.btn.size_hint_y))
        self.gd.pos_hint={"x":0.1,"y":self.btn.size_hint_y}
        self.gd.name = "gd"
        print(self.gd.name, self.gd.name)
        self.gd.background_normal = ""
        self.gd.background_color = (0.5, 1, 0.5, 0.5)
        self.gd.add_widget(Label(text="Resolução"))
        self.res=Button(text="800x600", on_release=self.resolution)
        self.gd.add_widget(self.res)
        self.gd.add_widget(Label(text="rs"))
        self.gd.add_widget(Button(text="oie"))
        self.op.add_widget(self.gd)
        self.op.add_widget(self.btn)
        content = self.op
        self._popup = Popup(title="Configurações", content=content,size_hint=(None,None),
                            size=(500,350), pos=(400-(self.size[0]/2), 300-(self.size[1]/2)))
        self._popup.open()

main = Main(name="main")

main_layout_title = Label(text="Fight Battle",font_name="font/mv-boli.ttf",color=(0,0,0,1), size_hint=(0.23,0.3),font_size =sp(82*Window.size[1]/600))
main_layout_title.pos_hint = {"x":0.523-(main_layout_title.size_hint_x/2),"y":0.653}

main_layout_btn_jogar_image=Image(source="img/bg/bg_botao.jpg",size_hint= (.255,.109), allow_stretch=True, keep_ratio=False)
main_layout_btn_opcoes_image=Image(source="img/bg/bg_btn_opcoes.jpg",size_hint= (.255,.109), allow_stretch=True, keep_ratio=False)

main_btn_jogar = Button(text="jogar",opacity= 0.0, size_hint= (.255,.109),on_press = main.jogar)
main_layout_btn_jogar_image.pos_hint = main_btn_jogar.pos_hint = {"x":0.522-float(main_btn_jogar.size_hint_x/2),"y":0.415}

main_btn_opcao = Button(text="opções",opacity= 0.0,size_hint=(.255,.109),on_press = main.opcoes)
main_layout_btn_opcoes_image.pos_hint=main_btn_opcao.pos_hint= {"x":0.522-float(main_btn_opcao.size_hint_x/2),"y":0.29}

main_image = Image(source="img/bg/tela_bg.jpg")
main_image.allow_stretch = True
main_image.keep_ratio = False
main_layout = FloatLayout()
main_layout.add_widget(main_image)
main_layout.add_widget(main_layout_btn_jogar_image)
main_layout.add_widget(main_layout_btn_opcoes_image)
main_layout.add_widget(main_btn_jogar)
main_layout.add_widget(main_btn_opcao)
main_layout.add_widget(main_layout_title)

main.add_widget(main_layout)

class Selecao(Screen):
    def jogar(self, btn):
        screen_manager.current = selecao.name

    def dismiss_popup(self, btn):
        self._popup.dismiss()

    def resolution(self, op):
        if (self.res.text == "800x600"):
            self.res.text = "1080x720"
        elif (self.res.text == "1080x720"):
            self.res.text = "1920x1080"
        else:
            self.res.text = "800x600"

    def opcoes(self, d):
        self.layout_internal = Opcoes()
        # gd.add_widget(Button(text="gd"))
        self.btn = Button(text="confirmar",font_size=sp(20*Window.size[1]/600), size_hint=(0.4, 0.15), background_color=(0.5, 1, 0.5, 0.5),
                          on_press=self.dismiss_popup)
        self.btn.pos_hint = {"x": (0.5 - (self.btn.size_hint[0] / 2)), "y": 0.1}
        self.btn.background_normal = ""
        self.gd = GridLayout(cols=2, size_hint=(0.5, 0.55 - self.btn.size_hint_y))
        self.gd.pos_hint = {"x": 0.5-(self.gd.size_hint_x/2), "y": self.btn.size_hint_y+self.btn.pos_hint["y"]}
        self.icone = Image(source="img/icone/img_vazia.jpg", size_hint=(0.25, 0.25), keep_ratio=False, allow_stretch=True)
        self.icone.pos_hint = {"x": 0.5 - (self.icone.size_hint_x / 2), "y":self.gd.pos_hint["y"]+self.gd.size_hint_y}
        self.count_lb = 3
        self.lb_name = Label(text="Nome:", size_hint=(0.5, 2 + 1 / self.count_lb), font_size=sp(18*Window.size[1]/600))
        self.lb_name_value = Label(text="120", size_hint=(0.5, 2 + 1 / self.count_lb), font_size=sp(18*Window.size[1]/600))
        self.lb_ataque = Label(text="Ataque:", size_hint=(0.5, 2+1/self.count_lb), font_size=sp(18*Window.size[1]/600))
        self.lb_ataque_value = Label(text="120", size_hint=(0.5, 2+1/self.count_lb), font_size=sp(18*Window.size[1]/600))
        self.lb_vida = Label(text="Vida", size_hint=(0.5, 2+1/self.count_lb), font_size=sp(18*Window.size[1]/600))
        self.lb_vida_value = Label(text="200", size_hint=(0.5, 2+1/self.count_lb), font_size=sp(18*Window.size[1]/600))
        self.pass_left = Button(size_hint=(0.17, 0.3), background_normal="img/seta_left.png")
        self.pass_left.pos_hint={"x": 0.02 - (self.pass_left.size_hint_x / 2), "y":0.5-(self.pass_left.size_hint_y/2)}
        self.pass_right = Button(size_hint=(0.17, 0.3), background_normal="img/seta_right.png")
        self.pass_right.pos_hint = {"x": 0.97 - (self.pass_right.size_hint_x / 2),
                                   "y": 0.5 - (self.pass_right.size_hint_y / 2)}
        self.layout = FloatLayout()
        self.layout.orientation = "horizontal"
        self.layout.size_hint = (1, 1)
        self.layout.pos_hint = {"x": 0.5 - (self.layout.size_hint[0] / 2), "y": 0.5 - (self.layout.size_hint[1] / 2)}
        self.layout_image = Image(source="img/hd-800/fundo.jpg", size_hint=(1, 1), keep_ratio=False, allow_stretch=True)
        self.layout_image.pos_hint = {"x": 0.0, "y": 0.0}  # self.layout.pos_hint
        self.layout_internal.size_hint=(self.layout.size_hint[0]*0.8,self.layout.size_hint[1]*0.8)
        self.layout_internal.pos_hint = {"x":self.layout.pos_hint["x"]+((1-self.layout_internal.size_hint_x)/2),"y":self.layout.pos_hint["y"]+((1-self.layout_internal.size_hint_y)/2)}
        self.layout_internal_image = Image(source="img/bg/fundo_grid.jpg", size_hint=(0.7,1), keep_ratio=False, allow_stretch=True)
        self.layout_internal_image.pos_hint={"x":0.5-(self.layout_internal_image.size_hint_x/2),"y":0.}
        self.layout_internal.add_widget(self.layout_internal_image)
        self.layout_internal.add_widget(self.pass_left)
        self.layout_internal.add_widget(self.pass_right)
        self.layout_internal.add_widget(self.icone)
        self.layout_internal.add_widget(self.gd)
        self.layout_internal.add_widget(self.btn)
        self.gd.add_widget(self.lb_name)
        self.gd.add_widget(self.lb_name_value)
        self.gd.add_widget(self.lb_ataque)
        self.gd.add_widget(self.lb_ataque_value)
        self.gd.add_widget(self.lb_vida)
        self.gd.add_widget(self.lb_vida_value)
        self.layout.add_widget(self.layout_image)
        self.layout.add_widget(self.layout_internal)
        content = self.layout
        self._popup = Popup(title="Personagem Selection", content=content, size_hint=(0.65,0.8))
        self._popup.pos_hint={"x": 0.5-(self._popup.size_hint_x/2),"y": 0.5-(self._popup.size_hint_y/2)}
        self._popup.open()

selecao = Selecao(name="selecao")
sel_txti = TextInput(size_hint= (0.285,0.085),multiline= False)
sel_txti.pos_hint= {"x": 0.5-sel_txti.size_hint_x, "y": 0.67}

sel_btn_check = Button(text= "check",size_hint=(0.1285,0.085),pos_hint= {"x": 0.5, "y": 0.67})
sel_btn_icone = Button(size_hint= (0.155, 0.17), on_press= selecao.opcoes,opacity= 0.3)
sel_btn_icone.pos_hint= {"x": 0.5+sel_btn_check.size_hint_x, "y": 0.67}
sel_icone = Image(source="img/icone/img_vazia.jpg", size_hint=sel_btn_icone.size_hint, pos_hint=sel_btn_icone.pos_hint)
sel_icone.allow_stretch = True
sel_icone.keep_ratio = False

sel_grid_image = Image(source= "img/bg/fundo_grid.jpg",size_hint=(0.57, 0.5), allow_stretch=True, keep_ratio=False)
sel_grid_image.pos_hint = {"x": 0.5-(sel_grid_image.size_hint_x/2), "y": 0.17}
sel_grid = GridLayout(cols = 2,size_hint=(0.57, 0.5))
sel_grid.pos_hint = {"x": 0.5-(sel_grid.size_hint_x/2), "y": 0.17}
for i in range(1,3+1):
    sel_grid.add_widget(Label(text="Server"+str(i)))
    sel_grid.add_widget(Button(text="Entrar"+str(i)))
sel_image = Image(source="img/fullhd/fundo.jpg",allow_stretch=True,keep_ratio=False)
sel_layout = FloatLayout()

sel_layout.add_widget(sel_image)
sel_layout.add_widget(sel_txti)
sel_layout.add_widget(sel_btn_check)
sel_layout.add_widget(sel_icone)
sel_layout.add_widget(sel_btn_icone)
sel_layout.add_widget(sel_grid_image)
sel_layout.add_widget(sel_grid)


selecao.add_widget(sel_layout)

class Loading(Screen):
    pass

class Loading_Layout(FloatLayout):
    fps = StringProperty(None)

    def __init__(self, **kwargs):
        super(Loading_Layout, self).__init__(**kwargs)
        Clock.schedule_once(self.conn, 0)

    def conn(self, dt):
        try:
            url = "http://10.0.0.109:5000/register"
            json = {"user_ip": ip, "user_resoluction": "1280x299"}
            headers = {"Content-Type": "application/json"}
            response = requests.post(url=url, json=json, headers=headers,
                                     verify=False)  # envia token + json ignorando SSl(certificado)
            self.text = str(response.json())
        except:
            print("timeout")
            Clock.schedule_once(self.conn, 6)
        else:
            screen_manager.current = "main"

loading_bg_image = Image(source="img/bg/loading_bg.jpg", size_hint=(1,1), allow_stretch=True, keep_ratio=False)
loading_image = Image(source="img/connection.gif",size_hint=(0.2,0.2),anim_delay=0.04, allow_stretch=True,keep_ratio=False)
loading_image.pos_hint={"x":0.65-(loading_image.size_hint_x/2),"y":0.5-(loading_image.size_hint_y/2)}
loading_label = Label(text="trying connection: ", font_size = sp(20*Window.size[1]/600))
loading_label.pos_hint ={"x":0.45-(loading_label.size_hint_x/2),"y":0.5-(loading_label.size_hint_y/2)}
loading_layout =Loading_Layout()
loading_layout.add_widget(loading_bg_image)
loading_layout.add_widget(loading_label)
loading_layout.add_widget(loading_image)

loading = Loading(name="loading")
loading.add_widget(loading_layout)

class WindowManager(ScreenManager):
    pass
# Create the screen manager
screen_manager = WindowManager()
screen_manager.transition = FadeTransition()
screen_manager.add_widget(loading)
screen_manager.add_widget(main)
screen_manager.add_widget(selecao)


class GameApp(App):
    def build(self):
        return screen_manager

if __name__ == '__main__':
    GameApp().run()
