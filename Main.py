import pygame as pg,random,os,sys
from pygame.constants import K_SPACE, KEYDOWN, QUIT, USEREVENT
from pygame.sprite import collide_mask
from pygame.time import Clock

def R(RP):
    try:
        BP=sys._MEIPASS
    except:
        BP=os.path.abspath(".")
    
    return os.path.join(BP,RP)



Icon=pg.image.load(R("Icon.ico"))
BG=pg.image.load(R("Sprites/BG.jpg"))
screen=pg.display.set_mode((BG.get_width()/2,BG.get_height()))
pg.init()
pg.display.set_caption("Dino Run")
pg.display.set_icon(Icon)
text_h=pg.font.Font(R("Sprites/LTEnergy.ttf"),50)


screen.blit(BG,(0,0))
Loading_Message=text_h.render("Loading",False,(255,0,0))
Loading_Message_Rect=Loading_Message.get_rect()
Loading_Message_Rect.center=screen.get_rect().center
screen.blit(Loading_Message,Loading_Message_Rect)
pg.display.flip()

clock=pg.time.Clock()
posx=0
speed=3
global Animation_Rate
Animation_Rate=0.1
Currect_Time=0
Jump=pg.mixer.Sound(R("Jump.wav"))
BGM=pg.mixer.Sound(R("BGM.wav"))
Lose=pg.mixer.Sound(R("Lose.wav"))
text=pg.font.Font(R("Sprites/LTEnergy.ttf"),16)

Speedup=pg.USEREVENT

def Background():
    global posx
    posx-=speed
    if posx<=-BG.get_width()/2:
        posx=0
    screen.blit(BG,(posx,0))

class Dino(pg.sprite.Sprite):
    class Animations():
        Dead=[]
        Jump=[]
        Run=[]
        Dino_Animations=[(Dead,"Dead",8),(Jump,"Jump",11),(Run,"Run",8)]
        for animation in Dino_Animations:
            for i in range(1,animation[2]):
                image=pg.image.load(R(f"Sprites/Dinosaur/{animation[1]}{i}.png")).convert_alpha()
                animation[0].append(pg.transform.scale(image,(image.get_width()/6,image.get_height()/6)))

    def __init__(self):
        super(Dino,self).__init__()
        self.images=Dino.Animations.Run
        self.index=0
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.topleft=(100,230)
        self.vely=0
        self.accy=0
        self.cooldown=False
        self.cooldowntimer=0
        self.dead=False
        self.reset=False

    def movements(self):

        if self.rect.y<230:
            self.accy=0.5
        else:
            self.vely=0

        for event in pg.event.get():
            if event.type==KEYDOWN:
                if event.key==pg.K_SPACE and self.cooldown==False and self.dead==False:
                    BGM.set_volume(0.1)
                    Jump.play()
                    self.accy=-12
                    self.cooldown=True
                    self.cooldowntimer=pg.time.get_ticks()
                if event.key==pg.K_ESCAPE:
                    sys.exit()
            elif event.type==QUIT:
                sys.exit()
            elif event.type==Speedup:
                global speed
                speed+=0.5
        self.vely+=self.accy

        if self.cooldown==True:
            if pg.time.get_ticks()-self.cooldowntimer>800:
                self.cooldown=False
    

    def Update(self):
        if self.dead==False:
            self.rect.y=self.rect.y+self.vely

            try:
                self.index+=Animation_Rate
                self.image=self.images[round(self.index)]
            except:
                self.index=0
                self.image=self.images[round(self.index)]
        else:
            try:
                if self.reset==False:
                    pg.time.wait(500)
                    self.index=0
                    self.reset=True
                self.index+=0.1
                self.image=Dino().Animations().Dead[round(self.index)]
            except:
                self.index=6
                self.image=Dino().Animations().Dead[round(self.index)]
                sys.exit()

            

class Cactus(pg.sprite.Sprite):
    def __init__(self):
        super(Cactus,self).__init__()
        image=pg.image.load(R("Sprites/Cactus/Cactus.png")).convert_alpha()
        self.image=pg.transform.scale(image,(image.get_width()/8,image.get_height()/8))
        self.mask=pg.mask.from_surface(self.image)
        self.rect=self.mask.get_rect()
        self.rect.left=screen.get_rect().right
        self.rect.bottom=300
        

    def Update(self):
        self.rect.x-=speed
        if self.rect.x<-self.rect.width:
            image=pg.image.load(R("Sprites/Cactus/Cactus.png")).convert_alpha()
            size=random.randint(6,10)
            self.image=pg.transform.scale(image,(image.get_width()/size,image.get_height()/size))
            self.mask=pg.mask.from_surface(self.image)
            self.rect=self.mask.get_rect()
            self.rect.bottom=300
            self.rect.left=screen.get_rect().right+random.randint(1,100)
played=0
def Collision():
    if pg.sprite.groupcollide(Dino_Group,Cactus_Group,0,0,collide_mask):
        Dino_Sprite.dead=True
        Dino_Sprite.images=Dino.Animations.Dead
        BGM.stop()
        global played
        if Lose.get_num_channels()==0 and played==0:
            Lose.play()
            played=1
        Death_Message=text_h.render("Game Over",False,(255,0,0))
        Death_Message_Rect=Death_Message.get_rect()
        Death_Message_Rect.center=screen.get_rect().center
        screen.blit(Death_Message,Death_Message_Rect)     
        global speed
        speed=0
        

Cactus_Sprite=Cactus()
Cactus_Group=pg.sprite.Group(Cactus_Sprite)

Dino_Sprite=Dino()
Dino_Group=pg.sprite.Group(Dino_Sprite)

def time():
    global Currect_Time
    if Dino_Sprite.dead==False:
        Currect_Time=str((pg.time.get_ticks()-loadtime)//1000)
    Time=text.render(Currect_Time,False,(255,255,255))
    Time_Rect=Time.get_rect()
    Time_Rect.centerx=screen.get_rect().centerx
    Time_Rect.y=50
    screen.blit(Time,Time_Rect)

loadtime=pg.time.get_ticks()

BGM.play(-1)

pg.time.set_timer(Speedup,10000,-1)
while 1:
    BGM.set_volume(1)
    Background()
    clock.tick(60)
    Dino_Group.draw(screen)
    Dino_Sprite.Update()
    Dino_Sprite.movements()
    Cactus_Group.draw(screen)
    Cactus_Sprite.Update()
    Collision()
    time()
    pg.display.update()