import pygame
from sys import exit

pygame.init()

background_menu = pygame.image.load('Images/Poongle_bg.png')

# Efeito de click
mouse_select = pygame.mixer.Sound('Sounds/mouse_select.wav')

# Crédito
def credito(surface):
    credit_font = pygame.font.SysFont('cambria', 15)
    credit = credit_font.render('by: DeNevski', True, white)
    surface.blit(credit, (510, 380))

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 140, 0)

# Música de fundo
def background_music():
    background_music = pygame.mixer.music.load('Sounds/backgroung_music.mp3')
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)
background_music()

# Tela
x = 600
y = 400

class Menu:

    def __init__(self):
        self._surface_menu = pygame.display.set_mode((x, y))
        self._icon_title()

    def _icon_title(self):
        pygame.display.set_caption('Poongle')
        icon = pygame.image.load('Images/Poongle_icon.png')
        icon = pygame.transform.smoothscale(icon, (32, 32))
        pygame.display.set_icon(icon)

    def main_menu(self):
        while True:

            mouse_pos = pygame.mouse.get_pos()

            self._surface_menu.blit(background_menu, (205, -20))

            # Define o retângulo do botão "PLAY"
            play_rect = pygame.draw.rect(self._surface_menu, black, (255, 184, 72, 26))
            # Cria a botão "PLAY"
            play_font = pygame.font.SysFont('unispacebold', 30)
            play_button = play_font.render('PLAY', True, white)
            # Muda a cor do botão "PLAY" ao passar o mouse em cima
            if 255 <= mouse_pos[0] <= 327 and 184 <= mouse_pos[1] <= 210:
               play_button = play_font.render('PLAY', True, orange)
            # Mostra o botão na tela
            self._surface_menu.blit(play_button, (255, 180))
            
            # Define o retângulo do botão "OPTIONS"
            options_rect = pygame.draw.rect(self._surface_menu, black, (254, 244, 125, 26))
            # Cria a botão "OPTIONS"
            options_font = pygame.font.SysFont('unispacebold', 30)
            options_button = options_font.render('OPTIONS', True, white)
            # Muda a cor do botão "OPTIONS" ao passar o mouse em cima
            if 254 <= mouse_pos[0] <= 379 and 244 <= mouse_pos[1] <= 270:
                options_button = options_font.render('OPTIONS', True, orange)
            # Mostra o botão na tela
            self._surface_menu.blit(options_button, (254, 240))

            # Define o retângulo do botão "EXIT"
            exit_rect = pygame.draw.rect(self._surface_menu, black, (253, 304, 71, 26))
            # Cria a botão "EXIT"
            exit_font = pygame.font.SysFont('unispacebold', 30)
            exit_button = exit_font.render('EXIT', True, white)
            # Muda a cor do botão "EXIT" ao passar o mouse em cima
            if 253 <= mouse_pos[0] <= 326 and 304 <= mouse_pos[1] <= 330:
               exit_button = exit_font.render('EXIT', True, orange)
            # Mostra o botão na tela
            self._surface_menu.blit(exit_button, (253, 300))

            credito(self._surface_menu)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit
                    exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if 255 <= mouse_pos[0] <= 327 and 184 <= mouse_pos[1] <= 210:
                        mouse_select.play()
                        self._run_play()
                    
                    elif 254 <= mouse_pos[0] <= 379 and 244 <= mouse_pos[1] <= 270:
                        mouse_select.play()
                        self._run_options()

                    elif 253 <= mouse_pos[0] <= 326 and 304 <= mouse_pos[1] <= 330:
                        pygame.quit()
                        exit()
        
            pygame.display.flip()

    # Chama a classe Options e abre sua tela
    def _run_options(self):
        from GUI.options import Options
        options = Options()
        options.options_menu()

    # Chama a classe Play e abre sua tela
    def _run_play(self):
        from GUI.play import Play
        play = Play()
        play.game_mode()
