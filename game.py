import pygame
import random
import config

pygame.init()
 
dis = pygame.display.set_mode((config.dis_width, config.dis_height))
pygame.display.set_caption('Snake Game by Jander')
 
clock = pygame.time.Clock()
 
font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, config.colors['yellow'])
    dis.blit(value, [0, 0])
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, config.colors['black'], [x[0], x[1], snake_block, snake_block])

 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [config.dis_width / 6, config.dis_height / 3])
 
 
def game_loop():
    game_over = False
    game_close = False
 
    x1 = config.dis_width / 2
    y1 = config.dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, config.dis_width - config.snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, config.dis_height - config.snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(config.colors['blue'])
            game_over_msg = font_style.render('Game Over', True, config.colors['red'])
            press_msg = font_style.render('Pressione:', True, config.colors['white'])
            quit_message = font_style.render('Q para sair', True, config.colors['white'])
            restart_message = font_style.render('C Para jogar novamente', True, config.colors['white'])
            dis.blit(game_over_msg, [280, 160])
            dis.blit(press_msg, [280, 180])
            dis.blit(quit_message, [280, 200])
            dis.blit(restart_message, [280, 220])
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -config.snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = config.snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -config.snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = config.snake_block
                    x1_change = 0
 
        if x1 >= config.dis_width or x1 < 0 or y1 >= config.dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(config.colors['blue'])
        pygame.draw.rect(dis, config.colors['green'], [foodx, foody, config.snake_block, config.snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(config.snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, config.dis_width - config.snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, config.dis_height - config.snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(config.snake_speed)
 
    pygame.quit()
    quit()
 
 
game_loop()