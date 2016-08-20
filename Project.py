

# pr(map)
class Players:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.speedX=0
        self.speedY=0
        self.sX = 0
        self.sY = 0

    def draw(self):
        # self.sX=0
        # self.sY=0


        map[self.y-self.sY][self.x-self.sX]='-'
        map[self.y][self.x]="p"

    def control(self):
        n = input("Please input your step: ")
        return n

    def TrialMove(self):
        n = self.control()

        self.speedX = 0
        self.speedY = 0
        if n == 'a':
            self.speedX = -1

        if n == 'w':
            self.speedY = -1
        if n == 'd':
            self.speedX = 1
        if n == 's':
            self.speedY = 1

    def checkPlayer(self):

        c1 = (self.x + self.speedX >= 0) and (self.x + self.speedX <= mapX - 1)
        c2 = (self.y + self.speedY >= 0) and (self.y + self.speedY <= mapY - 1)
        if (c1) and (c2) == True:
            return True
        else:
            return False


    def findBehindBox(self):

        n=-1
        for box in listBox:
            c1 = (self.x + self.speedX == box.x)
            c2 = (self.y + self.speedY == box.y)

            if ((c1) and (c2))==True:
                n=listBox.index(box)
        return n
    
    def check1Box(self):
        if self.findBehindBox()>-1:
            return True
        else:
            return False

    def check2Box(self):

        i=0
        if self.check1Box() == True:
            for box in listBox:
                c1 = (self.x + 2*self.speedX == box.x)
                c2 = (self.y + 2*self.speedY == box.y)
                if (c1) and (c2) == True:
                    i=i+1
        if i==0:
            return True
        else:
            return False


    def checkBoxLine(self):
        n=self.findBehindBox()
        if n<0:
            return True
        else:
            if listBox[n].checkBox() == True:
                return True
            else:
                False

    def checkRock(self):
        c=True

        for rock in listRock:
            c1 = (self.x + self.speedX == rock.x)
            c2 = (self.y + self.speedY == rock.y)
            if ((c1) and (c2)) == True:
                c= c and False

        return c

    def check_Box_Rock(self):
        n = self.findBehindBox()
        if n < 0:
            return True
        else:
            if listBox[n].checkRock() == True:
                return True
            else:
                False



    def check(self):
        c = self.check2Box() and self.checkBoxLine() and self.checkPlayer() and self.checkRock() and self.check_Box_Rock()
        if (c) == True:
            return True
        else:
            return False


    def update(self):

        self.TrialMove()
        self.sX=0
        self.sY=0
        if self.check() == True:
            self.sX=self.speedX
            self.sY=self.speedY
        self.x=self.x+self.sX
        self.y = self.y + self.sY
        self.draw()
        

      
class Boxes:
    def __init__(self,x,y):
        self.x=x
        self.y=y



    def TrialMove(self,p):

        self.speedX = p.speedX
        self.speedY = p.speedY

    def checkBox(self):

        c1 = (self.x + player.speedX >= 0) and (self.x + player.speedX <= mapX - 1)
        c2 = (self.y + player.speedY >= 0) and (self.y + player.speedY <= mapY - 1)
        if (c1) and (c2) == True:
            return True
        else:
            return False

    def checkRock(self):
        for rock in listRock:
            c = True

            for rock in listRock:
                c1 = (self.x + player.speedX == rock.x)
                c2 = (self.y + player.speedY == rock.y)
                if (c1 and c2 == True):
                    c = c and False

        return c


    def update(self):

        c1 = (player.x==self.x)
        c2 = (player.y==self.y)
        c3 = player.check()
        if (c1 and c2 and c3 == True):
            self.x=self.x+player.sX
            self.y = self.y + player.sY
            # self.draw()

    def draw(self):
        map[self.y][self.x] = 'b'
    

class Doors:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def draw(self):
        c1 = (self.x!=player.x) or (self.y!=player.y)
        c2 = True
        for box in listBox:
            c3 = (self.x!=box.x) or (self.y!=box.y)
            c2 = (c2 and c3)
        if (c1 and c2) == True:

            map[self.y][self.x]='d'

class Rock:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        map[self.y][self.x]="r"

import listMap

mapX=listMap.mapX
mapY=listMap.mapY
map=[]

for i in range(mapY):
    m1=["-"]*mapX
    map.append(m1)


def pr(map):
    for i in map:
            for j in i:
                print(j,' ',end='')
            print()



positionPerson=listMap.positionPerson
player=Players(positionPerson[0],positionPerson[1])
positionDoor=listMap.positionDoor
positionBox=listMap.positionBox
positionRock=listMap.positionRock
n=len(positionBox)


listDoor=[]
for i in range(len(positionDoor)):
    d=Doors(positionDoor[i][0],positionDoor[i][1])
    listDoor.append(d)

listBox=[]
for i in range(len(positionBox)):
    d=Boxes(positionBox[i][0],positionBox[i][1])
    listBox.append(d)

listRock=[]
for i in range(len(positionRock)):
    d=Rock(positionRock[i][0],positionRock[i][1])
    listRock.append(d)


player.draw()

for i in range(n):
    listBox[i].draw()
    listDoor[i].draw()

for i in range(len(listRock)):
    listRock[i].draw()

def Win():
    k=0
    for i in range(n):
        for j in range(n):
            c1 = (listDoor[i].x == listBox[j].x)
            c2 = (listDoor[i].y == listBox[j].y)
            if (c1 and c2) == True:
                k=k+1
    return k

level=1
pr(map)
print(mapX,mapY)
# while True:
#     player.update()
#
#     for i in range(n):
#         listBox[i].update()
#
#         listBox[i].draw()
#     player.draw()
#     for i in range(n):
#         listDoor[i].draw()
#
#     for i in range(len(listRock)):
#         listRock[i].draw()
#
#     pr(map)
#
#     if Win() == n:
#         print("You win")
#         break







