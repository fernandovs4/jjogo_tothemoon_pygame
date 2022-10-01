import json
import pygame
import variaveis
import random
from constantes import*



class Surprise(pygame.sprite.Sprite):
    '''Classe usada para fazer os três objetos que alteram a velocidade da cama elástica quando eles são pegos'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('imagem/relampago.png'), [16,16])
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(20, 380)
        self.rect.centery = random.randrange(20, 300)
   



class Bird(pygame.sprite.Sprite):
        '''Classe para criar pássaros'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load("imagem/passaros.png"),[120,90])
            self.rect = self.image.get_rect()
            self.rect.centerx = random.randrange(500, 800)
            self.rect.centery = random.randrange(5,200)
        def update(self):
            '''Método para atualizar a posição dos pássaros e trocar as imagens dos pássaros para dar animação'''
            if variaveis.incremetation_position%7 == 0:
                self.image = pygame.transform.scale(pygame.image.load('imagem/passaros.png'),[120,90])
            else:
                self.image = pygame.transform.scale(pygame.image.load('imagem/passaros - 2.png'),[120,90])
            
            self.rect.centerx -= 1.5
            if self.rect.centerx < -100:
                    self.rect.centerx = random.randrange(700,1100)
                    self.rect.centery = random.randrange(5,250)


class Screen_final(pygame.sprite.Sprite):
    '''Classe para criar a tela final'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagem\TelaFinal.png')
        self.rect = self.image.get_rect()
    

class Screen_initial(pygame.sprite.Sprite):
    '''Classe para criar a tela inicial'''
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('imagem/tela_inicial.png')
            self.rect = self.image.get_rect()
    

class Help(pygame.sprite.Sprite):
    '''Classe para criar a tela de ajuda, onde fica explicado os níveis do jogo'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagem/tela_inicial.png')
        self.rect = self.image.get_rect()


