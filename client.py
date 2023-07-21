import pygame
import random
from network import Network

width = 800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

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
score = 0
##############################################################


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win,player):
    win.fill((0,0,0))
    player.draw(win)
    # player2.draw(win)
    pygame.display.update()

def create_enemies(enemy_army_list):
    delay = random.random()
    if len(enemy_army_list) < amount_of_enemies or delay < 0.2:
        enemy_random_x = random.randint(0, 800 - enemy_size)
        enemy_y = 0
        enemy_army_list.append([enemy_random_x,enemy_y])


##################################################################
def draw_enemies(enemy_army_list):
    for enemy_position in enemy_army_list:
        pygame.draw.rect(win, ENEMY_COLOR, (enemy_position[0],enemy_position[1], enemy_size, enemy_size))

def drop_store_enemies(enemy_army_list):
# DROP AND STORE ENEMY
    global score
    global enemy_velocity

    for idx,enemy_position in enumerate(enemy_army_list):
        if enemy_position[1] >= 0 and enemy_position[1] < height:
            enemy_position[1] += enemy_velocity
        else:
            score += 1
            enemy_army_list.pop(idx)

    if score%20 == 0:
        enemy_velocity += 1
    else:
        pass



run = True
# n = Network()
# startPos = read_pos(n.getPos())
p1 = Player(100,100,50,50,(0,255,0))
# p2 = Player(200,200,50,50(0,0,255))
clock = pygame.time.Clock()

while run:
    clock.tick(50)
    # p2Pos = read_pos(n.send(make_pos((p1.x, p1.y))))
    # p2.x = p2Pos[0]
    # p2.y = p2Pos[1]
    # p2.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    create_enemies(enemy_army_list)
    drop_store_enemies(enemy_army_list)
    draw_enemies(enemy_army_list)
    p1.move()
    redrawWindow(win, p1)

