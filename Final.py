import math;import pygame;import random;import time;from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((1550,850),pygame.RESIZABLE)
background=pygame.image.load("4k.jpg");name=pygame.image.load("cooltext.png");start_but1 = pygame.image.load("play.png")
start_but2 = pygame.image.load("play bright.png");quit_but1 = pygame.image.load("quit.png");quit_but2 = pygame.image.load("quit bright.png")
single_but1 = pygame.image.load("single.png");single_but2 = pygame.image.load("single bright.png")
multi_but1 = pygame.image.load("multi.png");multi_but2 = pygame.image.load("multi bright.png")
inst_but1 = pygame.image.load("instructions.png");inst_but2 = pygame.image.load("instructions bright.png")
back_but1 = pygame.image.load("back.png");back_but2 = pygame.image.load("back bright.png")
player1name=pygame.image.load("player 1 Name.png");player2name=pygame.image.load("player 2 Name.png")
bs1=pygame.mixer.Sound("brick1.mpeg");bs2=pygame.mixer.Sound("brick2.mpeg")
buzz=pygame.mixer.Sound("buzzer.mp3");click=pygame.mixer.Sound("click.mp3");background2=pygame.image.load("4k2.jpg")
pygame.mixer.music.load("backgroundmus.mp3")
pygame.mixer.music.play(-1)
bslist=[bs1,bs2]
def blit_but(inst_but1,quit_but1,single_but1,multi_but1):#Passive
    screen.blit(single_but1,(240,310))
    screen.blit(multi_but1,(240,410))
    screen.blit(inst_but1,(240,510))
    screen.blit(quit_but1,(240,610))
def blit_but2(inst_but2,quit_but2,single_but2,multi_but2):#Active
    if mx in range(240,700) and my in range(340,400):
        screen.blit(single_but2,(240,310))
    if mx in range(240,650) and my in range(440,500):
        screen.blit(multi_but2,(240,410))
    if mx in range(240,650) and my in range(540,600) :
        screen.blit(inst_but2,(240,510))
    if mx in range(240,400) and my in range(640,700) :
        screen.blit(quit_but2,(240,610))

pygame.display.set_caption("COLLIDE")

icon = pygame.image.load("medicine-ball.png")
pygame.display.set_icon(icon)
bricks1 = bricks2 = bricks3 = bricks4 = bricks5 = bricks6 = bricks7 = bricks8 = []
def initialize():
    global bricks1, bricks2, bricks3, bricks4, bricks5, bricks6, bricks7, bricks8, ballY, ballX, ballX1, ballY1, count1, count2, speed_x, speed_y, speed_x1, speed_y1
    bricks1 = [[550,50],[600,50],[650,50],[700,50],[750,50],[800,50],[850,50],[900,50]]
    bricks2 = [[550,150],[600,150],[650,150],[700,150],[750,150],[800,150],[850,150],[900,150]]
    bricks3 = [[550,250],[600,250],[650,250],[700,250],[750,250],[800,250],[850,250],[900,250]]
    bricks4 = [[550,350],[600,350],[650,350],[700,350],[750,350],[800,350],[850,350],[900,350]]
    bricks5 = [[550,450],[600,450],[650,450],[700,450],[750,450],[800,450],[850,450],[900,450]]
    bricks6 = [[550,550],[600,550],[650,550],[700,550],[750,550],[800,550],[850,550],[900,550]]
    bricks7 = [[550,650],[600,650],[650,650],[700,650],[750,650],[800,650],[850,650],[900,650]]
    bricks8 = [[550,750],[600,750],[650,750],[700,750],[750,750],[800,750],[850,750],[900,750]]
    ballX = random.randint(450,500)*2
    ballY = random.randint(75,375)*2
    ballX1 = random.randint(75,125)*2
    ballY1 = random.randint(75,375)*2
    count1 = 0
    count2 = 0
    speed_y = 2
    speed_x = 2
    speed_x1 = 2
    speed_y1 = 2
colors=["red","blue","green","yellow","orange","purple","brown","pink"]
l=[]
col=[]
while len(col) <= 7:
    a=random.randint(0,7)
    if a not in l:
        l.append(a)
        col.append(colors[a])
