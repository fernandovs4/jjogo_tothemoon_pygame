import pygame
from classes import*
import variaveis
from constantes import*


def inicializa():
    '''Função que inicializa todos os assets e states do jogo'''
    pygame.init()
    pygame.mixer.music.load('som/musica_de_fundo.mp3')
    pygame.mixer.music.play(-1)
    window = pygame.display.set_mode((400, 600), vsync=True, flags=pygame.SCALED)
    pygame.key.set_repeat(50)
    font1 = pygame.font.Font(None, 10)
    font2 = pygame.font.Font(None, 20)
    font3 = pygame.font.Font(None,40)

    '''Parte abaixo utilizado para criar todos os objetos do jogo e os grupos de sprites'''
    all_trampolin1 = pygame.sprite.Group()
    all_Trampoline3 = pygame.sprite.Group()
    all_Trampoline2 = pygame.sprite.Group()
    trampolin3 = Trampoline3()
    all_Trampoline3.add(trampolin3)
    trampolin2 = Trampoline2()
    all_Trampoline2.add(trampolin2)
    trampolin1 = Trampoline1()
    all_trampolin1.add(trampolin1)
    all_character1 = pygame.sprite.Group()
    all_character2 = pygame.sprite.Group()
    all_character3 = pygame.sprite.Group()
    character1 = Character1()
    character2 = Character2()
    character3 = Character3()
    all_character1.add(character1)
    all_character2.add(character2)
    all_character3.add(character3)
    all_bird = pygame.sprite.Group()
    bird = Bird()
    all_bird.add(bird)
    all_screen_initial = pygame.sprite.Group()
    screen_initial = Screen_initial()
    all_screen_final = pygame.sprite.Group()
    screen_final = Screen_final()
    all_screen_final.add(screen_final)
    all_screen_initial.add(screen_initial)
    all_surprise = pygame.sprite.Group()
    for i in range(3):
        surprise = Surprise()
        all_surprise.add(surprise)
    all_coins1 = pygame.sprite.Group()
    for i in range(30):
        coin1 = Coin1()
        all_coins1.add(coin1)
    all_coins2 = pygame.sprite.Group()
    for i in range(30):
        coin2 = Coin2()
        all_coins2.add(coin2)
    all_coins3 = pygame.sprite.Group()
    for i in range(200):
        coin3 = Coin3()
        all_coins3.add(coin3)
    all_cloud = pygame.sprite.Group()
    cloud1 = Cloud()
    cloud2 = Cloud()
    cloud3 = Cloud()
    all_cloud.add(cloud1)
    all_cloud.add(cloud2)
    all_cloud.add(cloud3)
    all_help_screen = pygame.sprite.Group()
    help_screen = Help()
    all_help_screen.add(help_screen)
    

    text = font3.render('Game Over', True, RED)
    screen_help_rect = pygame.Rect(361, 7, 63, 31)
    principal_menu_rect = pygame.Rect(74, 396, 252, 59)
    play_again_rect = pygame.Rect(74, 321, 252, 59)
    exit_rect = pygame.Rect(74, 471, 252, 59)
    medium_phase_rect = pygame.Rect(74, 396, 252, 59)
    easy_phase_rect = pygame.Rect(74, 321, 252, 59)
    hard_phase_rect = pygame.Rect(74, 471, 252, 59)
    text_rect = text.get_rect(center = (20,20))
  
   
    easy_phase = font3.render('Fácil', True, color[0])
    medium_phase = font3.render('Médio', True, PURPLE)
    hard_phase = font3.render('Prova Pygame', True, PURPLE)
    score_text = font2.render(f'{variaveis.score}', True, PURPLE)



    assets = {

         'walk': pygame.mixer.Sound('som/pulo.wav'),
         'coin_sound': pygame.mixer.Sound('som/coin_sound.ogg'),
         'bird_sound': pygame.mixer.Sound('som/bird_sound.flac'),
         'selecting_sound': pygame.mixer.Sound('som/selecting_sound.ogg')

    }

    state = {
      'trampolin1': trampolin1, 'all_trampolin1': all_trampolin1, 'trampolin2': trampolin2, 'all_trampolin2': all_Trampoline2,'trampolin3': trampolin3, 'all_trampolin3': all_Trampoline3,
      'all_character1': all_character1, 'character1': character1, 'character2': character2, 'character3': character3, 'all_character2': all_character2, 'all_character3': all_character3, 'all_coins1': all_coins1,
      'cloud1': cloud1, 'cloud2': cloud2,'cloud3': cloud3,'all_cloud': all_cloud, 'screen_initial': screen_initial, 'all_screen': all_screen_initial,
      'easy_phase': easy_phase, 'medium_phase':  medium_phase, 'hard_phase': hard_phase,'easy_phase_rect': easy_phase_rect, 'medium_phase_rect':  medium_phase_rect, 'hard_phase_rect': hard_phase_rect,
      'coin1': coin1, 'coin2': coin2, 'coin3': coin3, 'all_coins2': all_coins2, 'all_coins3': all_coins3, 'all_screen_final': all_screen_final, 'screen_final': screen_final,
      'text': text,   'principal_menu_rect': principal_menu_rect, 'play_again_rect': play_again_rect, 'exit_rect': exit_rect, 'all_bird': all_bird, 'bird': bird, 'background': pygame.image.load('imagem\Background.png'),
      'score_text': score_text, 'font3' : font3, 'surprise': surprise, 'all_surprise': all_surprise, 'all_help_screen': all_help_screen, 'screen_help_rect': screen_help_rect, 
      'help_screen':help_screen
    }


    return window, assets, state




