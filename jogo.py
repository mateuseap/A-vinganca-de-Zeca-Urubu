import random
import pygame, sys # lib
clock = pygame.time.Clock() 
from pygame.locals import * 
pygame.init() 

pygame.display.set_caption('A vingança de Zeca Urubu') #o nome da janela

WINDOW_SIZE = (1000,600) #variavel pra guardar o tamanho da minha janela
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) #janela

player_walkR = [pygame.image.load('Imagens/zequinha1d.png'), pygame.image.load('Imagens/zequinha2d.png'), pygame.image.load('Imagens/zequinha3d.png'), pygame.image.load('Imagens/zequinha4d.png'), pygame.image.load('Imagens/zequinha5d.png'), pygame.image.load('Imagens/zequinha6d.png'), pygame.image.load('Imagens/zequinha7d.png'), pygame.image.load('Imagens/zequinha8d.png'), pygame.image.load('Imagens/zequinha9d.png'), pygame.image.load('Imagens/zequinha10d.png'), pygame.image.load('Imagens/zequinha11d.png'), pygame.image.load('Imagens/zequinha12d.png'), pygame.image.load('Imagens/zequinha13d.png'), pygame.image.load('Imagens/zequinha14d.png'), pygame.image.load('Imagens/zequinha15d.png')] #carrega a imagem do meu personagem
player_walkL = [pygame.image.load('Imagens/zequinha1e.png'), pygame.image.load('Imagens/zequinha2e.png'), pygame.image.load('Imagens/zequinha3e.png'), pygame.image.load('Imagens/zequinha4e.png'), pygame.image.load('Imagens/zequinha5e.png'), pygame.image.load('Imagens/zequinha6e.png'), pygame.image.load('Imagens/zequinha7e.png'), pygame.image.load('Imagens/zequinha8e.png'), pygame.image.load('Imagens/zequinha9e.png'), pygame.image.load('Imagens/zequinha10e.png'), pygame.image.load('Imagens/zequinha11e.png'), pygame.image.load('Imagens/zequinha12e.png'), pygame.image.load('Imagens/zequinha13e.png'), pygame.image.load('Imagens/zequinha14e.png'), pygame.image.load('Imagens/zequinha15e.png')]
player_jump = [pygame.image.load('Imagens/zequinhajumpd.png'), pygame.image.load('Imagens/zequinhajumpe.png')]
obstaculo_sprite = pygame.image.load('Imagens/obstaculo.png')
bg = pygame.image.load('Imagens/background.png')

last = "right"

moving_right = False
moving_left = False
vertical_momentum = 0
air_timer = 0
walkCount = 0

player_location = [10,536]
player_y_momentum = 1

player_rect = pygame.Rect(player_location[0],player_location[1],player_walkL[0].get_width(),player_walkL[0].get_height())#isso aqui eh pra tratar colisao

#variaveis pra meu obstaculo
array_rect = [0, 590]
obstaculo_X=900
obstaculo_Y=510
speed=-5
#rectX = 900
#rectY = 300

def redrawGameWindow():
    global walkCount

    if walkCount+1 >= 75:
        walkCount = 0

    if (moving_left) and (pulo == False):
        screen.blit(player_walkL[walkCount//5], (player_location[0], player_location[1]))
        walkCount += 1
    elif (moving_right) and (pulo == False):
        screen.blit(player_walkR[walkCount//5], (player_location[0], player_location[1]))
        walkCount += 1
    elif pulo:
        if last == "right":
            screen.blit(player_jump[0], (player_location[0], player_location[1]))
        if last == "left":
            screen.blit(player_jump[1], (player_location[0], player_location[1]))
    else:
        if last == "right":
            screen.blit(player_walkR[0], (player_location[0], player_location[1]))
        if last == "left":
            screen.blit(player_walkL[0], (player_location[0], player_location[1]))
    
    pygame.display.update()

#novo evento pra aumentar a velocidade
increase_speed = pygame.USEREVENT + 1
pygame.time.set_timer(increase_speed,1000)


while True: # famoso loop infinito
    clock.tick(60) # fpszada
    screen.blit(bg, (0,0))
    screen.blit(obstaculo_sprite, (obstaculo_X, obstaculo_Y))
   
    #printando meu obstaculo
    test_rect2 = pygame.Rect(array_rect[0], array_rect[1], 1000, 10)
    obstaculo = pygame.Rect(obstaculo_X, obstaculo_Y, obstaculo_sprite.get_width(), obstaculo_sprite.get_height())

    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4
    player_location[1] += vertical_momentum
    vertical_momentum += 0.3
    if vertical_momentum > 5:
        vertical_momentum = 4
    
    player_rect.x = player_location[0] # atualizando as "fronteiras" do personagem
    player_rect.y = player_location[1] # atualizando as "fronteiras" do personagem
    
    #atualiza a posição do obstaculo
    obstaculo.move_ip(speed, 0)
    obstaculo_X+=speed
    if (obstaculo_X<-60):
        obstaculo_X=1060

	#colisão com o chão
    if player_rect.colliderect(test_rect2):
        player_location[1] = array_rect[1]-player_walkL[0].get_height()
        pulo = False

    #colisão com o livro    
    if player_rect.colliderect(obstaculo):
        player_location[1] = obstaculo_Y-player_walkL[0].get_height()
        pulo = False

    for event in pygame.event.get(): #isso aqui fica esperando os eventos
        #eventozinho pra aumentar a velocidade
        if event.type == increase_speed:
            speed -= 1

        if event.type == QUIT: # se a pessoa saiu
            pygame.quit() 
            sys.exit()
        
        #qnd clica nas setinhas
        if event.type == KEYDOWN: 
            if (event.key == K_RIGHT) or (event.key == K_d):
                moving_right = True
                last = "right"
            elif (event.key == K_LEFT) or (event.key == K_a):
                moving_left = True
                last = "left"
            elif ((event.key == K_UP) or (event.key == K_w)) and (pulo == False):
                pulo = True
                if air_timer < 6:
                    vertical_momentum = -8
            else:
                moving_left = False
                moving_right = False
                walkCount = 0
        if event.type == KEYUP:
            if (event.key == K_RIGHT) or (event.key == K_d):
                moving_right = False
            elif (event.key == K_LEFT) or (event.key == K_a):
                moving_left = False
            else:
                moving_left = False
                moving_right = False
                walkCount = 0

    redrawGameWindow()