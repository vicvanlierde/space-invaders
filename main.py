import math
import pygame
import random
pygame.init()

running = True
playerX, playerY = 336, 510
playerX_change = 0

frame = pygame.display.set_mode((800, 600))
achtergrond = pygame.image.load('img/background.jpg')
player = pygame.image.load('img/player.png')

pygame.display.set_caption("Space Invaders")

while running:
  frame.blit(achtergrond, (0,0))
  for events in pygame.event.get():
    if events.type == pygame.QUIT:
      running = False
    if events.type == pygame.KEYDOWN:
      if events.key == pygame.K_q:
        playerX_change = -2
      if events.key == pygame.K_d:
        playerX_change = 2
    if events.type == pygame.KEYUP:
      if events.key == pygame.K_q:
        playerX_change = 0
      if events.key == pygame.K_q:
        playerX_change = 0

  playerX += playerX_change
  if playerX > 736:
    playerX = 736
  elif playerX < 0:
    playerX = 0
    
  frame.blit(player, (playerX,playerY))
  pygame.display.update()