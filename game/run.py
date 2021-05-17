import pygame,sys,time,random

# check error game

check_error = pygame.init()
if check_error[1]>0:
    print('[!] {check_error} error game')
else :
    print('[+] Game Sukses Install')

### ===========Window Game =========

size_x =720
size_y = 480

# title game
pygame.display.set_caption('Hendry Snake')
screen = pygame.display.set_mode((size_x,size_y))

#### ======================= Game Variabel ==================
# color
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255,255)
green = pygame.Color(0,255,0)
blue = pygame.Color(102, 204, 255)

# sound 
pygame.mixer.init()
eating = pygame.mixer.Sound('apple_crunch.wav')


#score 
score =0

level = 100

#show skor function
def show_me ():
    hend_font = pygame.font.SysFont('times new roman',14)
    hend_surface = hend_font.render('eNjoy Hends Game :)',True,black)
    hend_rect = hend_surface.get_rect()
    hend_rect.midtop = (600,15)

    screen.blit(hend_surface,hend_rect)
    pygame.display.flip()

def show_score():
    score_font = pygame.font.SysFont('consolas',20)
    score_surface = score_font.render('Point :' +str(score) ,True,black)
    score_rect =score_surface.get_rect()
    score_rect.midtop = (72,15)

    screen.blit(score_surface,score_rect)
    pygame.display.flip()


# game over display
def game_over ():
    my_font = pygame.font.SysFont('times new roman',90)
    game_over_surface =my_font.render('END',True,white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (size_x/2,size_y/4)
    screen.fill(black)
    screen.blit(game_over_surface,game_over_rect)

    pygame.display.flip()
    time.sleep(3)
    pygame.quit()


#snake 
snake_pos = [100,50]
snake_body = [[100,50],[90,50],[80,50]]
change_to = 'RIGHT'
direction = 'RIGHT'

#food 
food_pos =[random.randrange(1,size_x//10)*10,random.randrange(1,size_y//10)*10]

# Change Background to white 
screen.fill(white)

#running 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
               
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
               
                
            if event.key == pygame.K_UP:
                change_to = 'UP'
               
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
                
        
    
    #update screen to white again
    screen.fill(white)

    #creat snake 
    for pos in snake_body:
        pygame.draw.rect(screen,blue,pygame.Rect(pos[0],pos[1],10,10))
    snake_body.insert(0,list(snake_pos))
    #snake_body.pop()
    

    # FIX DIRECTION 
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    #snake run
    if direction == 'RIGHT' :
        snake_pos[0] += 10
    if direction == 'LEFT' :
        snake_pos[0] -= 10
    if direction == 'UP' :
        snake_pos[1] -= 10
    if direction == 'DOWN' :
        snake_pos[1] += 10

    # snake over window 
        
    if snake_pos[0]>size_x:
        snake_pos[0] = 0
    if snake_pos[0]<0:
        snake_pos[0] = size_x
    if snake_pos[1] > size_y:
        snake_pos[1] =0
    if snake_pos[1]<0:
        snake_pos[1] = size_y

    #creat food
    pygame.draw.ellipse(screen,green,pygame.Rect(food_pos[0],food_pos[1],10,10))
    if snake_pos == food_pos:
        #setiap memakan -> menambah 1 score dan 1 level
        score +=1
        level+=1 
        eating.play() 
        
        while snake_pos == food_pos:
            food_pos =[random.randrange(1,size_x//10)*10,random.randrange(1,size_y//10)*10]
    else:
        snake_body.pop()
    
    show_score()
    show_me()
    for block in snake_body:
        if snake_pos[0]==block[0] and snake_pos[1]==block[1]:
            game_over()
    #level 
    pygame.time.Clock().tick(level)

    #Update screen
    pygame.display.update()
