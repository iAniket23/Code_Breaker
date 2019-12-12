import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((753, 678))
pygame.display.set_caption("Code Breaker")
screen.fill((255,255,255))


num = [pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png'), pygame.image.load('4.png'), pygame.image.load('5.png'), pygame.image.load('6.png'), pygame.image.load('7.png'), pygame.image.load('8.png'), pygame.image.load('9.png'), pygame.image.load('0.png')]
arrow = pygame.image.load('arr.png')
circ= pygame.image.load('cir.png')
cros= pygame.image.load('cro.png')
bg=pygame.image.load('bg1.png')
bgsec=pygame.image.load('bgf.jpg')


prin=[pygame.image.load('win.jpg'), pygame.image.load('los.jpg'), pygame.image.load('click.jpg'), pygame.image.load('ru.png')]
barr=pygame.image.load('bar.png')

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

screen.blit(bg,(0,0))
screen.blit(bgsec,(513,0))

pygame.draw.rect(screen,(0,0,0),(453,0,60,680))
pygame.draw.rect(screen,(255,255,255),(293,0,2,680))

x = 10
y = 65
mx = 10
my = 10
counter = 0
arc=[0,1,2,3]
arrowcounter= 1
inputuser = [0, 1, 2, 3]
inputcounter = 0
inpucolu = 1
numcounter = 0
boxx = [0, 1, 2, 3]

boxy = [0, 1, 2, 3, 4, 5, 6, 7]
code = randint(1000, 9999)
code1 = str(code)
con = list(code1)

while ((con[0] == con[1]) or (con[0] == con[2]) or (con[0] == con[3]) or (con[1] == con[2]) or (con[1] == con[3]) or (con[2] == con[3])):
    code = randint(1000, 9999)
    code1 = str(code)
    con = list(code1)



arc[0] = int(con[0])
arc[1] = int(con[1])
arc[2] = int(con[2])
arc[3] = int(con[3])

print(arc)

ef printinpu():
    global inputuser
    global arc
    global counter

    screen.blit(num[numcounter-1], (50 + 60*inputcounter-60, 10+80*inpucolu-80))

    if inputcounter>=4 and counter<9:
        screen.blit(arrow, (5, 15 + 81 * counter))

        if inputuser[0] == arc[0]:
            print("X")
            screen.blit(cros,(305 , 15+80*inpucolu-80))
        if inputuser[1] == arc[1]:
            print("X")
            screen.blit(cros, (343 , 15 + 80 * inpucolu - 80))
        if inputuser[2] == arc[2]:
            print("X")
            screen.blit(cros, (383, 15+ 80 * inpucolu - 80))
        if inputuser[3] == arc[3]:
            print("X")
            screen.blit(cros, (421, 15 + 80 * inpucolu - 80))
        if inputuser[0]==arc[1]:
            print("O")
            screen.blit(circ,( 305, 15 + 80 * inpucolu - 80))
        if inputuser[0]==arc[2]:
            print("O")
            screen.blit(circ, (305, 15 + 80 * inpucolu - 80))
        if inputuser[0]==arc[3]:
            print("O")
            screen.blit(circ, (305, 15 + 80 * inpucolu - 80))
        if inputuser[1]==arc[0]:
            print("O")
            screen.blit(circ, (343, 15 + 80 * inpucolu - 80))
        if inputuser[1]==arc[2]:
            print("O")
            screen.blit(circ, (343, 15 + 80 * inpucolu - 80))
        if inputuser[1]==arc[3]:
            print("O")
            screen.blit(circ, (343, 15 + 80 * inpucolu - 80))
        if inputuser[2]==arc[3]:
            print("O")
            screen.blit(circ, (383, 15 + 80 * inpucolu - 80))
        if inputuser[2] == arc[0]:
            print("O")
            screen.blit(circ, (383, 15 + 80 * inpucolu - 80))
        if inputuser[2] == arc[1]:
            print("O")
            screen.blit(circ, (383, 15 + 80 * inpucolu - 80))
        if inputuser[3] == arc[2]:
            print("O")
            screen.blit(circ, (421, 15 + 80 * inpucolu - 80))
        if inputuser[3] == arc[1]:
            print("O")
            screen.blit(circ, (421, 15 + 80 * inpucolu - 80))
        if inputuser[3] == arc[0]:
            print("O")
            screen.blit(circ, (421, 15 + 80 * inpucolu - 80))

def showinpu():
    global arrowcounter
    global inputcounter
    global inpucolu
    global numcounter
    global inputuser
    global counter

    if inputcounter > 3 and counter == arrowcounter:
        inputcounter = 0
        inpucolu = inpucolu + 1
        arrowcounter=arrowcounter+1
        inputuser[inputcounter] = numcounter
        inputcounter = inputcounter + 1

        printinpu()
    elif inputcounter > 3 and counter != arrowcounter:
        print("Wrong step")
        if not counter==23:
            screen.blit(prin[2],(515,160))
            
    else:
        inputuser[inputcounter]=numcounter
        inputcounter=inputcounter+1
        printinpu()

def drawnumber():
    screen.blit(barr,(453,23))

def check():
    global numcounter
    x1, y1 = pygame.mouse.get_pos()
    if (x1>=540 and x<610 and y1>=530 and y1< 548):
        screen.blit(prin[3],(513,0))
    else:
        screen.blit(bgsec,(513,0))

    print ("break")

    if x1>=453 and x1<513:
        if y1>=27 and y1<87:
            print("sucess num 0")
            numcounter=0


        elif y1 >= 88 and y1 < 151:
            print("sucess num 1")
            numcounter = 1
        elif y1 >= 152 and y1< 214:
            print("sucess num 2")
            numcounter = 2
        elif y1>= 215 and y1< 279:
            print("sucess num 3")
            numcounter = 3
        elif y1 >= 280 and y1 < 343:
            print("sucess num 4")
            numcounter = 4
        elif y1 >= 344 and y1 < 407:
            print("sucess num 5")
            numcounter = 5
        elif y1 >= 408 and y1 < 466:
            print("sucess num 6")
            numcounter = 6
        elif y1 >= 467 and y1 < 526:
            print("sucess num 7")
            numcounter = 7
        elif y1 >= 527 and y1 < 581:
            print("sucess num 8")
            numcounter = 8
        elif y1 >= 582 and y1 < 636:
            print("sucess num 9")
            numcounter = 9
        else:
            print("nothing between")
        showinpu()

def arrowf():
    x1, y1 = pygame.mouse.get_pos()
    print(x1,y1)

    if x1 >= 10 and x1 < 40:
        global counter
        if y1 >= 15 and y1 < 45 and counter == 0:
            counter = 1
            screen.blit(bgsec, (513, 0))

        elif y1 >= 96 and y1 < 126 and counter == 1:
            counter = 2
            screen.blit(bgsec, (513, 0))

        elif y1 >= 177 and y1 < 207 and counter == 2:
            counter = 3
            screen.blit(bgsec, (513, 0))

        elif y1 >= 258 and y1 < 288 and counter == 3:
            counter = 4
            screen.blit(bgsec, (513, 0))

        elif y1 >= 339 and y1 < 369 and counter == 4:
            counter = 5
            screen.blit(bgsec, (513, 0))

        elif y1 >= 420 and y1 < 450 and counter == 5:
            counter = 6
            screen.blit(bgsec, (513, 0))

        elif y1 >= 501 and y1 < 531 and counter == 6:
            counter = 7
            screen.blit(bgsec, (513, 0))

        elif y1 >= 582 and y1 < 612 and counter == 7:
            counter = 8
            screen.blit(bgsec, (513, 0))

        else:
            print("nothing")
    else:
        pass

pygame.display.update()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False

        if event.type == pygame.MOUSEBUTTONDOWN:
            check()
            arrowf()
    mx1,my1=pygame.mouse.get_pos()
    drawnumber()
    pygame.display.update()

    if inputuser==arc and inputcounter>3:
        print ('winner')
        counter=23
        screen.blit(prin[0],(520,200))
    if inpucolu == 8 and inputcounter == 4:
        if inputuser == arc and inputcounter > 3:
            print('winner')
            screen.blit(prin[0], (520, 200))
            counter=23

        else:
            screen.blit(prin[1],(520,200))
            print("lost")
            counter=23


print (inputuser)

print(arc)

pygame.quit()