C0,C1,C2,C3,C4,C5,C6,C7=0,1,2,3,4,5,6,7
c=3
ball_ = pygame.transform.scale(pygame.image.load("medicine-ball.png"),(15,15))
pad_1 = pygame.transform.scale(pygame.image.load("minus1.png"),(90,190))
pad1X = 40
pad1Y = 300
pad1Y_change = 0
pad_2 = pygame.transform.scale(pygame.image.load("minus1.png"),(90,190))
pad2X = 1400
pad2Y = 300
pad2Y_change = 0
pads=3
bug = 0
players=0
ballX = random.randint(450,500) * 2
ballY = random.randint(75,375) * 2
ballX1 = random.randint(75,125) * 2
ballY1 = random.randint(75,375) * 2
#MESSAGE FOR P-WON,PAUSE,STARTING
font=pygame.font.SysFont("Times new roman",150,True,True)
def msg_on_screen(msg,color,x,y):
    screen_text=font.render(msg,True,color)
    screen.blit(screen_text,(x,y))
#PLAYER LIVES
livesfont=pygame.font.SysFont("Times new roman",32,True,True)
def lives(msg,color,x,y):
    screen_text=livesfont.render(msg,True,color)
    screen.blit(screen_text,(x,y))
#INSTRUCTIONS
instfont=pygame.font.SysFont("Calibri",32,False,True)
def inst1(msg,color,x,y):
    screen_text=instfont.render(msg,True,color)
    screen.blit(screen_text,(x,y))
def inst():
    inst1("    Each Player has 3 lives.","white",250,350)
    inst1("    Player 1 controls the paddle by Keys: 8 (to move up) and 2 (to move down).","white",250,450)
    inst1("    Player 2 controls the paddle by Keys: W (to move up) and S(to move down)","white",250,550)
def collide(ballX,ballY,bricks0,a,b,col,Cx,c):#(DETERMINES THE COLLISIONS OF GIVEN LISTS)
    screen.blit(ball_,(ballX,ballY))
    for brick in bricks0 :
        rectangle = pygame.Rect(brick[0],brick[1],10,30)#Bricks characteristics
        pygame.draw.rect(screen,pygame.Color(col[Cx]),rectangle,c)
        # Collission on Sides
        if (rectangle.left == ballX + 14 and -30 < rectangle.top - ballY < 15) or (
                rectangle.right == ballX and -30 < rectangle.top - ballY < 15) :
            bricks0.remove(brick)

            pygame.mixer.Sound.play(random.choice(bslist))
            a = -1 * a
            return a,b
        # Collission on Top and Bottom
        if (rectangle.bottom == ballY and 15 > rectangle.left - ballX > -11) or (
                rectangle.top == ballY + 16 and 15 > rectangle.left - ballX > -11) :
            bricks0.remove(brick)
            pygame.mixer.Sound.play(random.choice(bslist))
            b = -1 * b
            return a,b
    return a,b
#TO GET COLLISION FOR ALL BRICKS
def collide2(ballX,ballY,bricks1,bricks2,bricks3,bricks4,bricks5,bricks6,bricks7,bricks8,speed_x,speed_y,col,collide):
    speed_x,speed_y = collide(ballX,ballY,bricks1,speed_x,speed_y,col,C0,3)
    speed_x,speed_y = collide(ballX,ballY,bricks2,speed_x,speed_y,col,C1,10)
    speed_x,speed_y = collide(ballX,ballY,bricks3,speed_x,speed_y,col,C2,3)
    speed_x,speed_y = collide(ballX,ballY,bricks4,speed_x,speed_y,col,C3,10)
    speed_x,speed_y = collide(ballX,ballY,bricks5,speed_x,speed_y,col,C4,3)
    speed_x,speed_y = collide(ballX,ballY,bricks6,speed_x,speed_y,col,C5,10)
    speed_x,speed_y = collide(ballX,ballY,bricks7,speed_x,speed_y,col,C6,3)
    speed_x,speed_y=  collide(ballX,ballY,bricks8,speed_x,speed_y,col,C7,10)
    return speed_x,speed_y
#COLLISION BETWEEN BALL AND PAD
def ball_collide(ballX,ballY,speed_x,speed_y,pad1Y,pad2Y):
    global bug
    if ballY >= 800 :
        speed_y = -1 * speed_y
        ballY=796
    if ballY <= 0:
        speed_y = -1 * speed_y
        ballY = 6
    if ballX <= 85 and ballX >=80:
        if  pad1Y+60  < ballY < (pad1Y + 130) :
            speed_x = -1 * speed_x
            ballX = 88
            bug = random.randint(-105,105)
        elif pad1Y-10  < ballY < (pad1Y + 190):
            speed_x = -1 * speed_x
            speed_y = -1 * abs(speed_y)
            ballX = 88
            bug = random.randint(-105,105)
    if ballX >= 1430 and ballX <= 1435:
        if  pad2Y+60  < ballY < (pad2Y + 130) :
            speed_x = -1 * speed_x
            ballX =1428
        elif  pad2Y-10  < ballY < (pad2Y + 190) :
            speed_x = -1 * speed_x
            speed_y = -1 * speed_y
            ballX =1428
    return speed_x,speed_y,ballY,ballX
