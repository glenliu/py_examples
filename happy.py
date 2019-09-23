#coding:utf-8
import pygame
import sys
from sys import exit
from pygame.locals import QUIT
#初始化pygame环境
pygame.init()
pygame.font.init()

#创建一个长宽分别为480/650窗口
screen = pygame.display.set_mode((1400, 800))
# screen.fill((255,255,255))

#设置窗口标题
pygame.display.set_caption("Happy Birthday")
bg=pygame.image.load("images/bg1.png")
cr=pygame.image.load("images/crown.png")
screen.blit(bg,(0,0))

def handleEvent():
	for e in pygame.event.get():
		if e.type == QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
			pygame.quit()
			sys.exit()
		if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
			if pygame.font:
				font = pygame.font.Font(None, 36)
				text = font.render("Happy Birthday", 1, (10, 10, 10))
				textpos = text.get_rect(centerx=screen.get_width()/2)
				screen.blit(text, textpos)
				#screen.blit("Happy",(50,50))
		if e.type == pygame.KEYDOWN and e.key == pygame.K_c:
			screen.blit(cr,(632,20))
while True:


	# 更新屏幕内容
	pygame.display.update()
	#处理关闭游戏
	handleEvent()
