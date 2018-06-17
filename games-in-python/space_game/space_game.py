#########################################################
#				  The Space Showdown					#
#                ---------------------					#
#			 created by Omair and Shayan				#
#														#
# STORY													#
# Scientists on Earth created a new technology, but		#
# things went wrong when someone hacked the system and  #
# bombers from another planet arrived and started		#
# attacking the Earth - and the whole universe.
# 
#														#
#														#
# GOAL													#
# ----													#
# You play Cyber, a space ranger whose job it is to		#
# destroy the bombers and make sure they don't hit her  #
# ships.												#
# 														#
#														#
#														#
# CONTROLS												#			
# ---------												#
# W to go up											#
# S to go down											#
# D to go right											#
# A to go left											#			
#														#
#														#
#########################################################


#1 Import library
import pygame
import random
import math
from pygame.locals import *

clock=pygame.time.Clock()

#2 Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [200,100]
badtimer = 100
badtimer1=0
badguys=[[640,100]]
healthvalue=194
acc=[0,0]
lasers=[]
#pygame.mixer.init()


#3 Load images
player = pygame.image.load("resources/images/cyber.png")
spacebg = pygame.image.load("resources/images/spacebg.png")
ship = pygame.image.load("resources/images/ship.png")
bomberimg1 = pygame.image.load("resources/images/bomber.png")
bomberimg = bomberimg1
laser = pygame.image.load("resources/images/bullet.png")

#3.1 Load sound effects
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)



gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")

#4 Keep looping through
running = 1
exitcode = 0
while running:
	clock.tick(24.0)
	badtimer-=1
	#5Clear the screen before drawing it again
	screen.fill(0)
	#6Draw the screen elements
	for x in range(width/spacebg.get_width()+1):
		for y in range(height/spacebg.get_height()+1):
			screen.blit(spacebg,(x*100, y*100)) 				
	screen.blit(ship,(0,135))				# Earth ship 2
	position = pygame.mouse.get_pos()
	angle = math.atan2(position[1]-(playerpos[1]+32), position[0]-(playerpos[0]+26))
	playerrot = pygame.transform.rotate(player, 360-angle*57.29)
	playerpos1 = (playerpos[0] - playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
	screen.blit(playerrot, playerpos1)			# The space ranger, Cyber
	#Draw bullets
	for bullet in lasers:
		index=0
		velx=math.cos(bullet[0])*10
		vely=math.sin(bullet[0])*10
		bullet[1]+=velx
		bullet[2]+=vely
		if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
			lasers.pop(index)
		index+=1
		for projectile in lasers:
			laser1 = pygame.transform.rotate(laser, 360-projectile[0]*57.29)
			screen.blit(laser1, (projectile[1], projectile[2]))
	if badtimer==0:
		badguys.append([640,random.randint(50,430)])
		badtimer=100-(badtimer1*2)
		if badtimer1>=35:
			badtimer1=35
		else:
			badtimer1+=5
	index=0
	for badguy in badguys:
		if badguy[0]<-64:
			badguys.pop(index)
		badguy[0]-=7

		badrect=pygame.Rect(bomberimg.get_rect())
		badrect.top=badguy[1]
		badrect.left=badguy[0]
		if badrect.left<64:
			hit.play()
			healthvalue -= random.randint(5,20)
			badguys.pop(index)

	index1=0
	for bullet in lasers:
		bullrect = pygame.Rect(laser.get_rect())
		bullrect.left=bullet[1]
		bullrect.top=bullet[2]
		if badrect.colliderect(bullrect):
			enemy.play()
			acc[0]+=1
			badguys.pop(index)
			lasers.pop(index1)
		index+=1

		index+=1
	for badguy in badguys:
		screen.blit(bomberimg, badguy)
			
	#6.4Health bar
	font = pygame.font.Font(None, 24)
	survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
	textRect = survivedtext.get_rect()
	textRect.topright=[635,5]
	screen.blit(survivedtext, textRect)

	healthbar = pygame.image.load("resources/images/healthbar.png")
	health = pygame.image.load("resources/images/health.png")

	screen.blit(healthbar, (5,5))
	for health1 in range(healthvalue):
		screen.blit(health, (health1+8,8))
 
	# Pull up the screen with all these updated elements on it
	pygame.display.flip()	


	#7Loop through the events
	for event in pygame.event.get():
		#8check if the event is the x button
		if event.type==pygame.QUIT:
			#if it is quit the game
			pygame.quit()
			exit(0)

		#8.2 Key pressed?
		if event.type == pygame.KEYDOWN:
			if event.key==K_w:
				keys[0]=True
			elif event.key==K_a:
				keys[1]=True
			elif event.key==K_s:
				keys[2]=True
			elif event.key==K_d:
				keys[3]=True
		if event.type == pygame.KEYUP:
			if event.key==pygame.K_w:
				keys[0]=False
			elif event.key==pygame.K_a:
				keys[1]=False
			elif event.key==pygame.K_s:
				keys[2]=False
			elif event.key==pygame.K_d:
				keys[3]=False

		#8.3 Shoot!
		if event.type==pygame.MOUSEBUTTONDOWN:
			shoot.play()
			position=pygame.mouse.get_pos()
			acc[1]+=1
			lasers.append([math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])


	# 9 - Move Cyber
	if keys[0]:
		playerpos[1]-=5
	elif keys[2]:
		playerpos[1]+=5
	if keys[1]:
		playerpos[0]-=5
	elif keys[3]:
		playerpos[0]+=5

    #10 - Win/Lose check
	if pygame.time.get_ticks()>=90000:
		running=0
		exitcode=1
	if healthvalue<=0:
		running=0
		exitcode=0
	if acc[1]!=0:
		accuracy=acc[0]*1.0/acc[1]*100
	else:
		accuracy=0
# 11 - Win/lose display        
if exitcode==0:
	pygame.font.init()
	font = pygame.font.Font(None, 24)
	text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
	textRect = text.get_rect()
	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery+24
	screen.blit(gameover, (0,0))
	screen.blit(text, textRect)
else:
	pygame.font.init()
	font = pygame.font.Font(None, 24)
	text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
	textRect = text.get_rect()
	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery+24
	screen.blit(youwin, (0,0))
	screen.blit(text, textRect)
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
	pygame.display.flip()