class Cloud(pygame.sprite.Sprite):
        '''Classe para criar as nuvens'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load('imagem/nuvem1(B).png'), [100, 50])
            self.rect = self.image.get_rect(center = (15,15))
            self.rect.centerx = random.randrange(10, 375)
            self.rect.centery = random.randrange(10, 300)
        def update(self):
            '''Método utilizado para atualizar a posição das nuvens'''
            self.rect.centerx -= 1
            if self.rect.centerx <= -100:
                self.rect.centerx = random.randrange(500, 700)
                self.rect.centery = random.randrange(5, 300)


class Trampoline1(pygame.sprite.Sprite):
        '''Classe para criar a cama elástica da fase de nível fácil'''
        def __init__(self):
            global VELOCITY
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('imagem\Trampolin2.png')
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH/2
            self.rect.centery =     HEIGHT - 15
            self.speedx = 1
            self.b = 0.001
            self.direction = 1
        
        def update(self):
            '''Método utilizado para atualizar a posição da cama elástica '''
            if self.rect.right > 400:
                self.direction = -1 
            if self.rect.left < 0:
                self.direction = 1
            self.speedx = self.speedx + self.b
            self.rect.centerx += self.speedx*self.direction
            if variaveis.die == 1:
                self.rect.centerx = WIDTH/2

class Trampoline2(pygame.sprite.Sprite):
        '''Classe para criar a cama elástica do nível médio'''
        def __init__(self):
            global VELOCITY
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('imagem\Trampolin2.png')
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH/2
            self.rect.centery =     HEIGHT - 15
            self.speedx = 1
            self.b = 0.003
            self.direction = 1
        
        
        def update(self):
            '''Método utilizado para atualizar a posição da cama elástica '''
            if self.rect.right > 400:
                self.direction = -1 
            if self.rect.left < 0:
                self.direction = 1
            self.speedx = self.speedx + self.b
            self.rect.centerx += self.speedx*self.direction


class Trampoline3(pygame.sprite.Sprite):
        '''Classe para criar a cama elástica do nível difícil'''
        def __init__(self):
            global VELOCITY
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('imagem\Trampolin2.png')
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH/2
            self.rect.centery =     HEIGHT - 15
            self.speedx = 1
            self.b = 0.005
            self.direction = 1

        
        def update(self):
            '''Método utilizado para atualizar a posição da cama elástica '''
            if self.rect.right > 400:
                self.direction = -1 
            if self.rect.left < 0:
                self.direction = 1
            self.speedx = self.speedx + self.b
            self.rect.centerx += self.speedx*self.direction

class Character1(pygame.sprite.Sprite):
        '''Classe para criar o personagem da fase de nível fácil'''
        def __init__(self):
            global GRAVITY1
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load('imagem/Jump (1).png'), [40,40])
            '''sprite obtido no link: https://www.gameart2d.com/red-hat-boy-free-sprites.html'''
            self.rect = self.image.get_rect(center = (20,20))
            self.rect.centerx = 200
            self.rect.centery = 500
            self.direction = 1
            self.speedy = 0.1
            self.last_update = 0
            self.flip = False

        def update(self):
            '''Método utilizado para atualizar a posição do personagem do nível fácil, gerar a animação do personagem e salvar a pontuação do jogador, caso seja recorde '''
            global GRAVITY1
            global screen_easy, screen_medium, screen_hard, analyisng
            if variaveis.collide == True:
                self.speedy = -self.speedy
                variaveis.collide = False
            self.last_update = pygame.time.get_ticks()
            for i in range(12):
                if (self.last_update//300)%12  == i:
                    self.image = pygame.transform.scale(pygame.image.load(f'imagem/Jump ({i + 1}).png'), [40,40])
                    self.last_update = pygame.time.get_ticks()
            self.speedy += GRAVITY1
            if self.speedy >= 20.5:
                self.speedy = 20.5
            self.rect.centery += self.speedy
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.rect.centerx -= 3
            if key[pygame.K_RIGHT]:
                self.rect.centerx += 3
            if self.rect.centery > 600:
                with open('record.json', 'r') as arquivo_json:
                    records = arquivo_json.read()
                dict_record = json.loads(records)
                variaveis.record_final = dict_record['record']
                if variaveis.score >= variaveis.record_final:
                    variaveis.record_final = variaveis.score
                elif variaveis.score < variaveis.record_final:
                    variaveis.record_final = variaveis.record_final
                dict_record["record"] = variaveis.record_final
                novo_json = json.dumps(dict_record)
                with open('record.json', 'w') as arquivo_json:
                    arquivo_json.write(novo_json)
                print(variaveis.record_final)
                variaveis.screen_easy = False
                variaveis.screen_medium = False
                variaveis.screen_hard = False
                variaveis.analyisng = 'screen_final'
                variaveis.die = 1
                self.rect.centery=500
                self.rect.centerx = 200
                self.speedy = 0.1
                variaveis.score_antigo = variaveis.score
                variaveis.str_score_antigo = str(variaveis.score_antigo)
                variaveis.score = 0
                variaveis.str_score = '0'
                

class Character2(pygame.sprite.Sprite):
        '''Classe para criar o personagem da fase de nível médio'''
        def __init__(self):
            global GRAVITY2
            self.lista = []
            for i in range(12):
               self.lista.append(pygame.transform.scale(pygame.image.load(f'imagem/Jump ({i + 1}).png'), [40,40]))
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load('imagem/boneco_parado.png'), [40,40])
            '''sprite obtido no link: https://www.gameart2d.com/red-hat-boy-free-sprites.html'''
            self.rect = self.image.get_rect()
            self.rect.centerx = 200
            self.rect.centery = 500
            self.direction = 1
            self.speedy = 0.2

        def update(self):
            '''Método utilizado para atualizar a posição do personagem do nível médio, gerar a animação do personagem e salvar a pontuação do jogador, caso seja recorde '''
            global medium_phase_screen
            global GRAVITY2
            global score
            global str_score
            if variaveis.collide == True:
                self.speedy = -self.speedy
                variaveis.collide = False
            self.last_update = pygame.time.get_ticks()
            self.image = self.lista[(self.last_update//300)%12] 
            self.speedy += GRAVITY2
            if self.speedy >= 20.5:
                self.speedy = 20.5
            self.rect.centery += self.speedy
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.rect.centerx -= 5
            if key[pygame.K_RIGHT]:
                self.rect.centerx += 5
            if self.rect.centery > 600:
                with open('record.json', 'r') as arquivo_json:
                    records = arquivo_json.read()
                dict_record = json.loads(records)
                variaveis.record_final = dict_record['record']
                if variaveis.score >= variaveis.record_final:
                    variaveis.record_final = variaveis.score
                elif variaveis.score < variaveis.record_final:
                    variaveis.record_final = variaveis.record_final
                dict_record["record"] = variaveis.record_final
                novo_json = json.dumps(dict_record)
                with open('record.json', 'w') as arquivo_json:
                    arquivo_json.write(novo_json)
                variaveis.screen_easy = False
                variaveis.screen_medium = False
                variaveis.screen_hard = False
                variaveis.analyisng = 'screen_final'
                variaveis.die = 1
                self.rect.centery=500
                self.rect.centerx = 200
                self.speedy = 0.2
                variaveis.score_antigo = variaveis.score
                variaveis.str_score_antigo = str(variaveis.score_antigo)
                variaveis.score = 0
                variaveis.str_score = '0'

class Character3(pygame.sprite.Sprite):
        def __init__(self):
            '''Classe para criar o personagem da fase de nível difícil'''

            global GRAVITY3
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load('imagem/boneco_parado.png'), [40,40])
            '''sprite obtido no link: https://www.gameart2d.com/red-hat-boy-free-sprites.html'''
            self.rect = self.image.get_rect()
            self.rect.centerx = 200
            self.rect.centery = 400
            self.direction = 1
            self.speedy = 0.5

        def update(self):
            '''Método utilizado para atualizar a posição do personagem do nível difícil, gerar a animação do personagem e salvar a pontuação do jogador, caso seja recorde '''

            global GRAVITY3
            global score
            global str_score
            global hard_phase_screen
            if variaveis.collide == True:
                self.speedy = -self.speedy
                variaveis.collide = False
            self.last_update = pygame.time.get_ticks()
            for i in range(12):
                if (self.last_update//300)%12  == i:
                    self.image = pygame.transform.scale(pygame.image.load(f'imagem/Jump ({i + 1}).png'), [40,40])
                    self.last_update = pygame.time.get_ticks()
            self.speedy += GRAVITY3
            if self.speedy >= 20.5:
                self.speedy = 20.5
            self.rect.centery += self.speedy
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.rect.centerx -= 8
            if key[pygame.K_RIGHT]:
                self.rect.centerx += 8
            if self.rect.centery > 600:
                with open('record.json', 'r') as arquivo_json:
                    records = arquivo_json.read()
                dict_record = json.loads(records)
                variaveis.record_final = dict_record['record']
                if variaveis.score >= variaveis.record_final:
                    variaveis.record_final = variaveis.score
                elif variaveis.score < variaveis.record_final:
                    variaveis.record_final = variaveis.record_final
                dict_record["record"] = variaveis.record_final
                novo_json = json.dumps(dict_record)
                with open('record.json', 'w') as arquivo_json:
                    arquivo_json.write(novo_json)
                variaveis.screen_easy = False
                variaveis.screen_medium = False
                variaveis.screen_hard = False
                variaveis.analyisng = 'screen_final'
                self.rect.centery= 400
                self.rect.centerx = 200
                self.speedy = 0.5
                variaveis.die = 1
                variaveis.score_antigo = variaveis.score
                variaveis.str_score_antigo = str(variaveis.score_antigo)
                variaveis.score = 0
                variaveis.str_score = '0'

class Coin1(pygame.sprite.Sprite):
        def __init__(self):
            '''Classe utilizada para gerar as moedas da fase de nível fácil'''
            
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('imagem\moeda_to_the_moon.png')
            self.rect = self.image.get_rect()
            self.rect.centerx = random.randrange(400)
            self.rect.centery = random.randrange(100, 500)
        def update(self):
            if variaveis.kill:
                variaveis.score += 1
                variaveis.str_score = str(variaveis.score)
                self.kill()
                variaveis.kill = False

class Coin2(pygame.sprite.Sprite):
        '''Classe utilizada para gerar as moedas da fase de nível médio'''
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('imagem\moeda_to_the_moon.png')
            self.rect = self.image.get_rect()
            self.rect.centerx = random.randrange(400)
            self.rect.centery = random.randrange(100, 500)
        def update(self):
                '''Método utilizado para atualizar o valor da váriavel score e str_score'''
                if variaveis.kill:
                    variaveis.score += 1
                    variaveis.str_score = str(variaveis.score)
                    self.kill()
                    variaveis.kill = False
    

class Coin3(pygame.sprite.Sprite):
        '''Classe utilizada para gerar as moedas da fase de nível difícil'''
        def __init__(self):     
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('imagem\moeda_to_the_moon.png')
            self.rect = self.image.get_rect()
            self.rect.centerx = random.randrange(400)
            self.rect.centery = random.randrange(100, 500)
        def update(self):
                '''Método utilizado para atualizar o valor da váriavel score e str_score'''
                if variaveis.kill:
                    variaveis.score += 1
                    variaveis.str_score = str(variaveis.score)
                    self.kill()
                    variaveis.kill = False