#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
#import pyglet
import random
#import time
#from playsound import playsound
pygame.init()
win = pygame.display.set_mode((1024,600))
pygame.display.set_caption("Andrew simulator")

walkRight = [pygame.image.load('right_1.png'),pygame.image.load('right_2.png'),pygame.image.load('right_3.png')]
walkLeft = [pygame.image.load('left_1.png'),pygame.image.load('left_2.png'),pygame.image.load('left_3.png')]
swimRight = [pygame.image.load('swim_right_1.png'),pygame.image.load('swim_right_2.png'),pygame.image.load('swim_right_3.png')]
swimLeft = [pygame.image.load('swim_left_1.png'),pygame.image.load('swim_left_2.png'),pygame.image.load('swim_left_3.png')]
playerStand = pygame.image.load('idle.png')
playerStandRight = pygame.image.load('idleRight.png')
playerStandSwimLeft = pygame.image.load('idle_swim_left.png')
playerStandSwimRight = pygame.image.load('idle_swim_right.png')
bulletWord = pygame.image.load('bulletWord.png')
bulletWordLeft = pygame.image.load('bulletWordLeft.png')
bg = pygame.image.load('background.jpg')
bg2 = pygame.image.load('background2.jpg')
bg3 = pygame.image.load('background3.jpg')
bg4 = pygame.image.load('background4.jpg')
sale1 = pygame.image.load('sale.png')
badAndrew = pygame.image.load('badAndrew.png')
boom = pygame.image.load('boom.png')
clock = pygame.time.Clock()
x = 50
y = 330
width = 248
height = 253
speed = 5
isJump = False
jumpCount = 10
left = False
right = False
animCount = 0
lastMove = "right"
lastDirectionShot = "right"
switchscreen = 0
saleJump = 0
#music = pygame.mixer.music.load('test.mp3')
randomX = 0
saleHight = 50
#pygame.mixer.music.play(-1)
score = 0
crash = 0
crash2 = 0
f1 = pygame.font.Font(None, 50)
class Bandit():
    def __init__(self, x, y, direct):
        self.x = x
        self.y = y
        self.direct = direct
        # speed
        self.speed = 4 * direct

    def drawLeft(self, win):

        win.blit(badAndrew, (self.x, self.y))

class Boom():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Appear(self, win):

        win.blit(boom, (self.x, self.y))



class Sale():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def Appear(self, win):
        win.blit(sale1, (self.x, self.y))
class snaryad():
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
#speed
        self.vel = 8 * facing
    def drawRight(self, win):
#bullet
            win.blit(bulletWord, (self.x, self.y))


    def drawLeft(self, win):
# bullet
        win.blit(bulletWordLeft, (self.x - 300, self.y))

def drawWindow():
    global animCount, switchscreen, x ,y, playerStandRight, playerStand, walkRight, walkLeft, swimLeft, swimRight

    text1 = f1.render(str(score), 1, (0, 0, 0))
    win.blit(text1, (100, 100))

    if x == 680:
        switchscreen += 1
        for extraSale in extraSales:
            extraSales.pop(extraSales.index(extraSale))
        for extraBandit in extraBandits:
            extraBandits.pop(extraBandits.index(extraBandit))
    if switchscreen == 0:
        win.blit(bg, (0, 0))
        text1 = f1.render('Score:' + str(score), 1, (255, 255, 255))
        if x == 680:
            x = 5

    elif switchscreen == 1:
        win.blit(bg2, (0, 0))
        text1 = f1.render('Score:' + str(score), 1, (0, 0, 0))
        if x == 680:
            x = 5
    elif switchscreen == 2:
        if x == 680:
            x = 5
        win.blit(bg3, (0, 0))
        text1 = f1.render('Score:' + str(score), 1, (0, 0, 0))
    else:
        win.blit(bg4, (0, 0))
        walkLeft = swimLeft
        walkRight = swimRight
        playerStand = playerStandSwimLeft
        playerStandRight = playerStandSwimRight
        text1 = f1.render('Score:' + str(score), 1, (0, 0, 0))
# Kolichestvo kadrov
    if animCount + 1 >= 15:
        animCount = 0
    if left:
# okruglenie do menshego
        win.blit(walkLeft[animCount // 5], (x,y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x,y))
        animCount += 1
    else:
        if lastMove == "left":
            win.blit(playerStand, (x,y))
        else:
            win.blit(playerStandRight, (x,y))
    for bullet in bullets:
        if lastDirectionShot == "left":
            bullet.drawLeft(win)
        else:
            bullet.drawRight(win)
    for extraSale in extraSales:
        extraSale.Appear(win)
    for extraBandit in extraBandits:
        extraBandit.drawLeft(win)
    for extraboom in extrabooms:
        extraboom.Appear(win)
    win.blit(text1, (100, 20))
    pygame.display.update()
run = True
bullets = []
extraSales = []
extraBandits = []
extrabooms = []
while run:
# Kolichestvo kadrov
    clock.tick(300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             run = False


    for extraSale in extraSales:
        if saleJump == 0:
            extraSale.y += 1
            if extraSale.y == saleHight + 200:
                saleJump = 1
        else:
            extraSale.y -= 1
            if extraSale.y == saleHight - 200:
                saleJump = 0
    if len(extraSales) < 2:
        randomX = random.uniform(20, 700)
        extraSales.append(Sale(randomX, saleHight))
    for extraSale in  extraSales:
        if ((x + 80 > extraSale.x) and (x-80 < extraSale.x)) and ((y + 80 > extraSale.y) and (y-80 < extraSale.y)):
            extraSales.pop(extraSales.index(extraSale))
            score +=1
    for extraBandit in extraBandits:
        if crash == 1 and extraBandit.x < 700:
            for extraboom in extrabooms:
                extrabooms.pop(extrabooms.index(extraboom))
#polet puli
    for bullet in bullets:
        if bullet.x < 1024 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    for extraBandit in extraBandits:
        if extraBandit.x < (1024 + 450) and extraBandit.x > -450:
            extraBandit.x += extraBandit.speed
        else:
            extraBandits.pop(extraBandits.index(extraBandit))
    if len(extraBandits) < 1:
        extraBandits.append(Bandit(770, 330, -1))

    #crash Bullet and car
    for extraBandit in extraBandits:
        for bullet in bullets:
            if ((extraBandit.x > (bullet.x - 100)) and (extraBandit.x < (bullet.x + 100))) and ((extraBandit.y > (bullet.y - 100)) and (extraBandit.y < (bullet.y + 100))):
                score += 10
                extraBandits.pop(extraBandits.index(extraBandit))
                bullets.pop(bullets.index(bullet))
                extrabooms.append(Boom(extraBandit.x, extraBandit.y - 80))
                crash = 1

    #Crash Andrewa and car
    for extraBandit in extraBandits:
        if ((x > (extraBandit.x - 20)) and (x < (extraBandit.x + 20))) and ((y > (extraBandit.y - 100)) and (y < (extraBandit.y + 100))):
            score -= 10
            extraBandits.pop(extraBandits.index(extraBandit))
            extrabooms.append(Boom(extraBandit.x, extraBandit.y - 80))
            crash = 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:

        lastDirectionShot = lastMove
        if lastMove == "right":
            facing = 1
        else:
            facing = -1
        if len(bullets) < 1:
           bullets.append(snaryad(int(round(x + width // 2)), int(round(y - 20)), facing ))
    if keys[pygame.K_LEFT] and x>5:
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x<1024-width-5:
        x += speed
        right = True
        left = False
        lastMove = "right"

    else:

        left = False
        right = False
        animCount = 0
    if not(isJump):

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount**2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()