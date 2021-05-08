import pygame
import random
import os
import time

pygame.mixer.init()
pygame.init()


white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
brown = (200, 200, 30)
blue = (50, 50, 100)

screen_width = 1320
screen_height = 768
gameWindow = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


pygame.display.set_caption("Snake Game By Adarsh")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 80)


def screen_score(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        screen_score("Welcome to SnakesAndCity", red, 300, 200)
        screen_score("Created By Adarsh Kumar", red, 300, 400)
        screen_score("PRESS SPACE TO PLAY", black, 350, 600)
        screen_score(
            "1=Kya karu  2=52-gaj  3=burjkhalifa  4=lahore ", black, 5, 5)
        screen_score("5=nacch-rani  6=Tora  7=waliaan", black, 250, 70)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('Grateful(PaglaSongs).mp3')
                    pygame.mixer.music.play()
                    gameloop()
                elif event.key == pygame.K_1:
                    pygame.mixer.music.load('Kya_Karu_1.mp3')
                    pygame.mixer.music.play()
                    gameloop()
                elif event.key == pygame.K_2:
                    pygame.mixer.music.load('52_Gaj_Ka_Daman.mp3')
                    pygame.mixer.music.play()
                    gameloop()
                elif event.key == pygame.K_3:
                    pygame.mixer.music.load('Burjkhalifa_Laxmmi.mp3')
                    pygame.mixer.music.play()
                    gameloop()
                elif event.key == pygame.K_4:
                    pygame.mixer.music.load('Lagdi_Lahore_Di.mp3')
                    pygame.mixer.music.play()
                    gameloop()
                elif event.key == pygame.K_5:
                    pygame.mixer.music.load('Naach Rani-(Mr-Jat.in).mp3')
                    pygame.mixer.music.play()
                    gameloop()
                elif event.key == pygame.K_6:
                    pygame.mixer.music.load('TORA-(Mr-Jat.in).mp3')
                    pygame.mixer.music.play()
                    gameloop()
                elif event.key == pygame.K_7:
                    pygame.mixer.music.load('Waalian.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(70)


def gameloop():
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    if(not os.path.exists("last.txt")):
        with open("last.txt", "w") as g:
            g.write("0")
    with open("highscore.txt", "r") as f:
        hiscore = f.read()
    with open("last.txt", "r") as g:
        last = g.read()
    snk_list = []
    snk_length = 1
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 35
    velocity_x = 0
    velocity_y = 0
    fps = 70
    init_velocity = 5
    score = 0
    food_x = random.randint(20, 1320)
    food_y = random.randint(20, 750)
    while not exit_game:
        gameWindow.fill(blue)
        if game_over:
            with open("last.txt", "w") as g:
                g.write(str(score))
            if score == int(hiscore):
                with open("highscore.txt", "w") as f:
                    f.write(str(hiscore))
                if score == int(hiscore):
                    screen_score(
                        "Congratulations you have created a high score", brown, 60, 200,)
            screen_score("Game over!! Press enter to continue", red, 210, 350)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_over = False
                        welcome()
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        snake_x = snake_x + 10
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True

                    if event.key == pygame.K_LEFT:
                        snake_x = snake_x - 10
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        snake_y = snake_y - 10
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        snake_y = snake_y + 10
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_PAGEDOWN:
                        score += 10
                        if score > int(hiscore):
                            hiscore = score

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x-food_x) < 18 and abs(snake_y-food_y) < 18:
                score = score + 10
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length += 5
                if score > int(hiscore):
                    hiscore = score
            gameWindow.fill(brown)
            screen_score("Score: "+str(score)+"     Highscore : " +
                         str(hiscore)+"   Last score: "+str(last), blue, 120, 5)
            plot_snake(gameWindow, black, snk_list, snake_size)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                pygame.mixer.music.load('crash.mp3')
                pygame.mixer.music.play()
                game_over = True
            if head in snk_list[:-1]:
                pygame.mixer.music.load('crash.mp3')
                pygame.mixer.music.play()
                game_over = True
            pygame.draw.rect(gameWindow, red, [
                             food_x, food_y, snake_size, snake_size])

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
gameloop()