def finaliza():
    '''Função utilizada para fechar o pygame'''
    pygame.quit()


def desenha(window: pygame.Surface, assets, state):
    '''Função utilizada para desenhar todos os sprites na tela'''
    
    variaveis.incremetation_position += 1
    if variaveis.screen_easy == True:
        '''Desenha a tela de nível fácil'''
        window.blit(state['background'], (0,0))
        state['all_trampolin1'].draw(window)
        state['all_character1'].draw(window)
        state['all_coins1'].draw(window)
        state['all_cloud'].draw(window)
        state['all_bird'].draw(window)
        state['all_surprise'].draw(window)
        score_text = state['font3'].render(f'{variaveis.score}', True, PURPLE)
        window.blit(score_text, (360, 20))
    elif variaveis.screen_medium == True:
        '''Desenha a tela de nível médio'''
        window.blit(state['background'], (0,0))
        state['all_trampolin2'].draw(window)
        state['all_character2'].draw(window)
        state['all_coins2'].draw(window)
        state['all_cloud'].draw(window)
        state['all_bird'].draw(window)
        state['all_surprise'].draw(window)
        score_text = state['font3'].render(f'{variaveis.score}', True, PURPLE)
        window.blit(score_text, (360, 20))
    elif variaveis.screen_hard == True:
        '''Desenha a tela de nível difícil'''
        window.blit(state['background'], (0,0))
        state['all_trampolin3'].draw(window)
        state['all_character3'].draw(window)
        state['all_coins3'].draw(window)
        state['all_cloud'].draw(window)
        state['all_bird'].draw(window)
        state['all_surprise'].draw(window)
        score_text = state['font3'].render(f'{variaveis.score}', True, PURPLE)
        window.blit(score_text, (360, 20))
    elif variaveis.analyisng == 'screen_initial':
        '''Desenha a tela inicial do jogo'''
        pygame.draw.rect(window, RED, state['play_again_rect'])
        pygame.draw.rect(window,RED,state['exit_rect'])
        pygame.draw.rect(window,RED,state['principal_menu_rect'])
        state['all_screen'].draw(window)
        show_record_text = state['font3'].render(variaveis.show_record,True, PURPLE)
        state['all_help_screen'].draw(window)
        if variaveis.help == False:
            window.blit(show_record_text,(266,236))
    elif variaveis.analyisng == 'screen_final':
        '''Desenha a tela final do jogo'''
        pygame.draw.rect(window, RED, state['play_again_rect'])
        pygame.draw.rect(window,RED,state['exit_rect'])
        pygame.draw.rect(window,RED,state['principal_menu_rect'])
        state['all_screen_final'].draw(window)
        print(variaveis.str_score_antigo)
        score_antigo_text = state['font3'].render(variaveis.str_score_antigo, True, PURPLE)
        window.blit(score_antigo_text,(266,236))
        print(pygame.mouse.get_pos())
    pygame.display.update()



