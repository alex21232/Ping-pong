#importar libreriass
import pygame

#Initializa pygame
pygame.init()

#RGB
background_color = (0,0,7)
player_color = (255,255,255)
player_color_2 = (255,255,255)
ball_color = (255,255,255)
line_color = (255,255,255)

#player size
players_windth = 15
players_height = 90

#player 1 coordinates
player_x_1 = 50 
player_y_1 = 50

#player two coordinates
player_x_2 = 750
player_y_2 = 150

players_windth_2 = 15
players_height_2 = 90

#ball coordinates
ball_x = 400
ball_y = 300
ball_radius = 20

#icon
icon = pygame.image.load("Pong.png")
pygame.display.set_icon(icon)

#title
pygame.display.set_caption("Ping Pong")

#window size
screen_windth = 800
screen_height = 600

# size variable
size = (screen_windth, screen_height)

#show window
screen = pygame.display.set_mode(size)

#Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#RGB
    screen.fill(background_color)

#Drawing are 

#Draw the ball
    ball = pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

# draw the center line
    pygame.draw.aaline(screen, line_color, (screen_windth/2,0),(screen_windth/2, screen_height) )

    #player one - left :rectangle
    player_one = pygame.draw.rect(screen, player_color, (player_x_1, player_y_1, players_windth, players_height))

#player two - left :rectangle
    player_two = pygame.draw.rect(screen, player_color_2, (player_x_2, player_y_2, players_windth_2, players_height_2))

    #Refresh the window
    pygame.display.flip()

