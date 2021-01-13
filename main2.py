import pygame
import random
import math
from pygame import mixer
# initialize the game
pygame.init()
viteX = 0.2
# create screen and background image
xcord = 500
ycord = 600
screen = pygame.display.set_mode((xcord,ycord))
background = pygame.image.load('33932.jpg')

# title and icon
pygame.display.set_caption("Fighter Jet")
icon = pygame.image.load('plane.png')
pygame.display.set_icon(icon)
def settings():
    global viteX
    easy = pygame.font.Font('freesansbold.ttf',27)
    medium = pygame.font.Font('freesansbold.ttf',27)
    hard = pygame.font.Font('freesansbold.ttf',27)
    difficulty = pygame.font.Font('freesansbold.ttf',32)
    dX= 60
    dY = 50
    cond = True
    while cond:
        mx, my = pygame.mouse.get_pos()
        screen.fill((255, 0, 43))
        # Pygame event forloop
        circ1 = pygame.draw.circle(screen,(0,0,0),(100,270),40)
        circ2 = pygame.draw.circle(screen,(0,0,0),(250,270),40)
        circ3 = pygame.draw.circle(screen,(0,0,0),(400,270),40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cond = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and circ1.collidepoint(mx,my):
                    viteX = 0.2
                if event.button == 1 and circ2.collidepoint(mx,my):
                    viteX = 0.4
                if event.button == 1 and circ3.collidepoint(mx,my):
                    viteX = 0.8
            if viteX == 0.2:
                circ1 = pygame.draw.circle(screen,(255,255,255),(100,270),50)
        #rectangle from menu 
        easy_blit = easy.render('easy',True,(255,255,255))
        medium_blit = medium.render('Medium ',True,(255,255,255))
        hard_blit = hard.render('Hard',True,(255,255,255))
        screen.blit(easy_blit, (100,260))
        screen.blit(medium_blit, (250,260))
        screen.blit(hard_blit, (400,260))

    #text render  
        difficulty_blit = difficulty.render('choose level of difficulty',True,(255,255,255))
        screen.blit(difficulty_blit, (dX,dY))
        pygame.display.update()

def main_menu():
    #text declaration
    Menu_text = pygame.font.Font('freesansbold.ttf',32)
    aliens = pygame.font.Font('freesansbold.ttf',21)
    play_text = pygame.font.Font('freesansbold.ttf',23)
    settings_text = pygame.font.Font('freesansbold.ttf',23)
    #text coordinates
    stingsX = 185
    stingsY = 345
    playX = 210
    playY = 245
    aliensX = 15
    aliensY = 150
    welcomeX = 160
    welcomeY = 100

    #loop for main menu
    run = True
    while run:
        mx, my = pygame.mouse.get_pos()
        screen.fill((255, 0, 43))
        # Pygame event forloop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and circle1.collidepoint(mx,my):
                    play()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and circle2.collidepoint(mx,my):
                    settings()

        #rectangle from menu 
        circle1 = pygame.Rect(180,225,130,60)
        circle2 = pygame.Rect(180,325,130,60)
        pygame.draw.rect(screen,(0,0,0),circle1)
        pygame.draw.rect(screen,(0,0,0),circle2) 
        #text render  
        welcome_blit = Menu_text.render('Main Menu ',True,(255,255,255))
        aliens_blit = aliens.render(' ',True,(255,255,255))
        play_blit = play_text.render('PLAY',True,(255,255,255))
        stings_blit = settings_text.render('SETTINGS',True,(255,255,255))
        screen.blit(play_blit, (playX,playY))
        screen.blit(aliens_blit, (aliensX,aliensY))
        screen.blit(welcome_blit, (welcomeX,welcomeY))
        screen.blit(stings_blit, (stingsX,stingsY))
        pygame.display.update()
        
        

def play():
    global viteX
    background = pygame.image.load('33932.jpg')
    # jet image + parametres
    playerImg = pygame.image.load('jet.png')
    playerX = 220
    playerY = 400
    playerX_change = 0.
    # ennemy image + parametres
    enemyImg = pygame.image.load('ufo.png')
    enemyX = random.randint(0,436)
    enemyY = random.randint(50,100)
    enemyX_change = viteX
    enemyY_change = 40
    num_ennemies = 6
    '''
    for i in range(num_ennemies):
        enemyImg.append(pygame.image.load('ufo.png'))
        enemyX.append(random.randint(0,436))
        enemyY.append(random.randint(50,100))
        enemyX_change.append(0.3)
        enemyY_change.append(40)'
    '''

    # bullet image + parametres
    BulletImg = pygame.image.load('bomb.png')
    BulletX = 0
    BulletY = 400
    BulletX_change = 0
    BulletY_change = 0.3
    bullet_State = 'ready' #ready : you can't see the bullet on the screen // Fire : the bullet is actually moving
    #score
    score = 0
    font = pygame.font.Font('freesansbold.ttf',32)
    fontX = 10
    fontY = 10
    #background sound
    mixer.music.load('hypemusic.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)
    #gameover text
    gameover = pygame.font.Font('freesansbold.ttf',64)

    # screnn.blit makes sure the jet, bullet and ufo show up
    def player(x, y):
        screen.blit(playerImg, (x, y))

    def enemy(x, y):
        screen.blit(enemyImg, (x, y))

    def bullet(x,y):
        screen.blit(BulletImg, (x+16,y+10))

    def collision(enemyX, enemyY, BulletX, BulletY):
        distance = math.sqrt((math.pow((enemyX - BulletX),2)) + (math.pow((enemyY-BulletY),2)))
        if distance < 27:
            return True
        else:
            return False
    def showscore(x,y):
        score_blit = font.render('score: '+str(score),True,(255,255,255))
        screen.blit(score_blit, (x,y))
    def game_over_text():
        over_blit = gameover.render('GAME OVER',True,(255,255,255))
        screen.blit(over_blit, (50,250))
    # game loop (makes sure the game stops once we quit)
    running = True
    while running:
        screen.fill((255, 0, 0))
        screen.blit(background, (0,0))
        # Pygame event forloop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # Player_movements
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -0.3
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0.3
                if event.key == pygame.K_SPACE:
                    if bullet_State is 'ready':
                        bullet_State = 'fire'
                        missile = mixer.Sound('Missile+2.wav')
                        missile.play()
                        BulletX = playerX
                        bullet(BulletX,BulletY)
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.pause()
                    pygame.mixer.music.pause()
                    main_menu()            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
            

        # check_boundary for jet 
        if playerX < 0:
            playerX = 0
            playerX_change = 0
        elif playerX > (xcord-64):
            playerX = xcord-64
            playerX_change = 0
        playerX += playerX_change
        # check_boundary for UFO
            #gameover
        if enemyY > 370:
            enemyY = 2000
            game_over_text()
            #rectangle1 = pygame.Rect(300,10,30,30)
            #pygame.draw.rect(screen,(255, 255, 0),rectangle1)
        enemyX += enemyX_change 
        if enemyX  < 0:
            enemyX  = 0
            enemyX_change  = viteX
            enemyY  += enemyY_change 
        elif enemyX  > (xcord-64):
            enemyX  = xcord-64
            enemyX_change  = -viteX
            enemyY  += enemyY_change 
        #collision parametres
        check_col = collision(enemyX,enemyY,BulletX,BulletY)
        if check_col:
            collision_sound = mixer.Sound('Explosion+3.wav')
            collision_sound.play()
            BulletY = 400
            bullet_State = 'ready'  
            score += 1
            enemyX = random.randint(0,436)
            enemyY = random.randint(50,100)
        #bullet parametres
        if bullet_State is 'fire':
            bullet(BulletX,BulletY) 
            BulletY -= BulletY_change
        if BulletY < 0:
            BulletY = 400
            bullet_State = 'ready'

        player(playerX, playerY)
        showscore(fontX,fontY)
        enemy(enemyX, enemyY)
        pygame.display.update()
main_menu()