def pad_on_screen (pad_1,pad1X,pad1Y,pad_2,pad2X,pad2Y) :#(BLITING PAD ON SCREEN)
    screen.blit(pad_1,(pad1X,pad1Y))
    screen.blit(pad_2,(pad2X,pad2Y))
#PLAYER NAMES
namefont=pygame.font.SysFont("Calibri",64,False,True)
p1="Player 1"
p2="Player 2"
color_active=pygame.Color("purple")
color_passive=pygame.Color("white")
color1=color_passive
active1=False
color2=color_passive
active2=False
#TAKING PLAYER'S NAMES
def playernaam(p1,RX,RY,color1):
    pygame.draw.rect(screen,color1,pygame.Rect(RX,RY,550,80),5)
    p_surface = namefont.render(p1,True,(35,211,255))#(color in rgb)
    screen.blit(p_surface,(RX+10,RY+10))
def menu_display_2players(start_but1,back_but1):
    screen.fill((0,0,0))
    screen.blit(background,(20,0))
    screen.blit(start_but1,(240,610))
    screen.blit(back_but1,(1000,610))
    screen.blit(player1name,(240,210))#images
    screen.blit(player2name,(240,410))#images
    playernaam(p1,500,320,color1)
    playernaam(p2,500,510,color2)
    pygame.display.update()
def menu_display_1player(back_but2,start_but1):
    screen.fill((0,0,0))
    screen.blit(background,(20,0))
    screen.blit(back_but2,(1000,610))
    screen.blit(start_but1,(240,610))
    screen.blit(player1name,(240,310))#images
    playernaam(p1,500,450,color1)
    pygame.display.update()

running = True
game_on=False
menu =True
instructions = False
names=False
pause=False

