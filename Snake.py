import pygame
import random

pygame.init()

#############################################
################ ПЕРЕМЕННЫЕ #################

# ДИСПЛЕЙ
displayHeight = 480
displayWidth = 640
display = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.update()
pygame.display.set_caption("Snake")

rectSize = 10

# ДАННЫЕ
colors = {
    "snake_head": (0, 255, 0),
    "snake_tail": (0, 190, 0),
    "apple": (255, 0, 0)
}

snake_pos = {
    "x": displayWidth/2,
    "y": displayHeight/2,

    "x_change": 0,
    "y_change": 0
}

snake_speed = 10

snake_tails = []

snake_pos["x_change"] = -snake_speed
for i in range(3):
    snake_tails.append([snake_pos["x"] + 10*i, snake_pos["y"]])

#############################################
############### ИГРОВОЙ ЦИКЛ ################
game_end = False
clock = pygame.time.Clock()

while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_pos["x_change"] == 0:
                snake_pos["x_change"] = -snake_speed
                snake_pos["y_change"] = 0
            elif event.key == pygame.K_RIGHT and snake_pos["x_change"] == 0:
                snake_pos["x_change"] = snake_speed
                snake_pos["y_change"] = 0
            elif event.key == pygame.K_UP and snake_pos["y_change"] == 0:
                snake_pos["x_change"] = 0
                snake_pos["y_change"] = -snake_speed
            elif event.key == pygame.K_DOWN and snake_pos["y_change"] == 0:
                snake_pos["x_change"] = 0
                snake_pos["y_change"] = snake_speed

    display.fill((0,0,0))

    # перерисовка змейки
    ltx = snake_pos["x"]
    lty = snake_pos["y"]

    for i,v in enumerate(snake_tails):
        _ltx = snake_tails[i][0]
        _lty = snake_tails[i][1]

        snake_tails[i][0] = ltx
        snake_tails[i][1] = lty

        ltx = _ltx
        lty = _lty

    for t in snake_tails:
        pygame.draw.rect(display, colors["snake_tail"], [
            t[0],
            t[1],
            rectSize,
            rectSize])

    snake_pos["x"] += snake_pos["x_change"]
    snake_pos["y"] += snake_pos["y_change"]



    # телепорт, если за экраном
    if(snake_pos["x"] <= -rectSize):
        snake_pos["x"] = displayWidth-rectSize

    elif (snake_pos["x"] >= displayWidth):
        snake_pos["x"] = 0

    elif (snake_pos["y"] <= -rectSize):
        snake_pos["y"] = displayHeight-rectSize

    elif (snake_pos["y"] >= displayHeight):
        snake_pos["y"] = 0

    pygame.draw.rect(display, colors["snake_head"], [
        snake_pos["x"],
        snake_pos["y"],
        rectSize,
        rectSize])

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
