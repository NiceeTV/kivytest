from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout
from kivy.uix.relativelayout import RelativeLayout
import threading
import obd
from obd import OBDStatus
import time
from kivy.clock import Clock

n = 0

class BoxL(BoxLayout):
    global n
    def __init__(self, **kwargs):
        global connection, connected, ids
        super(BoxL, self).__init__()

        connected = False
        connection = obd.OBD()


        n = 0

        ids = self.ids

        t2 = threading.Thread(target=self.checkConnection)
        t2.start()




    def checkConnection(self):
        global n

        c = []

        if connection.status() == OBDStatus.OBD_CONNECTED or connection.status() == OBDStatus.ELM_CONNECTED:
            connected = True
            c = [0,1,0.5,1]
        else:
            connected = False
            c = [0,0,1,1]


        ids.b1.background_color = c







class MainWidget(Widget):
    pass

class TestApp(App):
    def build(self):
        return BoxL()

    def on_start(self):
        Clock.schedule_interval(BoxL.checkConnection,1)

TestApp().run()