def atualiza_estado(state):
    '''Função utilizada para atualizar os estados do jogo'''
    global GRAVITY1
    variaveis.incremetation_position += 0.5
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            '''caso o jogador tenha pressionado o botão do mouse'''

            if variaveis.analyisng == 'screen_initial':
                if state['easy_phase_rect'].collidepoint(ev.pos):

                    assets['selecting_sound'].play()
                    state['trampolin1'].rect.centerx = 200
                    variaveis.die = 0
                    variaveis.screen_easy = True
                    variaveis.analyisng = '0'
                    variaveis.screen_medium = False
                    variaveis.screen_hard = False
                    variaveis.phase = 1
                elif state['medium_phase_rect'].collidepoint(ev.pos):
                    assets['selecting_sound'].play()
                    variaveis.phase = 2
                    variaveis.die = 0
                    variaveis.screen_medium = True
                    variaveis.analyisng = '0'
                    variaveis.screen_easy = False
                    variaveis.screen_hard = False
                elif state['hard_phase_rect'].collidepoint(ev.pos):
                    assets['selecting_sound'].play()
                    variaveis.die = 0
                    variaveis.screen_hard = True
                    variaveis.analyisng = '0'
                    variaveis.screen_medium = False
                    variaveis.screen_easy = False
                    variaveis.phase = 3
            if variaveis.analyisng == 'screen_final':
                state['trampolin1'].rect.centerx = 200
                state['trampolin1'].direction = 1
                state['trampolin2'].rect.centerx = 200
                state['trampolin2'].direction = 1
                state['trampolin3'].rect.centerx = 200
                state['trampolin3'].direction = 1
                if state['principal_menu_rect'].collidepoint(ev.pos):
                    assets['selecting_sound'].play()
                    if len(state['all_surprise']) == 2:
                        surprise = Surprise()
                        state['all_surprise'].add(surprise)
                    if len(state['all_surprise']) == 1:
                        for i in range(2):
                            surprise = Surprise()
                            state['all_surprise'].add(surprise)
                    if len(state['all_surprise']) == 0:
                        for i in range(3):
                            surprise = Surprise()
                            state['all_surprise'].add(surprise)
                    state['trampolin1'].speedx = 1
                    state['trampolin2'].speedx = 1
                    state['trampolin3'].speedx = 1
                    
                    variaveis.analyisng = 'screen_initial'
                    variaveis.screen_easy = False
                    variaveis.screen_hard = False
                    variaveis.screen_medium = False
                if state['play_again_rect'].collidepoint(ev.pos):
                    assets['selecting_sound'].play()
                    variaveis.die = 0
                    variaveis.analyisng = '0'
                    if len(state['all_surprise']) == 2:
                        surprise = Surprise()
                        state['all_surprise'].add(surprise)
                    if len(state['all_surprise']) == 1:
                        for i in range(2):
                            surprise = Surprise()
                            state['all_surprise'].add(surprise)
                    if len(state['all_surprise']) == 0:
                        for i in range(3):
                            surprise = Surprise()
                            state['all_surprise'].add(surprise)
                    state['trampolin1'].speedx = 1
                    state['trampolin2'].speedx = 1
                    state['trampolin3'].speedx = 1
                    if variaveis.phase == 1:
                        variaveis.screen_easy = True
                    elif variaveis.phase == 2:
                        variaveis.screen_medium = True
                    elif variaveis.phase == 3:
                        variaveis.screen_hard = True
                if state['exit_rect'].collidepoint(ev.pos):
                    assets['selecting_sound'].play()
                    return False
    mouse_position = pygame.mouse.get_pos()
    if state['screen_help_rect'].collidepoint(mouse_position):
        '''Caso o jogador passe o mouse no ícone de interrogação, aparecerá uma nova tela explicando o funcionamento do jogo'''
        state['help_screen'].image = pygame.image.load('imagem/tela_inicial_int.png')
        variaveis.help = True
    else:
        state['help_screen'].image = pygame.image.load('imagem/tela_inicial.png')
        variaveis.help = False
    
    if variaveis.screen_easy == True and variaveis.die == 0:
        '''Parte utilizada para verificar se o personagem colidiu com algum objeto do nível fácil'''
        if pygame.sprite.spritecollide(state['character1'],state['all_trampolin1'],False ):
             assets['walk'].play()
             variaveis.collide = True
        if pygame.sprite.spritecollide(state['character1'],state['all_coins1'],True ):
            assets['coin_sound'].play()
            coin1 = Coin1()
            state['all_coins1'].add(coin1)
            variaveis.kill = True
        if pygame.sprite.spritecollide(state['character1'],state['all_surprise'],True ):
            state['trampolin1'].speedx += 3   
        state['trampolin1'].update()
        state['character1'].update()
        state['coin1'].update()
        state['cloud1'].update()
        state['cloud2'].update()
        state['cloud3'].update()
        state['bird'].update()
        
       
    if variaveis.screen_medium == True and variaveis.die == 0:
        '''Parte utilizada para verificar se o personagem colidiu com algum objeto do nível médio'''
        if pygame.sprite.spritecollide(state['character2'],state['all_trampolin2'],False ):
             variaveis.collide = True
             assets['walk'].play()
        if pygame.sprite.spritecollide(state['character2'],state['all_coins2'],True ):
            assets['coin_sound'].play()
            coin2 = Coin2()
            state['all_coins2'].add(coin2)
            variaveis.kill = True
        if pygame.sprite.spritecollide(state['character2'],state['all_surprise'],True ):
            state['trampolin2'].speedx += 3
        state['trampolin2'].update()
        state['character2'].update()
        state['coin2'].update()
        state['cloud1'].update()
        state['cloud2'].update()
        state['cloud3'].update()
        state['bird'].update()
    if variaveis.screen_hard == True and variaveis.die == 0:
        '''Parte utilizada para verificar se o personagem colidiu com algum objeto do nível difícil'''
        if pygame.sprite.spritecollide(state['character3'],state['all_trampolin3'],False ):
             assets['walk'].play()
             variaveis.collide = True
        if pygame.sprite.spritecollide(state['character3'],state['all_coins3'],True ):
            assets['coin_sound'].play()
            variaveis.kill = True
            coin3 = Coin3()
            state['all_coins3'].add(coin3)
        if pygame.sprite.spritecollide(state['character3'],state['all_surprise'],True ):
            state['trampolin3'].speedx += 3
        state['trampolin3'].update()
        state['character3'].update()
        state['coin3'].update()
        state['cloud1'].update()
        state['cloud2'].update()
        state['cloud3'].update()
        state['bird'].update()
    state['screen_initial'].update()

    with open('record.json', 'r') as arquivo_json:
        records = arquivo_json.read()
    dict_record = json.loads(records)
    variaveis.show_record = str(dict_record['record'])

    return True



def gameloop(window, assets, state):
    while atualiza_estado(state):
        desenha(window, assets, state)

if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()
