import pygame
from sys import exit

pygame.init()

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
red = (255, 0, 0)
green = (0, 255, 0)

# Tela
x = 600
y = 400


class Options:
    
    def __init__(self):
        self._icon_title()
        self._options_surface = pygame.display.set_mode((x, y))

    def _icon_title(self):
        pygame.display.set_caption('Options')
        icon = pygame.image.load('Images/Poongle_icon.png')
        icon = pygame.transform.smoothscale(icon, (32, 32))
        pygame.display.set_icon(icon)
        
    def options_menu(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()

            # Volume da música
            # Retângulo do botão "MUSIC VOLUME"
            rect_music = pygame.draw.rect(self._options_surface, black, (190, 82, 163, 30))
            # Cria o botão "MUSIC VOLUME"
            music_font = pygame.font.SysFont('unispacebold', 30)
            music_button = music_font.render('MUSIC ON', True, green)
            # Muda a cor do botão "MUSIC VOLUME" ao pausar a música
            if not pygame.mixer.music.get_busy():
                music_button = music_font.render('MUSIC OFF', True, red)
            # Mostra o botão na tela
            self._options_surface.blit(music_button, (190, 80))
            
            # Controles
            # Retângulo do botão "CONTROLS"
            rect_controls = pygame.draw.rect(self._options_surface, black, (190, 162, 147, 30))
            # Cria o botão "CONTROLS"
            control_font = pygame.font.SysFont('unispacebold', 30)
            control_button = control_font.render('CONTROLS', True, white)
            # Muda a cor do botão "CONTROLS" ao passar o mouse por cima
            if 190 <= mouse_pos[0] <= 337 and 162 <= mouse_pos[1] <= 192:
                control_button = control_font.render('CONTROLS', True, orange)
            # Mostra o botão na tela
            self._options_surface.blit(control_button, (190, 160))

            # Voltar
            # Retângulo do botão "BACK"
            rect_back = pygame.draw.rect(self._options_surface, black, (190, 242, 75, 30))
            # Cria o botão "BACK"
            back_font = pygame.font.SysFont('unispacebold', 30)
            back_button = back_font.render('BACK', True, white)
            # Muda a cor do botão "BACK" ao passar o mouse por cima
            if 190 <= mouse_pos[0] <= 265 and 242 <= mouse_pos[1] <= 272:
                back_button = back_font.render('BACK', True, orange)
            # Mostra o botão na tela
            self._options_surface.blit(back_button, (190, 240))

            credito(self._options_surface)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if 190 <= mouse_pos[0] <= 407 and 82 <= mouse_pos[1] <= 112:
                        mouse_select.play()
                        self._play_music()

                    elif 190 <= mouse_pos[0] <= 337 and 162 <= mouse_pos[1] <= 192:
                        mouse_select.play()
                        self._control_menu()

                    elif 190 <= mouse_pos[0] <= 265 and 242 <= mouse_pos[1] <= 272:
                        mouse_select.play()
                        self._back()

            pygame.display.flip()

    # Desativa e ativa a música
    def _play_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    # Volta para o menu principal
    def _back(self):
        from GUI.main_menu import Menu
        menu = Menu()
        menu.main_menu()

    # Mostra os controles
    def _control_menu(self):
        control = Control()
        control.controls()


class Control:

    def __init__(self):
        self._icon_title()
        self._controls_surface = pygame.display.set_mode((x, y))

    def _icon_title(self):
        pygame.display.set_caption('Controls')
        icon = pygame.image.load('Images/Poongle_icon.png')
        icon = pygame.transform.smoothscale(icon, (32, 32))
        pygame.display.set_icon(icon)

    def controls(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()

            player_font = pygame.font.SysFont('segoeui', 20)

            # Mostra os controles do PLAYER 1 na tela
            player_one_text1 = player_font.render('PLAYER ONE CONTROL (LEFT):', True, white)
            player_one_text2 = player_font.render('W to go UP', True, orange)
            player_one_text3 = player_font.render('S to go DOWN', True, orange)
            self._controls_surface.blit(player_one_text1, (20, 20))
            self._controls_surface.blit(player_one_text2, (20, 50))
            self._controls_surface.blit(player_one_text3, (20, 80))

            # Mostra os controles do PLAYER 2 na tela
            player_two_text1 = player_font.render('PLAYER TWO CONTROL (RIGHT):', True, white)
            player_two_text2 = player_font.render('ARROW UP to go UP', True, orange)
            player_two_text3 = player_font.render('ARROW DOWN to go DOWN', True, orange)
            self._controls_surface.blit(player_two_text1, (310, 20))
            self._controls_surface.blit(player_two_text2, (310, 50))
            self._controls_surface.blit(player_two_text3, (310, 80))

            # Retângulo do botão "BACK"
            rect_back = pygame.draw.rect(self._controls_surface, black, (260, 342, 73, 30))
            # Cria o botão "BACK"
            back_font = pygame.font.SysFont('unispacebold', 30)
            back_button = back_font.render('BACK', True, white)
            # Muda a cor do botão "BACK" ao passar o mouse por cima
            if 260 <= mouse_pos[0] <= 333 and 342 <= mouse_pos[1] <= 372:
                back_button = back_font.render('BACK', True, orange)
            # Mostra o botão na tela
            self._controls_surface.blit(back_button, (260, 340))

            credito(self._controls_surface)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if 260 <= mouse_pos[0] <= 333 and 342 <= mouse_pos[1] <= 372:
                        mouse_select.play()
                        self._back()

            pygame.display.flip()

    # Volta para a tela Options
    def _back(self):
        options = Options()
        options.options_menu()
