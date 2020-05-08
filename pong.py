import pygame
import time
import random
from paddle import Paddle
from ball import Ball

pygame.init()


dis_width=800
dis_height=600


white=(255,255,255)
blue= (0,0,255)
red=(255,0,0)
black=(0,0,0)

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption('Pong')

paddleA = Paddle(white, 10, 110)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(white, 10, 110)
paddleB.rect.x = 770
paddleB.rect.y = 200

ball = Ball(white,10,10)
ball.rect.x= 345
ball.rect.y= 195



#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
# Add the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)



def game_loop():
	game_close= False
	clock=pygame.time.Clock()
	ScoreA=0
	ScoreB=0

	while  not game_close:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_close= True
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			paddleA.moveUp(5)
		if keys[pygame.K_s]:
			paddleA.moveDown(5)
		if keys[pygame.K_UP]:
			paddleB.moveUp(5)
		if keys[pygame.K_DOWN]:
			paddleB.moveDown(5)

		all_sprites_list.update()

		if ball.rect.x >= 790:
			ball.velocity[0] = -ball.velocity[0]
			ScoreA+=1
		if ball.rect.x <=10:
			ball.velocity[0] = -ball.velocity[0]
			ScoreB+=1
		if ball.rect.y >= 590:
			ball.velocity[1] = -ball.velocity[1]
		if ball.rect.y < 0:
			ball.velocity[1] = -ball.velocity[1]

		if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
			ball.bounce()

		dis.fill(black)

		pygame.draw.rect(dis,white,[0,0,dis_width-1,dis_height],5)  # Draw the edge
		pygame.draw.line(dis,white,[dis_width/2,0],[dis_width/2,dis_height],1) # Draw the mid net

		all_sprites_list.draw(dis)

		font = pygame.font.Font(None, 50)
		text = font.render(str(ScoreA), 1, white)
		dis.blit(text, (200,10))
		text = font.render(str(ScoreB), 1, white)
		dis.blit(text, (600,10))

		pygame.display.flip()

		clock.tick(60)
	pygame.quit()


game_loop()