while running :
    pygame.time.Clock().tick(600)
    if menu:
        background=pygame.image.load("4k.jpg")
        screen.blit(background,(20,0))
        screen.blit(name,(500,150))
        mx,my = pygame.mouse.get_pos()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
                menu = False
            if (mx in range(240,700) and my in range(340,400)) or (mx in range(240,650) and my in range(440,500)) or \
                    (mx in range(240,650) and my in range(540,600)) or (mx in range(240,400) and my in range(640,700)) :
                blit_but(inst_but1,quit_but1,single_but1,multi_but1)
                blit_but2(inst_but2,quit_but2,single_but2,multi_but2)
                pygame.display.update()
            else :
                blit_but(inst_but1,quit_but1,single_but1,multi_but1)
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1 and ((mx in range(240,650) and my in range(440,500)))  :#MULTIPLAYER
                    pygame.mixer.Sound.play(click)
                    players=2
                    menu = False
                    initialize()
                    names = True
                if event.button == 1 and ((mx in range(240,650) and my in range(540,600))) :#INSTRUCTIONS
                    pygame.mixer.Sound.play(click)
                    instructions=True
                    menu=False
                if event.button == 1 and mx in range(240,400) and my in range(640,700) :#QUIT BUTTON
                    pygame.mixer.Sound.play(click)
                    running = False
                    menu = False
                if event.button ==1 and mx in range(240,700) and my in range(340,400):#SINGLE PLAYER
                    pygame.mixer.Sound.play(click)
                    players=1
                    menu = False
                    initialize()
                    names = True
    if instructions:
        mx,my = pygame.mouse.get_pos()
        for event in pygame.event.get() :
            if (mx in range(1000,1200) and my in range(620,680)):
                screen.fill((0,0,0))
                screen.blit(background,(20,0))
                screen.blit(back_but2,(1000,610))
                screen.blit(name,(500,150))
                inst()
                pygame.display.update()
            else:
                screen.fill((0,0,0))
                screen.blit(background,(20,0))
                screen.blit(back_but1,(1000,610))
                screen.blit(name,(500,150))
                inst()
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1 and ((mx in range(1000,1200) and my in range(620,680))) :
                    pygame.mixer.Sound.play(click)
                    menu=True
                    instructions=False
                    pygame.display.update()
            if event.type == pygame.QUIT :
                running = False
    if names:
        mx,my = pygame.mouse.get_pos()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
            if players == 2 :
                if event.type == pygame.MOUSEBUTTONDOWN :
                    if event.button == 1 and (mx in range(500,1050) and my in range(320,400)) :
                        pygame.mixer.Sound.play(click)
                        active1 = True
                    else :
                        active1 = False
                    if event.button == 1 and (mx in range(500,1050) and my in range(510,590)) :
                        pygame.mixer.Sound.play(click)
                        active2=True
                    else:
                        active2=False
                    pygame.display.update()
                if event.type == pygame.KEYDOWN :
                    if active1 == True :
                        if event.key == pygame.K_BACKSPACE :
                            p1 = p1[:-1]
                        elif len(p1)<=8:
                            p1 += event.unicode
                        color1 = color_active
                    if active2 == True :
                        if event.key == pygame.K_BACKSPACE :
                            p2 = p2[:-1]
                        elif len(p2)<=8:
                            p2 += event.unicode
                if active1==True:
                    color1=color_active
                else:
                    color1=color_passive
                if active2==True:
                    color2=color_active
                else:
                    color2=color_passive
                if (mx in range(1000,1200) and my in range(620,680)) :
                    menu_display_2players(start_but1,back_but2)
                elif (mx in range(240,400) and my in range(620,680)) :
                    menu_display_2players(start_but2,back_but1)
                else :
                    menu_display_2players(start_but1,back_but1)
            if players==1:
                if event.type == pygame.MOUSEBUTTONDOWN :
                    if event.button == 1 and (mx in range(500,1050) and my in range(450,530)) :
                        pygame.mixer.Sound.play(click)
                        active1 = True
                    else :
                        active1 = False
                    pygame.display.update()
                if event.type == pygame.KEYDOWN :
                    if active1 == True :
                        if event.key == pygame.K_BACKSPACE :
                            p1 = p1[:-1]
                        elif len(p1)<=8:
                            p1 += event.unicode
                if active1==True:
                    color1=color_active
                else:
                    color1=color_passive
                if (mx in range(1000,1200) and my in range(620,680)) :
                    menu_display_1player(back_but2,start_but1)
                elif (mx in range(240,400) and my in range(620,680)) :
                    menu_display_1player(back_but1,start_but2)
                else :
                    menu_display_1player(back_but1,start_but1)
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1 and ((mx in range(1000,1200) and my in range(620,680))) :#MENU BUTTON
                    pygame.mixer.Sound.play(click)
                    menu = True
                    names = False
                    pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1 and ((mx in range(240,400) and my in range(620,680))) :#PLAY BUTTON
                    pygame.mixer.Sound.play(click)
                    for i in range(3,0,-1) :
                        screen.blit(background,(20,0))
                        msg_on_screen(f"Game starts in:{i}","white",270,350)
                        pygame.display.update()
                        time.sleep(1.5)
                    screen.blit(background,(20,0))
                    game_on = True
                    names = False
                    pygame.display.update()
    if pause:
        msg_on_screen("      PAUSED","white",270,350)
        pygame.display.update()
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_c:
                    pause=False
                    game_on=True
            if event.type == pygame.QUIT :
                running = False
    if game_on:
        for event in pygame.event.get() :
            screen.blit(background,(20,0))
            if event.type == pygame.QUIT :
                running = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_KP8 :
                    pad2Y_change -= pads
                if event.key == pygame.K_KP2 :
                    pad2Y_change += pads
                if event.key == pygame.K_p:
                    game_on=False
                    pause=True
                if players==2:
                    if event.key == pygame.K_w :
                        pad1Y_change -= pads
                    if event.key == pygame.K_s :
                        pad1Y_change += pads
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_KP8 :
                    pad2Y_change = 0
                if event.key == pygame.K_KP2 :
                    pad2Y_change = 0
                if event.key == pygame.K_w :
                    pad1Y_change = 0
                if event.key == pygame.K_s :
                    pad1Y_change = 0
        if players == 1 :
            if pad1Y + 95 + bug > ballY and ballX < ballX1 :
                pad1Y -= pads
            if pad1Y + 95 + bug < ballY and ballX < ballX1 :
                pad1Y += pads
            if (pad1Y + 95 + bug > ballY1) and (ballX > ballX1) :
                pad1Y -= pads
            if (pad1Y + 95 + bug < ballY1) and (ballX > ballX1) :
                pad1Y += pads
        screen.fill((0,0,0))
        screen.blit(background,(20,0))
        if players ==2:
            lives(f"{p2}-lives:{3 - count2}","red",30,30)
        if players ==1:
            lives(f"Computer-lives:{3-count2}","red",30,30)
        lives(f"{p1}-lives:{3 - count1}","red",1280,30)
        pad_on_screen(pad_1,pad1X,pad1Y,pad_2,pad2X,pad2Y)
        speed_x,speed_y=collide2 (ballX,ballY,bricks1,bricks2,bricks3,bricks4,bricks5,bricks6,bricks7,bricks8,speed_x,speed_y,col,
                      collide)#Brick Collsion ball 1
        speed_x1,speed_y1=collide2(ballX1,ballY1,bricks1,bricks2,bricks3,bricks4,bricks5,bricks6,bricks7,bricks8,speed_x1,speed_y1,col,
                 collide)#Brick Collsion ball 2
        speed_x,speed_y,ballY,ballX=ball_collide(ballX,ballY,speed_x,speed_y,pad1Y,pad2Y)#Pad collision ball 1
        speed_x1,speed_y1,ballY1,ballX1=ball_collide(ballX1,ballY1,speed_x1,speed_y1,pad1Y,pad2Y)#Pad collision ball 2
        if ballX1 >= 1500 or ballX >= 1500 :
            pygame.mixer.Sound.play(buzz)
            count1+=1
            pygame.display.update()
            time.sleep(2)
            if ballX>=1500:
                ballX = random.randint(450,500)*2
                ballY = random.randint(75,375)*2
                speed_x = -1 * abs(speed_x)
            if ballX1>=1500:
                ballX1 = random.randint(450,500)*2
                ballY1 = random.randint(75,375)*2
                speed_x1 = -1*abs(speed_x1)
            if count1==3:
                time.sleep(2)
                screen.blit(background,(20,0))
                if players==2:
                    msg_on_screen(f"  {p2} won","white",270,350)
                elif players==1:
                    msg_on_screen("  Computer won","white",270,350)
                pygame.display.update()
                time.sleep(5)
                menu=True
                game_on=False
        if ballX1 <= 0 or ballX <= 0 :
            pygame.mixer.Sound.play(buzz)
            count2+=1
            bug=0
            pygame.display.update()
            time.sleep(2)
            if ballX1<=0:
                ballX1 = random.randint(75,125)*2
                ballY1 = random.randint(75,375)*2
                speed_x1 = abs(speed_x1)
            if ballX<=0:
                ballX = random.randint(75,125)*2
                ballY = random.randint(75,375)*2
                speed_x = abs(speed_x)
            if count2==3:
                time.sleep(2)
                screen.blit(background,(20,0))
                msg_on_screen(f"  {p1} won","white",270,350)
                pygame.display.update()
                time.sleep(5)
                menu = True
                game_on = False
        if pad1Y <= 0 :
            pad1Y = 0
        if pad1Y >= 800 - 190 :
            pad1Y = 800 - 190
        if pad2Y <= 0 :
            pad2Y = 0
        if pad2Y >= 800 - 190 :
            pad2Y = 800 - 190
        if ((len(bricks1) + len(bricks2) + len(bricks3) + len(bricks4) + len(
                bricks5) + len(bricks6) + len(bricks7) + len(bricks8) == 5) and -3 < speed_y < 3) :
            bricks1.clear(),bricks2.clear(),bricks3.clear(),bricks4.clear(),bricks5.clear(),bricks6.clear(),
            bricks7.clear(),bricks8.clear(),
            screen.fill((0,0,0))
            background=background2
            screen.blit(background,(20,0))
            level = pygame.transform.scale(pygame.image.load("img.png"),(350,350))
            screen.blit(level,(600,270))
            pygame.display.update()
            time.sleep(2)

            ballX = random.randint(450,500) * 2
            ballY = random.randint(75,375) * 2
            ballX1 = random.randint(125,175) * 2
            ballY1 = random.randint(75,375) * 2
            speed_x =-3.5
            speed_y = 3.5
            speed_x1 = 3.5
            speed_y1 = 3.5
            pads = 4

        ballX += speed_x
        ballY += speed_y
        ballX1+=speed_x1
        ballY1+=speed_y1
        pad1Y += pad1Y_change
        pad2Y += pad2Y_change
        pygame.display.update()