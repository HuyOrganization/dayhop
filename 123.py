from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, \
    ObjectProperty, StringProperty, ListProperty
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.layout import Layout
from kivy.uix.floatlayout import FloatLayout


import listMap
from kivy.core.window import Window
listDoor = listMap.positionDoor
listBox = listMap.positionBox
listRock = listMap.positionRock
positionPerson = listMap.positionPerson
X = listMap.mapX
Y = listMap.mapY

def adjustmap(map,x, y):
    for element in map:
        element[0] = element[0] + y
        element[1] = element[1] + x
    return map

size = 50
Y = (12 - Y)//2
X = (16 - X)//2
listDoor = adjustmap(listDoor,X,Y)
listBox = adjustmap(listBox,X,Y)
listRock = adjustmap(listRock,X,Y)
positionPerson[0] += Y
positionPerson[1] += X

while len(listBox) < 4:
    listBox.append([-1, -1])
while len(listDoor) < 4:
    listDoor.append([-1, -1])

class Player(Widget):
    px = NumericProperty(positionPerson[1]*size + 5)
    py = NumericProperty(positionPerson[0]*size)
    # print(Project.positionPerson[0], Project.positionPerson[1])
    pos = ReferenceListProperty(px,py)
    image_ = StringProperty("Character4.png")
    speedX = NumericProperty(0)
    speedY = NumericProperty(0)

    def checkrock(self):
        for rock in listRock:
            c1 = (rock[1] * size == self.px - 5 + self.speedX)
            c2 = (rock[0] * size == self.py + self.speedY)
            if (c1 and c2 == True):
                return True
        return False

    def checkbox(self,lbox):
        for i in range(4):
            c1 = (lbox[i].px == self.px - 5 + self.speedX)
            c2 = (lbox[i].py == self.py + self.speedY)
            if (c1 and c2 == True):
                return i

        return -1

    def checkafterbox(self,box,lbox):
        print(listRock)
        for rock in listRock:
            c1 = (rock[1] * size == box.px + self.speedX)
            c2 = (rock[0] * size == box.py + self.speedY)
            if (c1 and c2 == True):
                return True
        for box_ in lbox:
            c1 = (box_.px == box.px + self.speedX)
            c2 = (box_.py == box.py + self.speedY)
            print(c1, c2)
            if (c1 and c2 == True):
                return True
        return False

    def move(self):
        self.px += self.speedX
        self.py += self.speedY

    def moveBox(self, box):
        box.px = box.px + self.speedX
        box.py = box.py + self.speedY

    def update(self, lbox, ldoor):

        if self.checkrock() == False:
            t = self.checkbox(lbox)

            if t == -1:
                self.move()
            elif self.checkafterbox(lbox[t],lbox) == False:
                self.moveBox(lbox[t])
                self.move()


class Box(Widget):

        # import Project

    # print(Project.positionPerson[0], Project.positionPerson[1])
    px = NumericProperty(0)
    py = NumericProperty(0)
    pos = ReferenceListProperty(px,py)

    image_ = StringProperty("Crate_Yellow.png")


class Door(Widget):

        # import Project


    px = NumericProperty(-1)
    py = NumericProperty(-1)
    # print(Project.positionPerson[0], Project.positionPerson[1])
    pos = ReferenceListProperty(px,py)
    image_ = StringProperty("door.png")


class SokobanGame(FloatLayout):


    #nguoi choi
    player = ObjectProperty(None)

    #tao hop
    box1 = ObjectProperty(None)
    box2 = ObjectProperty(None)
    box3 = ObjectProperty(None)
    box4 = ObjectProperty(None)

    #taocua
    door1 = ObjectProperty(None)
    door2 = ObjectProperty(None)
    door3 = ObjectProperty(None)
    door4 = ObjectProperty(None)

    def initbox(self):
        box = [self.box1,self.box2,self.box3,self.box4]
        for i in range(4):
            box[i].px = listBox[i][1]*50
            box[i].py = listBox[i][0]*50

    def initdoor(self):
        door = [self.door1,self.door2,self.door3,self.door4]
        for i in range(4):
            door[i].px = listDoor[i][1]*50 + 10
            door[i].py = listDoor[i][0]*50 + 10

    def draw(self):
        with self.canvas:
            for rock in listRock:
                self.add_widget(Image(source='Wall_Beige.png', pos_hint={"x": rock[1]/16, "y": rock[0]/12}, size_hint = (1/16, 1/12)))

            # for x in range(16):
            #     #print(x / 16)
            #     self.add_widget(Image(source='Wall_Beige.png', pos_hint={"x": x/16,"y": 0 }, size_hint = (1/16, 1/12)))
            #     self.add_widget(Image(source='Wall_Beige.png', pos_hint={"x": x/16,"y": 11/12}, size_hint = (1/16, 1/12)))
            # for y in range(12):
            #     self.add_widget(Image(source='Wall_Beige.png', pos_hint={"x": 0,"y": y/12}, size_hint=(1/16, 1/12)))
            #     self.add_widget(Image(source='Wall_Beige.png', pos_hint={"x": 15/16,"y": y/12 }, size_hint=(1/16, 1/12)))

    def __init__(self, **kwargs):
        super(SokobanGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.player.speedX = 0
        self.player.speedY = 0
        if keycode[1] == 'left':
            self.player.speedX = -size
        elif keycode[1] == 'right':
            self.player.speedX = size
        elif keycode[1] == 'up':
            self.player.speedY = size
        elif keycode[1] == 'down':
            self.player.speedY = -size

        # # for box in self.listBox:
        # #     self.player.moveBox(self.box)
        # self.player.moveBox(self.box)
        box = [self.box1,self.box2,self.box3,self.box4]
        door = [self.door1,self.door2,self.door3,self.door4]
        self.player.update(box,door)

class SokobanApp(App):
    #t1 = 40
    def build(self):
        game = SokobanGame()
        game.initbox()
        game.initdoor()
        game.draw()
        # Clock.schedule_interval(1.0 / 60.0)  # Vòng lặp fps game

        return game


if __name__ == "__main__":
    SokobanApp().run()