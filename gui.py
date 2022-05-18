import pygame

width=800
height=600

input = "309050020006000010452000683004000002001074500805109760503296800600081300098040006"
guesses = "000000000000000000000000000000000000000000000000000000000000000000000000000000000"
solution = "319658427786432915452917683974865132261374598835129764543296871627581349198743256"
g_loc = [0,0]


WHITE = (255,255,255)
BLACK = (0,0,0)
L_GRAY = (200,200,200)
GRAY = (170,170,170)
D_GRAY = (100,100,100)
L_BLUE = (131,238,255)
D_BLUE =(0,0,225)
RED = (255,0,0)

screenpadx = 242
screenpady = 142
grid = []
guess = '0'


def DrawBoard():
    #Draw the Board
    #Horizontal Lines
    pygame.draw.line(screen, BLACK, (243,246) , (556, 246), 4)
    pygame.draw.line(screen, BLACK, (243,351) , (556, 351), 4)

    #Vertical Lines
    pygame.draw.line(screen, BLACK, (346,142) , (346, 456), 4)
    pygame.draw.line(screen, BLACK, (451,142) , (451, 456), 4)

    #Grid
    blockSize = 35 #Set the size of the grid block
    for x in range(242, 523, blockSize):
        for y in range(142, 423, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, rect, 1)
    #Outline
    pygame.draw.rect(screen, BLACK, pygame.Rect(240, 140, 319,319), 4)

def MakeGrid():
    for y in range(9):
        row = []
        for x in range(9):
            row.append([x * (35) + screenpadx, y * (35) + screenpady, WHITE])
        grid.append(row)

def LoadBoard():
    x = 254
    y = 147
    for i in range(81):

        if input[i] == '0':
            screen.blit(pygame.font.SysFont('Corbel',25).render(" " , True , BLACK) , (x,y))
        else:
            screen.blit(pygame.font.SysFont('Corbel',25).render(input[i] , True , BLACK) , (x,y))
        x+=35
        if (i+1) % 9 == 0:
            y+=35
            x=254
        # pygame.display.flip()
    # screen.blit(pygame.font.SysFont('Corbel',25).render('6' , True , BLACK) , (254,147))

def update():
    global input, guesses, solution, guess
    x = 254
    y = 147

    location = (g_loc[0] * 9) + g_loc[1]
    updates = True
    if input[location] == solution[location]:
        guess = '0'
    elif solution[location] == guess:
        input = input[:location] + guess + input[location+1:]
        guesses = guesses[:location] + '0' + guesses[location+1:]
    else:
        if not guess == '0':
            guesses = guesses[:location] + guess + guesses[location+1:]
    for i in range(81):
        if guesses[i] == '0':
            screen.blit(pygame.font.SysFont('Corbel',25).render(" " , True , BLACK) , (x,y))
        else:
            screen.blit(pygame.font.SysFont('Corbel',25).render(guesses[i] , True , RED) , (x,y))
        x+=35
        if (i+1) % 9 == 0:
            y+=35
            x=254

def VisualLine():
    if 244 <= mouse[0] <= 278 and 144 <= mouse[1] <= 451:
        pygame.draw.rect(screen,WHITE,[244,144,315,315])
        pygame.draw.rect(screen,L_GRAY,[244,144,33,315])
        VisualH()
    elif 278 <= mouse[0] <= 313 and 144 <= mouse[1] <= 451:
        pygame.draw.rect(screen,WHITE,[244,144,315,315])
        pygame.draw.rect(screen,L_GRAY,[278,144,33,315])
        VisualH()
    elif 313 <= mouse[0] <= 348 and 144 <= mouse[1] <= 451:
        pygame.draw.rect(screen,WHITE,[244,144,315,315])
        pygame.draw.rect(screen,L_GRAY,[313,144,33,315])
        VisualH()
    elif 348 <= mouse[0] <= 383 and 144 <= mouse[1] <= 451:
        pygame.draw.rect(screen,WHITE,[244,144,315,315])
        pygame.draw.rect(screen,L_GRAY,[348,144,33,315])
        VisualH()
    elif 383 <= mouse[0] <= 418 and 144 <= mouse[1] <= 451:
        pygame.draw.rect(screen,WHITE,[244,144,315,315])
        pygame.draw.rect(screen,L_GRAY,[383,144,33,315])
        VisualH()
    elif 418 <= mouse[0] <= 453 and 144 <= mouse[1] <= 451:
        pygame.draw.rect(screen,WHITE,[244,144,315,315])
        pygame.draw.rect(screen,L_GRAY,[418,144,33,315])
        VisualH()
    elif 453 <= mouse[0] <= 488 and 144 <= mouse[1] <= 451:
        pygame.draw.rect(screen,WHITE,[244,144,315,315])
        pygame.draw.rect(screen,L_GRAY,[453,144,33,315])
        VisualH()
    elif 488 <= mouse[0] <= 523 and 144 <= mouse[1] <= 451:
        pygame.draw.rect(screen,WHITE,[244,144,315,315])
        pygame.draw.rect(screen,L_GRAY,[488,144,33,315])
        VisualH()
    elif 523 <= mouse[0] <= 558 and 144 <= mouse[1] <= 451:
        pygame.draw.rect(screen,WHITE,[244,144,315,315])
        pygame.draw.rect(screen,L_GRAY,[523,144,33,315])
        VisualH()
    else:
        pygame.draw.rect(screen,WHITE,[244,144,315,315])


