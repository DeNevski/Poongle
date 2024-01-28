import pygame
from sys import exit
from GUI.play import *

pygame.init()    

orange = (255, 117, 24)
white = (255, 255, 255)

sound_point = pygame.mixer.Sound('Sounds/point.wav')


class Ball:

    def __init__(self, screen):
        self.game_surface = screen
        self.x_ball = 300
        self.y_ball = 200
        self.diameter = 10
        self.speed_x = 5
        self.speed_y = 5
        
    def create_ball(self):
        return pygame.draw.circle(self.game_surface.surface, orange, (self.x_ball, self.y_ball), self.diameter)
    
    def move_ball(self):
        # Movimendo da bola no eixo X
        self.x_ball += self.speed_x
        if self.x_ball >= self.game_surface.game_surface_width - self.diameter or self.x_ball <= self.diameter:
            self.speed_x = -self.speed_x
        # Movimento da bola no eixo Y
        self.y_ball += self.speed_y
        if self.y_ball > self.game_surface.game_surface_height - (self.diameter * 1.5)  or self.y_ball <= self.diameter:
            self.speed_y = -self.speed_y  

class PlayerOne:

    def __init__(self, screen):
        self.game_surface = screen
        self._x_racket = 10
        self._y_racket = 150
        self._width_racket = 5
        self._heigh_racket = 70
        self._speed = 7
        self._point = 0

    def _create_racket(self):
        pygame.draw.rect(self.game_surface.surface, white, (self._x_racket, self._y_racket, self._width_racket, self._heigh_racket))
        
    def move_racket(self):
        self._create_racket()
        # Movimento da raquete para subir
        if pygame.key.get_pressed()[pygame.K_w]:
            self._y_racket -= self._speed
            if self._y_racket < 0:
                self._y_racket = 0
        # Movimento da raquete para descer
        elif pygame.key.get_pressed()[pygame.K_s]:
            self._y_racket += self._speed
            # Não deixa a raquete ultrapassar as bordas da tela
            limit = self.game_surface.game_surface_height - self._heigh_racket
            if self._y_racket > limit:
                self._y_racket = limit

    def racket_sound(self):
        racket_sound = pygame.mixer.Sound('Sounds/racket_sound.wav')
        racket_sound.play()

    def collision(self, ball):
        if self.racket.colliderect(ball.create_ball()):
            ball.speed_x = -ball.speed_x
            self.racket_sound()

    def points(self, ball):
        if ball.x_ball > 585:
            sound_point.play()
            self._point += 1
            ball.x_ball -= 15

        if self._point == 10:
            winner = 'Player 1'
            self.win(winner)
        self.game_surface.text(self._point, 180, 10)

    # Recebe um ganhador que atinja os 10 pontos primeiro
    def win(self, winner):
        from GUI.play import EndGame
        win = EndGame()
        win.end_game(winner) 

    @property
    def racket(self):
        return pygame.Rect(self._x_racket, self._y_racket, self._width_racket, self._heigh_racket)
    

class PlayerTwo(PlayerOne):

    def __init__(self, screen):
        self.game_surface = screen
        self._x_racket = 585
        self._y_racket = 150
        self._width_racket = 5
        self._heigh_racket = 70
        self._speed = 7
        self._point = 0

    def move_racket(self):
        self._create_racket()
        # Movimento da raquete para subir
        if pygame.key.get_pressed()[pygame.K_UP]:
            self._y_racket -= self._speed
            # Não deixa a raquete ultrapassar as bordas da tela
            if self._y_racket < 0:
                self._y_racket = 0
        # Movimento da raquete para descer
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self._y_racket += self._speed
            # Não deixa a raquete ultrapassar as bordas da tela
            limit = self.game_surface.game_surface_height - self._heigh_racket
            if self._y_racket > limit:
                self._y_racket = limit
        
    def points(self, ball):
        if ball.x_ball < 15:
            sound_point.play()
            self._point += 1
            ball.x_ball += 15

        if self._point == 10:
            winner = 'Player 2'
            self.win(winner)
        self.game_surface.text(self._point, 400, 10)


class Bot(PlayerOne):

    def __init__(self, screen):
        self.game_surface = screen
        self._x_bot = 585
        self._y_bot = 150
        self._width_bot = 5
        self._heigh_bot = 70
        self._point = 0

    def create_bot(self):
        pygame.draw.rect(self.game_surface.surface, white, (self._x_bot, self._y_bot, self._width_bot, self._heigh_bot))

    def move_bot(self, y):
        self.create_bot()
        self._y_bot = y.y_ball - 80
        # Não deixa a raquete ultrapassar as bordas da tela
        limit = self.game_surface.game_surface_height - self._heigh_bot
        if self._y_bot < 0:
            self._y_bot = 0
        elif self._y_bot > limit:
            self._y_bot = limit

    def points(self, ball):
        if ball.x_ball < 15:
            sound_point.play()
            self._point += 1
            ball.x_ball += 15

        if self._point == 10:
            winner = 'Bot'
            self.win(winner)
        self.game_surface.text(self._point, 400, 10)

    @property
    def racket(self):
        return pygame.Rect(self._x_bot, self._y_bot, self._width_bot, self._heigh_bot)
    