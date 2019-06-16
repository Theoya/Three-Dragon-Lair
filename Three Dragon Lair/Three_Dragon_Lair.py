import pygame, sys, random, Three_Dragon_Lair_Classes

from pygame.locals import *


def spread(tilemap, snake):
    
    if (tilemap[snake.pos[1]][snake.pos[0]] == POISON):
        n = random.randint(0,8)
        if (n == 1): tilemap[snake.pos[1]+1][snake.pos[0]] = POISON
        if (n == 2): tilemap[snake.pos[1]-1][snake.pos[0]] = POISON
        if (n == 3): tilemap[snake.pos[1]][snake.pos[0]+1] = POISON
        if (n == 4): tilemap[snake.pos[1]][snake.pos[0]-1] = POISON
        return tilemap


fpsClock = pygame.time.Clock()
           
    
pygame.display.set_caption("Three Dragon Lair")
pygame.display.set_icon(pygame.image.load("Dragon.png"))
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# Texture indicies
DIRT = 0
ROCK = 1
WATER = 2
COAL = 3
CLOUD = 4
COIN = 5
WALL = 6
POISON = 7


# Cloud
cloudx = -200
cloudy = 0
acloudx = -300
acloudy = 0
FOG = pygame.image.load("cloud.png")

# Textures
BLACK = (0, 0, 0)
BROWN = pygame.image.load("dirt.png")
BLUE = pygame.image.load("water.png")
GRAY = pygame.image.load("Rock.png")


WHITE = (255,255,255)

# Map size
TILESIZE= 40
MAPWIDTH = 25
MAPHEIGHT = 15

# Resource pool and mapping textures
textures = {DIRT : BROWN,
        COAL : pygame.image.load("Coal.png"),
        WATER : BLUE,
        COIN : pygame.image.load("Treasure.png"),
        ROCK : GRAY,
        CLOUD : FOG,
        WALL : pygame.image.load("Wall.png"),
        POISON : pygame.image.load("Poison.png")}
resources=[DIRT, COIN,  WATER,  COAL, ROCK]

# Generates random map
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        num = random.randint(0, 20)
        if num == 0:
            tile = COIN
        elif num <= 1:
            tile = WALL
        elif num <= 8:
            tile = WATER
        elif num <= 12:
            tile = ROCK
        else:
            tile = DIRT
        tilemap[rw][cl] = tile

for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        if (cl == MAPWIDTH-1 or rw == MAPHEIGHT-1):
            tilemap[rw][cl] = WALL
        



inventory = {DIRT : 0,
        COAL : 0,
        WATER : 0,
        ROCK : 0,
        COIN : 0}
snekMova = 0
snekMovb = 0
snekMovc = 0
difficulty = 0
score = 0
# Sets players position, initializes display, font, and snake position,difficulty, score
pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE+50))
DISPLAY.fill(BLACK)
INVFONT = pygame.font.Font('FreeSans.ttf', 18)

playera = Three_Dragon_Lair_Classes.player([0,0], pygame.image.load("player.png").convert_alpha())
snakea = Three_Dragon_Lair_Classes.snake([10,10], pygame.image.load("Dragon.png").convert_alpha())

snakeb = Three_Dragon_Lair_Classes.snake([8,8], pygame.image.load("Dragon.png").convert_alpha())
snakec = Three_Dragon_Lair_Classes.snake([12,12], pygame.image.load("Dragon.png").convert_alpha())




