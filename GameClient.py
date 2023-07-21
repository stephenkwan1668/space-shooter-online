import sys
import pygame
import random
##############

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Dodgerino")

##############################################################

BOARD_WIDTH = 800
BOARD_HEIGHT = 600
RESET_BOARD_COLOR = [0,0,0]
screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
score = 0
SCORE_TEXT_COLOR = (255,255,0)
myFont = pygame.font.SysFont("monospace", 35)

###################################################################

PLAYER_COLOR = [0,225,0]
player_size = 50
player_position = [BOARD_WIDTH/2,BOARD_HEIGHT-player_size*2] # the player will be

###################################################################

ENEMY_COLOR = [225,0,0]
enemy_size = 50
enemy_velocity = 1

enemy_random_x = random.randint(0,800-enemy_size)
enemy_y = 0
enemy_position = [enemy_random_x,enemy_y]

enemy_army_list = [enemy_position]
amount_of_enemies = 1

#######################################################################
game_over = False

##################################################################
def create_enemies(enemy_army_list):
    delay = random.random()
    if len(enemy_army_list) < amount_of_enemies or delay < 0.2:
        enemy_random_x = random.randint(0, 800 - enemy_size)
        enemy_y = 0
        enemy_army_list.append([enemy_random_x,enemy_y])


##################################################################
def draw_enemies(enemy_army_list):
    for enemy_position in enemy_army_list:
        pygame.draw.rect(screen, ENEMY_COLOR, (enemy_position[0],enemy_position[1], enemy_size, enemy_size))

def drop_store_enemies(enemy_army_list):
# DROP AND STORE ENEMY
    global score
    global enemy_velocity

    for idx,enemy_position in enumerate(enemy_army_list):
        if enemy_position[1] >= 0 and enemy_position[1] < BOARD_HEIGHT:
            enemy_position[1] += enemy_velocity
        else:
            score += 1
            enemy_army_list.pop(idx)

    if score%20 == 0:
        enemy_velocity += 1
    else:
        pass


def Collision_Check(enemy_army_list,player_position):
    for enemy_position in enemy_army_list:
        if Check_Collide_Condition(player_position,enemy_position):
            return True
    return False


def Check_Collide_Condition(player_position,enemy_position):
    global game_over
    player_x = player_position[0]
    player_y = player_position[1]

    enemy_x = enemy_position[0]
    enemy_y = enemy_position[1]

    if enemy_x >= player_x and enemy_x < (player_x+player_size) \
        or player_x >= enemy_x and player_x < (enemy_x + enemy_size):

        if player_y < enemy_y and enemy_y < player_y + player_size \
        or player_y > enemy_y and player_y < enemy_y + enemy_size:
            return True
    return False

def player_boundary(player_position):
    global game_over
    if player_position[0] < 0 or player_position[0] > BOARD_WIDTH-player_size:
        game_over = True
    else:
        False
''''
line 38: 
            [enemy = right]
    [player = left]
detects collision of the left side of the player 
if enemy_x >= player_x and enemy_x < player_x+player_size

line 42: reversed

height detection:
and player_y <= enemy_y and player_y <= player_y + enemy_size:
                    '''
while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()


    x = int(player_position[0])
    y = int(player_position[1])
    movement_velocity = 25

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= movement_velocity
    elif keys[pygame.K_RIGHT]:
        x += movement_velocity
    elif keys[pygame.K_UP]:
        y -= movement_velocity
    elif keys[pygame.K_DOWN]:
        y += movement_velocity
    else:
        pass
    player_position = [x,y]





    screen.fill(RESET_BOARD_COLOR)    # removing the traces of the previous positions by filling the screen black
    player_boundary(player_position)
    create_enemies(enemy_army_list)
    drop_store_enemies(enemy_army_list)
    draw_enemies(enemy_army_list)

    text = "Score:" + str(score*5)
    label = myFont.render(text, 1, SCORE_TEXT_COLOR)
    screen.blit(label, (BOARD_WIDTH - 200, BOARD_HEIGHT - 40))

    if Collision_Check(enemy_army_list,player_position):
        game_over = True
        break

    pygame.draw.rect(screen, PLAYER_COLOR, (player_position[0], player_position[1], player_size, player_size))
    print("scoreL: "+str(score))
    print("velocity: "+str(enemy_velocity))
    clock.tick(10)
    pygame.display.update()




