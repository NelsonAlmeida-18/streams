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
##Score
	blue = (0, 0, 128)
	font = pygame.font.SysFont("comicsansms", 30)
	text = font.render('Vezes que o Oant encabou a Oana'+str(score), True, blue)
	screen.blit(text,(20,20))
#####Nitrox
	fontNitrox= pygame.font.SysFont("comicsansms", 40)
	red=(255,0,0)
###########oWHANA################################
	posXOwhana = random.randrange(40,410,10)
	posYOwhana = random.randrange(40,460,10)	
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
				posXOwhana = random.randrange(40,410,10)
				posYOwhana = random.randrange(40,460,10)
				score+=1 			
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