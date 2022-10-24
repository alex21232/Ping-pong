#Mentions
print("Javier Ceballo")
print("Theilyn Saballo")

#importar libreriass
import pygame
import random as rd

#Initializa pygame
pygame.init()

#RGB
background_color = (0,0,0)
player_color = (255,255,255)
player_color_2 = (255,255,255)
ball_color = (255,255,255)
line_color = (255,255,255)

#score variables
player_1_score = 0
player_2_score = 0

#score font
score_font = pygame.font.Font("font.ttf", 69)

#win font
win_font = pygame.font.Font("font.ttf", 138)

#player size
players_windth = 15
players_height = 90

#player 1 coordinates
player_x_1 = 15
player_y_1 = 290 - (players_height/2)

#player 1 speed
player_1_y_speed = 0

#player two coordinates
player_x_2 = 860 - players_height
player_y_2 = player_y_1

#player 2 speed
player_2_y_speed = 0

#player 2 size
players_windth_2 = 15
players_height_2 = 90

#ball coordinates
ball_x = 400
ball_y = 300
ball_radius = 20

#ball speed
ball_speed_x = 0.6
ball_speed_y = 0.6

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

#score position in the screen Player one
player_1_score_x = 360
player_1_score_y = 10

#score position in the screen Player two
player_2_score_x = 417
player_2_score_y = 10

#win text position 
win_x = 100
win_y = 250

#function score - Player 1
def show_score_1(x, y):
    score_1 = score_font.render(str(player_1_score), True, (255, 255, 255))
    screen.blit(score_1, (x, y))

#function score - Player 2
def show_score_2(x, y):
    score_2 = score_font.render(str(player_2_score), True, (255, 255, 255))
    screen.blit(score_2, (x, y))



#Game loop
running = True
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #player key controls
        #cheks for keydowm event
        if event.type == pygame.KEYDOWN:

            #player one dowm
            if event.key == pygame.K_w: 
                player_1_y_speed = -1

            if event.key == pygame.K_s: 
                player_1_y_speed = +1

            #player two dowm
            if event.key == pygame.K_UP: 
                player_2_y_speed = -1

            if event.key == pygame.K_DOWN: 
                player_2_y_speed = +1

        if event.type == pygame.KEYUP:

            #player 1 up
            if event.key == pygame.K_w: 
                player_1_y_speed = -0

            if event.key == pygame.K_s: 
                player_1_y_speed = +0

            #player 2 up
            if event.key == pygame.K_UP: 
                player_2_y_speed = -0

            if event.key == pygame.K_DOWN: 
                player_2_y_speed = +0

#player movements
    player_y_1 += player_1_y_speed

#player 2 movements
    player_y_2 += player_2_y_speed

    #player boundaries

    #player one
    if player_y_1 <= 0:
        player_y_1 = 0
    
    if player_y_1 >= screen_height - players_height:
        player_y_1 = screen_height - players_height

    #player two
    if player_y_2 <= 0:
        player_y_2 = 0

    if player_y_2 >= screen_height - players_height_2:
        player_y_2 = screen_height - players_height_2

#ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    #ball boundaries: top or buttom
    if ball_y > (screen_height - ball_radius) or ball_y < ball_radius:
        ball_speed_y *= -1  

    #ball boudaries (right or left) add score
    if ball_x > screen_windth:

        player_1_score += 1

        ball_x = screen_windth/2
        ball_y = screen_height/2

        ball_speed_x *= rd.choice([-1, 1])

    elif ball_x < 0:

        player_2_score += 1

        ball_x = screen_windth/2
        ball_y = screen_height/2

        ball_speed_x *= rd.choice([-1, 1])  

#RGB
    screen.fill(background_color)

#Drawing are 

#draw the center line
    pygame.draw.aaline(screen, line_color, (screen_windth/2,0),(screen_windth/2, screen_height) )

#Draw the ball
    ball = pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

 #player one - left :rectangle
    player_one = pygame.draw.rect(screen, player_color, (player_x_1, player_y_1, players_windth, players_height))

#player two - left :rectangle
    player_two = pygame.draw.rect(screen, player_color_2, (player_x_2, player_y_2, players_windth_2, players_height_2))

    #Colitions
    if ball.colliderect(player_one) or ball.colliderect(player_two):
        ball_speed_x *= -1

    #player 1 win
    if player_1_score == 3:

        ball_y = 1000
        player_1_y_speed = 0.0
        player_2_y_speed = 0.0  
        ball_speed_x = 0
        ball_speed_y = 0  

        win_text = win_font.render("player 1 win", True, (255, 255, 255))
        screen.blit(win_text, (win_x, win_y))

    #player 2 win
    if player_2_score == 3:
        
        player_2_y_speed = 0.0
        player_1_y_speed = 0.0
        ball_y = 1000
        ball_speed_x = 0
        ball_speed_y = 0         

        win_text = win_font.render("player 2 win", True, (255, 255, 255))
        screen.blit(win_text, (win_x, win_y)) 

    #function show score
    show_score_1(player_1_score_x, player_1_score_y)

    show_score_2(player_2_score_x, player_2_score_y)

#Refresh the window
    pygame.display.flip()

