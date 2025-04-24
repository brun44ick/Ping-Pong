from pygame import *
from random import*
#создай окно игры
WIN_W = 700
WIN_H = 500
speed = 5
step = 5
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
FPS = 60
pole = 'grizly-club-p-zadnii-fon-terrariya-les-1.jpg'
player1 = 'Grass Dirt Platform (1).png'
player2 = 'Grass Dirt Platform (0).png'
sharik = 'png-klev-club-clrd-p-glaz-ktulkhu-png-14.png'

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h):
        super().__init__()
        self.image = transform.scale(
            image.load(img),
            (w, h)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, ing, x, y, w, h, speed=step):
        super().__init__(ing, x,y,w,h)
        self.speed = speed

    def update(self,up,down):
        keys_pressed = key.get_pressed()
        if keys_pressed[up] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[down] and self.rect.y < WIN_W - self.rect.width:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, ing, x,y, w, h, speed):
        super().__init__(ing, x,y,w,h)
        self.speed = speed
        self.rect.x = 300
        self.rect.y = 230

class Ball(GameSprite):
    def __init__(self, ing,x,y, sizeX, sizeY, speed):
        super().__init__(ing, x,y,sizeX,sizeY)
        self.speed_x = speed * choice([-1, 1])
        self.speed_y = speed * choice([-1, 1])
    
    def update(self):
        if self.rect.x <= 0 or self.rect.x >= WIN_W - self.rect.width:
            self.speed_x *= -1
        self.rect.x += self.speed_x

        if self.rect.y <= 0 or self.rect.y >= WIN_H - self.rect.height:
            self.speed_y *= -1
        self.rect.y += self.speed_y


window = display.set_mode((WIN_W, WIN_H))
clock = time.Clock()
display.set_caption("Mazeself.speed")

background = GameSprite(pole,0,0,WIN_W, WIN_H)
ball = Ball(sharik, 300,230,130,100,4)
pl1 = Player(player1, 5,140,30,130, speed)
pl2 = Player(player2, 590, 100, 200,200,speed)

#self, ing, x, y, w, h,

font.init()
title_font = font.SysFont('arial', 70)
win = title_font.render('WIN!', True,GREEN)
lose = title_font.render('LOSE!', True,RED)

font.init()
label_font = font.SysFont('arial', 20)
count_txt = label_font.render('Счетчик', True,WHITE)
miss_txt = label_font.render('Пропущено', True,WHITE)

finish = False
game = True
while game:
    if not finish:
        
        background.draw(window)
        ball.draw(window)
        ball.update()
        pl1.draw(window)
        pl2.draw(window)
        pl1.update(K_w,K_s)
        pl2.update(K_UP, K_DOWN)
        
        
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    display.update()
    clock.tick(FPS)