def VisualH():
    if 244 <= mouse[0] <= 551 and 144 <= mouse[1] <= 179:
        pygame.draw.rect(screen,L_GRAY,[244,144,315,33])
    elif 244 <= mouse[0] <= 551 and 178 <= mouse[1] <= 214:
        pygame.draw.rect(screen,L_GRAY,[244,178,315,33])
    elif 244 <= mouse[0] <= 551 and 214 <= mouse[1] <= 249:
        pygame.draw.rect(screen,L_GRAY,[244,213,315,33])
    elif 244 <= mouse[0] <= 551 and 249 <= mouse[1] <= 284:
        pygame.draw.rect(screen,L_GRAY,[244,248,315,33])
    elif 244 <= mouse[0] <= 551 and 284 <= mouse[1] <= 319:
        pygame.draw.rect(screen,L_GRAY,[244,283,315,33])
    elif 244 <= mouse[0] <= 551 and 319 <= mouse[1] <= 354:
        pygame.draw.rect(screen,L_GRAY,[244,318,315,33])
    elif 244 <= mouse[0] <= 551 and 354 <= mouse[1] <= 389:
        pygame.draw.rect(screen,L_GRAY,[244,353,315,33])
    elif 244 <= mouse[0] <= 551 and 389 <= mouse[1] <= 424:
        pygame.draw.rect(screen,L_GRAY,[244,388,315,33])
    elif 244 <= mouse[0] <= 551 and 424 <= mouse[1] <= 459:
        pygame.draw.rect(screen,L_GRAY,[244,423,315,33])

def Choices():

    mouse = pygame.mouse.get_pos()

    if 242 <= mouse[0] <= 382 and 480 <= mouse[1] <= 520:
        pygame.draw.rect(screen,L_GRAY,[242,480,140,40])
    else:
        pygame.draw.rect(screen,GRAY,[242,480,140,40])

    if 610 <= mouse[0] <= 640 and 232 <= mouse[1] <= 262:
        pygame.draw.rect(screen,L_GRAY,[610,232,35,35])
    else:
        pygame.draw.rect(screen,GRAY,[610,232,35,35])

    if 660 <= mouse[0] <= 690 and 232 <= mouse[1] <= 262:
        pygame.draw.rect(screen,L_GRAY,[660,232,35,35])
    else:
        pygame.draw.rect(screen,GRAY,[660,232,35,35])
    
    if 710 <= mouse[0] <= 740 and 232 <= mouse[1] <= 262:
        pygame.draw.rect(screen,L_GRAY,[710,232,35,35])
    else:
        pygame.draw.rect(screen,GRAY,[710,232,35,35])

    if 610 <= mouse[0] <= 640 and 282 <= mouse[1] <= 312:
        pygame.draw.rect(screen,L_GRAY,[610,282,35,35])
    else:
        pygame.draw.rect(screen,GRAY,[610,282,35,35])

    if 660 <= mouse[0] <= 690 and 282 <= mouse[1] <= 312:
        pygame.draw.rect(screen,L_GRAY,[660,282,35,35])
    else:
        pygame.draw.rect(screen,GRAY,[660,282,35,35])
    
    if 710 <= mouse[0] <= 740 and 282 <= mouse[1] <= 312:
        pygame.draw.rect(screen,L_GRAY,[710,282,35,35])
    else:
        pygame.draw.rect(screen,GRAY,[710,282,35,35])

    if 610 <= mouse[0] <= 640 and 332 <= mouse[1] <= 362:
        pygame.draw.rect(screen,L_GRAY,[610,332,35,35])
    else:
        pygame.draw.rect(screen,GRAY,[610,332,35,35])

    if 660 <= mouse[0] <= 690 and 332 <= mouse[1] <= 362:
        pygame.draw.rect(screen,L_GRAY,[660,332,35,35])
    else:
        pygame.draw.rect(screen,GRAY,[660,332,35,35])
    
    if 710 <= mouse[0] <= 740 and 332 <= mouse[1] <= 362:
        pygame.draw.rect(screen,L_GRAY,[710,332,35,35])
    else:
        pygame.draw.rect(screen,GRAY,[710,332,35,35])

     # superimposing the text onto our button
    screen.blit(pygame.font.SysFont('Corbel',31).render('Solve' , True , WHITE) , (281,485))
    
    screen.blit(pygame.font.SysFont('Corbel',31).render('1' , True , WHITE) , (620,235))
    screen.blit(pygame.font.SysFont('Corbel',31).render('2' , True , WHITE) , (670,235))
    screen.blit(pygame.font.SysFont('Corbel',31).render('3' , True , WHITE) , (720,230))
    screen.blit(pygame.font.SysFont('Corbel',31).render('4' , True , WHITE) , (620,280))
    screen.blit(pygame.font.SysFont('Corbel',31).render('5' , True , WHITE) , (670,280))
    screen.blit(pygame.font.SysFont('Corbel',31).render('6' , True , WHITE) , (720,285))
    screen.blit(pygame.font.SysFont('Corbel',31).render('7' , True , WHITE) , (620,330))
    screen.blit(pygame.font.SysFont('Corbel',31).render('8' , True , WHITE) , (670,335))
    screen.blit(pygame.font.SysFont('Corbel',31).render('9' , True , WHITE) , (720,328))

 