# Game loop
while True:
    for event in pygame.event.get():
        print(event)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Button press event handler
        elif event.type == KEYDOWN:
            if(event.key == K_RIGHT) and playera.pos[0]<MAPWIDTH-1:
                if (tilemap[playera.pos[1]][playera.pos[0]+1] != WALL):
                    playera.pos[0]+=1
            if(event.key == K_LEFT) and playera.pos[0]>0:
                if (tilemap[playera.pos[1]][playera.pos[0]-1] != WALL):
                    playera.pos[0]-=1
            if(event.key == K_DOWN) and playera.pos[1]<MAPHEIGHT-1:
                if (tilemap[playera.pos[1]+1][playera.pos[0]] != WALL):
                    playera.pos[1]+=1
            if(event.key == K_UP) and playera.pos[1]>0:
                if (tilemap[playera.pos[1]-1][playera.pos[0]] != WALL):
                    playera.pos[1]-=1
            # Picking up resources
            if(event.key == K_SPACE):
                currentTile = tilemap[playera.pos[1]][playera.pos[0]]
                inventory[currentTile] += 1
                if (tilemap[playera.pos[1]][playera.pos[0]] == COIN):
                    score += 200
                    
                tilemap[playera.pos[1]][playera.pos[0]] = DIRT
                print(inventory)
                placePosition = 10
                for item in resources:
                    DISPLAY.blit(textures[item],(placePosition, MAPHEIGHT*TILESIZE+20))
                    placePosition += 30
                    
                    textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
                    scoreDisp = INVFONT.render(str(score), True, WHITE, BLACK)
                    
                    DISPLAY.blit(textObj, (placePosition, MAPHEIGHT*TILESIZE+20))
                    
                    
                    placePosition += 50
                scoreDisp = INVFONT.render(str(score), True, WHITE, BLACK)
                DISPLAY.blit(scoreDisp, (placePosition+100, MAPHEIGHT*TILESIZE+20))
    pygame.display.update()
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAY.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
            DISPLAY.blit(playera.image,(playera.pos[0]*TILESIZE,playera.pos[1]*TILESIZE))
    difficulty = inventory[COIN]
    snekMova +=1
    snekMovb +=1
    snekMovc +=1
    if (snekMova >= 11):
        snekMova = difficulty
        snakea.snakeLog(playera)
    if (snekMovb >= 13):
        snekMovb = difficulty
        snakeb.snakeLog(playera)
    if (snekMovc >= 15):
        snekMovc = difficulty
        snakec.snakeLog(playera)
        
        
    if (snakea.pos == playera.pos):
        if playera.image != pygame.image.load("winner.png"):
            playera.image = snakea.image
            inventory[COAL] = -100
    if (snakeb.pos == playera.pos):
        if playera.image != pygame.image.load("winner.png"):
            playera.image = snakeb.image
            inventory[COAL] = -100
    if (snakec.pos == playera.pos):
        if playera.image != pygame.image.load("winner.png"):
            playera.image = snakec.image
            inventory[COAL] = -100

    
                    
    if ((tilemap[playera.pos[1]][playera.pos[0]]) == WATER):
        if ((tilemap[playera.pos[1]][playera.pos[0]+1]) == DIRT):
            (tilemap[playera.pos[1]][playera.pos[0]+1]) = WATER
            
            
        if ((tilemap[playera.pos[1]+1][playera.pos[0]])== DIRT):
            (tilemap[playera.pos[1]+1][playera.pos[0]]) = WATER
            
                
            
        if ((tilemap[playera.pos[1]-1][playera.pos[0]])== DIRT):
            (tilemap[playera.pos[1]-1][playera.pos[0]]) = WATER
            
            
        if ((tilemap[playera.pos[1]][playera.pos[0]-1])== DIRT):
            (tilemap[playera.pos[1]][playera.pos[0]-1]) = WATER
            
            
                
        snekMova +=2
        snekMovb +=3
        snekMovc +=4
        
    spread(tilemap, snakea)
    spread(tilemap, snakeb)
    spread(tilemap, snakec)
    
    
    
    if (tilemap[snakea.pos[1]][snakea.pos[0]] == ROCK):
        tilemap[snakea.pos[1]][snakea.pos[0]] = POISON
    if (tilemap[snakeb.pos[1]][snakeb.pos[0]] == ROCK):
        tilemap[snakeb.pos[1]][snakeb.pos[0]] = POISON
    if (tilemap[snakec.pos[1]][snakec.pos[0]] == ROCK):
        tilemap[snakec.pos[1]][snakec.pos[0]] = POISON
         
        
        
        
    DISPLAY.blit(snakea.image,(snakea.pos[0]*TILESIZE,snakea.pos[1]*TILESIZE))
    DISPLAY.blit(snakeb.image,(snakeb.pos[0]*TILESIZE,snakeb.pos[1]*TILESIZE))
    DISPLAY.blit(snakec.image,(snakec.pos[0]*TILESIZE,snakec.pos[1]*TILESIZE))
    # Blits clouds, moves cloud
    DISPLAY.blit(textures[CLOUD].convert_alpha(),(cloudx,cloudy))
    DISPLAY.blit(textures[CLOUD].convert_alpha(),(acloudx,acloudy))
    cloudx+=1
    acloudx+=1

    # Creates a new cloud if the cloud is off map
    if cloudx>MAPWIDTH*TILESIZE:
        cloudy = random.randint(0,MAPHEIGHT*TILESIZE-20)
        cloudx = -200

    # Creates a new cloud if the cloud is off map
    if acloudx>MAPWIDTH*TILESIZE:
        acloudy = random.randint(0,MAPHEIGHT*TILESIZE-20)
        acloudx = -300
    if (inventory.get(COIN)>=10):
        playera.image = pygame.image.load("winner.png")
    if (tilemap[playera.pos[1]][playera.pos[0]+1] == DIRT):
        score -= 10
        fpsClock.tick(20)
    
    score -= 1
    pygame.display.update()
    fpsClock.tick(70)


