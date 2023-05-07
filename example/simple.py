# example code by cool-dev-guy for simple pygame.
from python import pygame # in codon you can only import python modules like this
pygame.init()  
screen = pygame.display.set_mode((400,500),pygame.OPENGL)  # use pygame.OPENGL if you want opengl or experience multiple windows issue.
done = False  
      
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()
#Result is a blank black window
