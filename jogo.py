import pygame, sys # lib
clock = pygame.time.Clock() 
from pygame.locals import * 
pygame.init() 

pygame.display.set_caption('A vingança de Zeca Urubu') #o nome da janela

WINDOW_SIZE = (1000,600) #variavel pra guardar o tamanho da minha janela
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) #janela

player_image = pygame.image.load('Imagens/zequinha1d.png') #carrega a imagem do meu personagem
player_image2 = pygame.image.load('Imagens/zequinha1e.png')

array_imagem = [1,0]

moving_right = False
moving_left = False
vertical_momentum = 0
air_timer = 0

player_location = [0,519]
player_y_momentum = 1

player_rect = pygame.Rect(player_location[0],player_location[1],player_image.get_width(),player_image.get_height())#isso aqui eh pra tratar colisao
test_rect = pygame.Rect(100,100,100,50)#um retangulo pra testar colisao
#variaveis pra meu obstaculo
array_rect = [0, 590]
#rectX = 900
#rectY = 300

while True: # famoso loop infinito
    screen.fill((146,244,255)) # pinta a tela de azul

    #printando meu obstaculo
    test_rect2 = pygame.Rect(array_rect[0], array_rect[1], 1000, 10)

    if array_imagem[0]:
        screen.blit(player_image,player_location) # printa o personagem
    if array_imagem[1]:
        screen.blit(player_image2,player_location) 
	# movimento, qnd aperto as setinhas
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
    #printando meu rect
    pygame.draw.rect(screen,(0,0,0),test_rect2)
	# testando se meu jogador colidiu com o retangulo
    if player_rect.colliderect(test_rect2):
        #se sim, so mudo a cor mesmo
        pygame.draw.rect(screen,(255,0,0),test_rect2)
        player_location[1] = array_rect[1]-player_image.get_height()
        pulo = False
        #player_location[0] -= 5
    else:
        pygame.draw.rect(screen,(0,0,0),test_rect2)

    for event in pygame.event.get(): #isso aqui fica esperando os eventos
        if event.type == QUIT: # se a pessoa saiu
            pygame.quit() 
            sys.exit()
        #qnd clica nas setinhas
        if event.type == KEYDOWN: 
            if (event.key == K_RIGHT) or (event.key == K_d):
                moving_right = True
                array_imagem[1] = 0
                array_imagem[0] = 1
            if (event.key == K_LEFT) or (event.key == K_a):
                moving_left = True
                array_imagem[1] = 1
                array_imagem[0] = 0
            if ((event.key == K_UP) or (event.key == K_w))and (pulo == False):
                if air_timer < 6:
                    vertical_momentum = -8
                pulo = True
        if event.type == KEYUP:
            if (event.key == K_RIGHT) or (event.key == K_d):
                moving_right = False
            if (event.key == K_LEFT) or (event.key == K_a):
                moving_left = False


    pygame.display.update() #atualiza
    clock.tick(60) # fpszada