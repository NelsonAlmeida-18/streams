import pygame
import os
import random
import time

pygame.init()

x=450
y = 500
gameOver=False


screen = pygame.display.set_mode([x,y])

owhanaSprite = pygame.image.load('snakeProto (1).png').convert_alpha()
oantSprite = pygame.image.load('snakeProto.png').convert_alpha()
macDonnaldbackground = pygame.image.load('background.jpg').convert_alpha()
blankPng = pygame.image.load('blank.png')

r = True
while r:  
##score vai ser o length do oant  
	score=0
	background = pygame.transform.scale(macDonnaldbackground, (x,y))
	screen.blit(background,(0,0))
##GameOverBackground
	GameOverBackground=pygame.image.load('gameover.jpg').convert_alpha()
	GameOverBackground=pygame.transform.scale(GameOverBackground,(x,y))
##Score
	blue = (0, 0, 128)
	font = pygame.font.SysFont("comicsansms", 20)
	text = font.render('Vezes que o Oant encabou a Oana'+str(score), True, blue)
	screen.blit(text,(10,10))
#####Nitrox
	fontNitrox= pygame.font.SysFont("comicsansms", 40)
	red=(255,0,0)
##########Hamburguers
	hamburguerSprite = pygame.image.load('hamburguer.png.png').convert_alpha()
	posBurguerX=random.randrange(10,440,10)
	posBurguerY=random.randrange(10,440,10)
	hamburguerSprite=pygame.transform.scale(hamburguerSprite,(60,60))
######Castrol
	castrolLevel = 0
	fullLifeSprite = pygame.image.load('healthbarProto (5).png').convert_alpha()
	fullLifeSprite=pygame.transform.scale(fullLifeSprite,(100,40))
	fsthitSprite=pygame.image.load('healthbarProto (4).png').convert_alpha()
	fsthitSprite=pygame.transform.scale(fsthitSprite,(100,40))
	sndhitSprite=pygame.image.load('healthbarProto (3).png').convert_alpha()
	sndhitSprite=pygame.transform.scale(sndhitSprite,(100,40))
	rdhitSprite=pygame.image.load('healthbarProto (2).png').convert_alpha()
	rdhitSprite=pygame.transform.scale(rdhitSprite,(100,40))
	fourthhitSprite=pygame.image.load('healthbarProto (1).png').convert_alpha()
	fourthhitSprite=pygame.transform.scale(fourthhitSprite,(100,40))
	dead=pygame.image.load('healthbarProto.png').convert_alpha()
	dead=pygame.transform.scale(dead,(100,40))
	posXCastrol = 5
	posYCastrol=440
###########oWHANA################################
	posXOwhana = random.randrange(10,440,10)
	posYOwhana = random.randrange(10,440,10)	
	owhanaSprite = pygame.transform.scale(owhanaSprite, (80,80)) 
###########Woant################################
	posXOant=0
	posYOant=0
	yoantSprite = pygame.transform.scale(oantSprite, (70,65))
###########Movimento#################################
	pygame.display.flip()
	nitrado=False
	nitro=0
	boost=10
	speedX=0
	speedY=0
	loopsSinceBoost=0
	while gameOver==False:
		if(nitro!=0):
			loopsSinceBoost+=1
		if(loopsSinceBoost==40):
			nitro=0
			loopsSinceBoost=0
			nitrado=False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				r = False
				gameOver=True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					speedX=-(boost+nitro)
					speedY=0
				elif event.key == pygame.K_RIGHT:
					speedX=boost+nitro
					speedY=0
				elif event.key == pygame.K_UP:
					speedY=-(boost+nitro)
					speedX=0
				elif event.key == pygame.K_DOWN:
					speedY=boost+nitro
					speedX=0
			if((posXOant<=(posXOwhana+10) and posXOant >=(posXOwhana-10)) and (posYOant<=(posYOwhana+10) and posYOant >=(posYOwhana-10))):
				print("Comeram-se, Wuant engordou substancialmente")
				posXOwhana = random.randrange(0,450,10)
				posYOwhana = random.randrange(0,450,10)
				score+=1 
			if((posXOant<=(posBurguerX+10) and posXOant >=(posBurguerX-10)) and (posYOant<=(posBurguerY+10) and posYOant >=(posBurguerY-10))):
				castrolLevel+=1
				posBurguerX=random.randrange(10,440,10)
				posBurguerY=random.randrange(10,440,10)
				print("Owant está engordando")			
##Rever esta parte das boundaries
			if(posXOant<0):
				posXOant=450
				speedY=0
				speedX=-(boost+nitro)
			elif(posXOant>450):
				posXOant=0
				speedY=0
				speedX=boost+nitro
			elif(posYOant>450):
				posYOant=0
				speedX=0
				speedY=boost+nitro
			elif(posYOant<0):
				posYOant=450
				speedX=0
				speedY=-(boost+nitro)
		posXOant+=speedX
		posYOant+=speedY
		screen.blit(background,(0,0))
		screen.blit(owhanaSprite,(posXOwhana, posYOwhana))
		screen.blit(yoantSprite,(posXOant,posYOant))
		screen.blit(hamburguerSprite,(posBurguerX,posBurguerY))
		
		if(castrolLevel==0):
			screen.blit(fullLifeSprite,(posXCastrol,posYCastrol))
			posHamburguerX=random
		elif(castrolLevel==1):
			screen.blit(fsthitSprite,(posXCastrol,posYCastrol))
		elif(castrolLevel==2):
			screen.blit(sndhitSprite,(posXCastrol,posYCastrol))
		elif(castrolLevel==3):
			screen.blit(rdhitSprite, (posXCastrol,posYCastrol))
		elif(castrolLevel==4):
			screen.blit(fourthhitSprite,(posXCastrol,posYCastrol))
		elif(castrolLevel==5):
			screen.blit(dead,(posXCastrol,posYCastrol))
		elif(castrolLevel==6):
			screen.blit(GameOverBackground,(0,0))
			r=False
			gameOver=True

		text = font.render('Vezes que o Oant encabou a Oana: '+str(score), True, blue)
		screen.blit(text,(20,20))
###Nitrinho
		if(nitrado==False):
			probs=0
			probs=random.randrange(1,200)
			if(probs==2):
					nitrinho = fontNitrox.render('Nitrox time, sigura-te Zé!!!', True, red)
					screen.blit(nitrinho,(50,250))
					pygame.display.update()
					time.sleep(3)
					nitro+=20
					nitrado=True
		pygame.display.update()
		time.sleep(0.1)

pygame.quit()