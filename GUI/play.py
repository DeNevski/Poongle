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

# Música de fundo
def background_music():
    background_music = pygame.mixer.music.load('Sounds/backgroung_music.mp3')
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)

# Tela
x = 600
y = 400

class Play:

    def __init__(self):
        self._game_mode_surface = pygame.display.set_mode((x, y))
        self._icon_title()

    def _icon_title(self):
        pygame.display.set_caption('Poongle')
        icon = pygame.image.load('Images/Poongle_icon.png')
        icon = pygame.transform.smoothscale(icon, (32, 32))
        pygame.display.set_icon(icon)

    def game_mode(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()

            # Um jogador
            # Retângulo do botão "1 PLAYER"
            rect_one_player = pygame.draw.rect(self._game_mode_surface, black, (70, 103, 145, 28))
            # Cria botão "1 PLAYER"
            one_player_font = pygame.font.SysFont('unispacebold', 30)
            one_player_button = one_player_font.render('1 PLAYER', True, white)
            # Muda a cor do botão "1 PLAYER" ao passar o mouse por cima
            if 70 <= mouse_pos[0] <= 215 and 103 <= mouse_pos[1] <= 131:
                one_player_button = one_player_font.render('1 PLAYER', True, orange)
            # Mostra o botão na tela
            self._game_mode_surface.blit(one_player_button, (70, 100))

            # Dois jogadores
            # Retângulo do botão "2 PLAYERS"
            rect_two_players = pygame.draw.rect(self._game_mode_surface, black, (350, 103, 162, 28))
            # Cria botão "2 PLAYERS"
            two_players_font = pygame.font.SysFont('unispacebold', 30)
            two_players_button = two_players_font.render('2 PLAYERS', True, white)
            # Muda a cor do botão "2 PLAYERS" ao passar o mouse por cima
            if 350 <= mouse_pos[0] <= 512 and 103 <= mouse_pos[1] <= 131:
                two_players_button = two_players_font.render('2 PLAYERS', True, orange)
            # Mostra o botão na tela
            self._game_mode_surface.blit(two_players_button, (350, 100))

            # Voltar ao menu principal
            # Retângulo do botão "BACK"
            rect_back = pygame.draw.rect(self._game_mode_surface, black, (260, 303, 72, 28))
            # Cria botão "BACK"
            back_font = pygame.font.SysFont('unispacebold', 30)
            back_button = back_font.render('BACK', True, white)
            # Muda a cor do botão "BACK" ao passar o mouse por cima
            if 260 <= mouse_pos[0] <= 332 and 303 <= mouse_pos[1] <= 331:
                back_button = back_font.render('BACK', True, orange)
            # Mostra o botão na tela
            self._game_mode_surface.blit(back_button, (260, 300))

            credito(self._game_mode_surface)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if 70 <= mouse_pos[0] <= 215 and 103 <= mouse_pos[1] <= 131:
                        mouse_select.play()
                        self._run_game_one_player()

                    elif 350 <= mouse_pos[0] <= 512 and 103 <= mouse_pos[1] <= 131:
                        mouse_select.play()
                        self._run_game_two_players()

                    elif 260 <= mouse_pos[0] <= 332 and 303 <= mouse_pos[1] <= 331:
                        mouse_select.play()
                        self._back()

            pygame.display.flip()

    # Volta ao menu principal
    def _back(self):
        from GUI.main_menu import Menu
        menu = Menu()
        menu.main_menu()

    # Inicia o jogo para um jogador
    def _run_game_one_player(self):
        from Objects.objects import Ball, PlayerOne, Bot

        game_surface = GameSurface()
        ball = Ball(game_surface)
        player_one = PlayerOne(game_surface)
        bot = Bot(game_surface)
        while True:
            ball.move_ball()

            player_one.move_racket()
            player_one.collision(ball)
            player_one.points(ball)

            bot.move_bot(ball)
            bot.collision(ball)
            bot.points(ball)
            
            game_surface.clock()
            game_surface.update_screen()
            game_surface.close_window()

    # Inicia o jogo para dois jogadores
    def _run_game_two_players(self):
        from Objects.objects import Ball, PlayerOne, PlayerTwo

        game_surface = GameSurface()
        ball = Ball(game_surface)
        player_one = PlayerOne(game_surface)
        player_two = PlayerTwo(game_surface)
        while True:
            ball.move_ball()
            
            player_one.move_racket()
            player_one.collision(ball)
            player_one.points(ball)

            player_two.move_racket()
            player_two.collision(ball)
            player_two.points(ball)

            game_surface.clock()
            game_surface.update_screen()
            game_surface.close_window()


class GameSurface:

    def __init__(self):
        self._icon_title()
        self._game_surface = pygame.display.set_mode((x, y))
  
    def close_window(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Define o ícone e o título da janela
    def _icon_title(self):
        pygame.display.set_caption('Poongle')
        icon = pygame.image.load('Images/Poongle_icon.png')
        icon = pygame.transform.smoothscale(icon, (32, 32))
        pygame.display.set_icon(icon)

    def update_screen(self):
        pygame.display.flip()
        self._game_surface.fill((0, 0, 0))

    # Controla os frames da tela
    def clock(self):
        clock = pygame.time.Clock()
        return clock.tick(60) / 1000
    
    # Mostra a pontuação na tela
    def text(self, points, pos_x, pos_y):
        font = pygame.font.SysFont('unispacebold', 30)
        text = f'{points}'
        formatted_text = font.render(text, True, (255, 255, 255))
        self._game_surface.blit(formatted_text, (pos_x, pos_y))
    
    @property
    def surface(self):
        return self._game_surface

    @property
    def game_surface_width(self):
        return self._game_surface.get_width()
    
    @property
    def game_surface_height(self):
        return self._game_surface.get_height()
    

class EndGame:

    def __init__(self):
        self._icon_title()
        self._end_game_surface = pygame.display.set_mode((x, y))

    def _icon_title(self):
        pygame.display.set_caption('Poongle')
        icon = pygame.image.load('Images/Poongle_icon.png')
        icon = pygame.transform.smoothscale(icon, (32, 32))
        pygame.display.set_icon(icon)

    def end_game(self, winner):
        self._victory_song()

        while True:
            mouse_pos = pygame.mouse.get_pos()
            
            # Exibe o vencedor da partida
            end_game_font = pygame.font.SysFont('unispacebold', 30)
            the_winner = end_game_font.render('THE WINNER IS', True, white)
            winning_player = end_game_font.render(winner, True, orange)
            self._end_game_surface.blit(the_winner, (165, 50))
            if len(winner) <= 3:
                self._end_game_surface.blit(winning_player, (255, 100))
            else:
                self._end_game_surface.blit(winning_player, (215, 100))

            # Jogar novamente
            # Cria o retângulo do botão "PLAY AGAIN"
            rect_play_again = pygame.draw.rect(self._end_game_surface, black, (195, 343, 182, 28))
            # Cria o botão "PLAY AGAIN"
            play_again = end_game_font.render('PLAY AGAIN', True, white)
            # Muda a cor do botão "PLAY AGAIN" ao passar o mouse por cima
            if 195 <= mouse_pos[0] <= 377 and 343 <= mouse_pos[1] <= 371:
                play_again = end_game_font.render('PLAY AGAIN', True, orange)
            # Mostra na tela
            self._end_game_surface.blit(play_again, (195, 340))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if 195 <= mouse_pos[0] <= 377 and 343 <= mouse_pos[1] <= 371:
                        mouse_select.play()
                        background_music()
                        self._play_again()

            pygame.display.flip()

        # Volta para a tela game mode
    def _play_again(self):
        play = Play()
        play.game_mode()

        # Pausa a música de fundo e toca a de vitória
    def _victory_song(self):
        victory_song = pygame.mixer.music.load('Sounds/victory_song.wav')
        pygame.mixer.music.set_volume(0.20)
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        pygame.mixer.music.play()
    