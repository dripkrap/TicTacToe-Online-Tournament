import pygame
import itertools

size = [800,800]#size of the window
win = pygame.display.set_mode(size)#creates the window
mouse = pygame.mouse.get_pos()#tuple of the cursor's x and y coords
pygame.display.set_caption("client")#gives the window a name

clientNumber = 0

def redrawWindow():
    win.fill("gray")
    pygame.display.update()

def drawBoard():#draws the gameboard
    win.fill("gray")
    pygame.draw.rect(win, (0,0,0), [250,100,50,550])
    pygame.draw.rect(win, (0,0,0), [100,250,550,50])
    pygame.draw.rect(win, (0,0,0), [475,100,50,550])
    pygame.draw.rect(win, (0,0,0), [100,475,550,50])
    pygame.display.update()

quadX = [100,100,100,300,300,300,525,525,525]
quadY = [100,300,525,100,300,525,100,300,525]
quadWidth = [150,150,150,175,175,175,125,125,125]
quadHeight = [150,175,125,150,175,125,150,175,125]
#hitbox coordinates and dimensions
gameBox1 = pygame.Rect(quadX[0],quadY[0],quadWidth[0],quadHeight[0])
gameBox2 = pygame.Rect(quadX[1],quadY[1],quadWidth[1],quadHeight[1])
gameBox3 = pygame.Rect(quadX[2],quadY[2],quadWidth[2],quadHeight[2])
gameBox4 = pygame.Rect(quadX[3],quadY[3],quadWidth[3],quadHeight[3])
gameBox5 = pygame.Rect(quadX[4],quadY[4],quadWidth[4],quadHeight[4])
gameBox6 = pygame.Rect(quadX[5],quadY[5],quadWidth[5],quadHeight[5])
gameBox7 = pygame.Rect(quadX[6],quadY[6],quadWidth[6],quadHeight[6])
gameBox8 = pygame.Rect(quadX[7],quadY[7],quadWidth[7],quadHeight[7])
gameBox9 = pygame.Rect(quadX[8],quadY[8],quadWidth[8],quadHeight[8])
#establishing hitboxes

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("clicked!")
                if gameBox1.collidepoint(event.pos):
                    print("hit")
                elif gameBox2.collidepoint(event.pos):
                    print("hit")
                elif gameBox3.collidepoint(event.pos):
                    print("hit")
                elif gameBox4.collidepoint(event.pos):
                    print("hit")
                elif gameBox5.collidepoint(event.pos):
                    print("hit")
                elif gameBox6.collidepoint(event.pos):
                    print("hit")
                elif gameBox7.collidepoint(event.pos):
                    print("hit")
                elif gameBox8.collidepoint(event.pos):
                    print("hit")
                elif gameBox9.collidepoint(event.pos):
                    print("hit")
        
                    
            

        drawBoard()

main()