#initialize the game
pygame.init()

#creates the screen
screen = pygame.display.set_mode((width, height))

#Caption
pygame.display.set_caption("Sudoku")
#Set Icon
icon = pygame.image.load('Icons/sudoku.png')
pygame.display.set_icon(icon)


#Background
screen.fill(WHITE)
screen.blit(pygame.font.SysFont('Corbel',45).render('SUDOKU' , True , BLACK) , (320,80))

MakeGrid()
current = [0,0,WHITE]
clicked = False


running = True
while running:
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 242 <= mouse[0] <= 382 and 480 <= mouse[1] <= 520:
                input = solution

            if 610 <= mouse[0] <= 640 and 232 <= mouse[1] <= 262:
                guess = '1'

            if 660 <= mouse[0] <= 690 and 232 <= mouse[1] <= 262:
                guess = '2'
            
            if 710 <= mouse[0] <= 740 and 232 <= mouse[1] <= 262:
                guess = '3'

            if 610 <= mouse[0] <= 640 and 282 <= mouse[1] <= 312:
                guess = '4'

            if 660 <= mouse[0] <= 690 and 282 <= mouse[1] <= 312:
                guess = '5'
            
            if 710 <= mouse[0] <= 740 and 282 <= mouse[1] <= 312:
                guess = '6'

            if 610 <= mouse[0] <= 640 and 332 <= mouse[1] <= 362:
                guess = '7'

            if 660 <= mouse[0] <= 690 and 332 <= mouse[1] <= 362:
                guess = '8'
            
            if 710 <= mouse[0] <= 740 and 332 <= mouse[1] <= 362:
                guess = '9'


            mpos_x, mpos_y = event.pos

            mpos_x -= screenpadx
            mpos_y -= screenpady

            col = mpos_x // 35
            row = mpos_y // 35
            if row >= 0 and col >= 0:
                try:
                    # calculate the boundaries of the cell
                    cell_x_min, cell_y_min =  col * (35), row * (35)
                    cell_x_max = cell_x_min + 35
                    cell_y_max = cell_y_min + 35
                    # now we will see if the user clicked the cell or the margin
                    if cell_x_min <= mpos_x <= cell_x_max and cell_y_min <= mpos_y <= cell_y_max:
                        # grid[row][col][2] = GRAY if event.button == 1 else WHITE
                        clicked = True
                        current = grid[row][col]
                        g_loc[0] = row
                        g_loc[1] = col
                    
                except IndexError: # clicked outside of the GRID
                    pass   

    Choices()
    VisualLine()

    if clicked:
        pygame.draw.rect(screen, L_BLUE, (current[0], current[1], 35, 35))
        if not guess == '0':
            update()
            guess = '0'
    # elif not clicked:
    #     pygame.draw.rect(screen, WHITE, (current[0], current[1], 35, 35))
    update()
    DrawBoard()
    LoadBoard()
    pygame.display.update()

