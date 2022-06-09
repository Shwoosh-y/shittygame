from re import A
import pygame
import sys
import random
playtex = pygame.image.load("player.png")
plusone = pygame.image.load("+1.png")

pygame.init()
e = True
global score
score = 0
fps=30
fpsclock=pygame.time.Clock()
sur_obj=pygame.display.set_mode((400,300))
pygame.display.set_caption("Better")
White=(255,255,255)
Gray= (20,20,20)
p1=10
p2=10
speed=5.0
a = 3
x2=0
x1=0
x = 0
y = 0
while True:
    sur_obj.fill(Gray)
    pygame.draw.rect(sur_obj, (20,20,20), (p1, p2, 50, 50))
    sur_obj.blit(playtex, (p1, p2))
    #make the rectangle have a textur
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT]:
        p1 -= speed
    if key_input[pygame.K_UP]:
        p2 -= speed
    if key_input[pygame.K_RIGHT]:
        p1 += speed
    if key_input[pygame.K_DOWN]:
        p2 += speed

    #draw a circle in a random position
    def draw_circle():
        global e
        global x
        global y
        global a
        if e == True:
            x=random.randint(0,400)
            y=random.randint(0,300)
            e = False
            a +=1
        pygame.draw.circle(sur_obj, (0,0,255), (x,y), 5)
        sur_obj.blit(plusone, (x, y))
    def draw_circle2():
        global x2
        global y2
        global a
        if(a > 3):
            x2=random.randint(0,400)
            y2=random.randint(0,300)
            a = 0
        pygame.draw.circle(sur_obj, (255,0,0), (x2,y2), 5)
       
    def death():
        global a 
        global e 
        global score
        global speed 
        global p1 
        global p2
        e = True
        a = 4
        score = 0
        speed = 4.8
        #teleport the rectangle to 0 0
        p1 = 10
        p2 = 10
    
    #make circle disapear after collision with rectangle
    if p1+50>x and p1<x+5 and p2+50>y and p2<y+5:
        e = True
        score += 1
        #play sound e.wav
        pygame.mixer.music.load("collect.wav")
        pygame.mixer.music.play()

    #call death() when touching red circle
    if p1+50>x2 and p1<x2+5 and p2+50>y2 and p2<y2+5:
        death()
        #play sound d.wav
        pygame.mixer.music.load("death.wav")
        pygame.mixer.music.play()

    #if p1+70>x>p1 and p2+65>y>p2:
    #    e = True
     #   score += 1
      #  #play sound collect.wav
       # pygame.mixer.music.load("collect.wav")
        #pygame.mixer.music.play()
    #display score
    font=pygame.font.SysFont(None,25)
    text=font.render("Score: "+str(score),True,(125,125,125))
    sur_obj.blit(text,(15,15))
    #make walls around the screen
    wall1a = 0
    wall1b = 0
    wall1c = 400
    wall1d = 10
    wall2a = 0
    wall2b = 0
    wall2c = 10
    wall2d = 300
    wall3a = 0
    wall3b = 290
    wall3c = 400
    wall3d = 10
    wall4a = 390
    wall4b = 0
    wall4c = 10
    wall4d = 300
    pygame.draw.rect(sur_obj, (0,0,0), (wall1a,wall1b,wall1c,wall1d))
    pygame.draw.rect(sur_obj, (0,0,0), (wall2a,wall2b,wall2c,wall2d))
    pygame.draw.rect(sur_obj, (0,0,0), (wall3a,wall3b,wall3c,wall3d))
    pygame.draw.rect(sur_obj, (0,0,0), (wall4a,wall4b,wall4c,wall4d))


    #make the rectangle stop at the walls
    if p1<0:
        p1=0
    if p1>340:
        p1=340
    if p2<0:
        p2=0
    if p2>240:
        p2=240
    #destroy circle if it collides with the walls
    if wall1a+wall1c>x>wall1a and wall1b+wall1d>y>wall1b:
        e = True
        #score -= 1
    if wall2a+wall2c>x>wall2a and wall2b+wall2d>y>wall2b:
        e = True
        #score -= 1
    if wall3a+wall3c>x>wall3a and wall3b+wall3d>y>wall3b:
        e = True
        #score -= 1
    if wall4a+wall4c>x>wall4a and wall4b+wall4d>y>wall4b:
        e = True
        #score -= 1

    #draw 4 red circles in random positions but not in the same position as the rectangle and call the function draw_circle2()
    #def draw_circle2():
     #   global x2
      #  global y2
       # if(e == True):
        # x2=random.randint(0,400)
         #y2=random.randint(0,300)
         #pygame.draw.circle(sur_obj, (255,0,0), (x2,y2), 5)



        #pygame.draw.circle(sur_obj, (255,0,0), (x2,y2), 5)
    if score%3==0 and e==True:
     speed += 0.2
    #draw_circle2()
    draw_circle()
    draw_circle2()
    #if r is pressed, the game ends
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                e = True
                score = 0
    #if enter is pressed, the game ends

    key_input2 = pygame.key.get_pressed()
    if key_input2[pygame.K_RETURN]:
        e = True

    if key_input2[pygame.K_r]:
        death()
    #if the rectangle collides with the red circles, the game ends
    #if p1+50>x2 and p1<x2+5 and p2+50>y2 and p2<y2+5:
        #make game end
        #e = True
        #play sound gameover.wav
        #pygame.mixer.music.load("gameover.wav")
        #pygame.mixer.music.play()
        #display game over
       # font=pygame.font.SysFont(None,100)
       # text=font.render("Game Over",True,(0,0,0))
       # sur_obj.blit(text,(100,100))
       # score = 0
    

         
    
    


    #display the speed
    font=pygame.font.SysFont(None,25)
    text=font.render("Speed: "+str(int(speed*10)/10),True,(125,125,125))
    sur_obj.blit(text,(15,45))
    #print(a)
    
    pygame.display.update()
    fpsclock.tick(fps)
    pygame.display.update()
