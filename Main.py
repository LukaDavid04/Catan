# Brick, Ore, Wood, Sheep, Grain
from Player import *
from random import *
from pygame import *
import ctypes

init()
font.init()
StartFont = font.SysFont('Georgia', 70)
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
screen = display.set_mode((0, 0), FULLSCREEN)
screen_rect = screen.get_rect()

menu_cover = image.load('Pics/main_cover.jpg')
size = menu_cover.get_rect().size
ratio = size[0]/size[1]
new_w = ratio * screensize[1]
menu_cover = transform.scale(menu_cover, (int(new_w), screensize[1]))
logo = image.load('Pics/logo.png')

Orange = (186, 100, 53)
Yellow = (239, 173, 2)
White = (255, 255, 255)
Black = (0, 0, 0)

Bank = Bank(19, 19, 19, 19, 19)
Luka = Player('Luka', 'Green', 0, 0, 0, 0, 0, 0)
Liz = Player('Liz', 'White', 0, 0, 0, 0, 0, 0)
Hope = Player('Hope', 'Blue', 0, 0, 0, 0, 0, 0)
Matt = Player('Matt', 'Red', 0, 0, 0, 0, 0, 0)
Players = [Luka, Liz, Hope, Matt]
Board = Board([-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4])
Row0 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
Row1 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
Row2 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
Row3 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
Row4 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
Rows = [Row0, Row1, Row2, Row3, Row4]
shuffle(Players)
Board.print()
Row0[0][5] = House(1, Board.at(0), 'Green')

running = True
mode = 'Menu'
tikTok = time.Clock()

while running:
	click = False
	for evt in event.get():
		if evt.type == MOUSEBUTTONDOWN:
			if evt.button == 1:
				click = True
		# if evt.button == 4: 'Scroll'
		if evt.type == KEYDOWN:
			if evt.key == K_ESCAPE:
				running = False
		if evt.type == QUIT:
			running = False
	mx, my = mouse.get_pos()
	mb = mouse.get_pressed()

	if mode == 'Menu':
		screen.blit(menu_cover, (screensize[0]/2 + screensize[0]/2 - new_w/2, screensize[1]/2))
		screen.blit(logo, (850, 500))
		start = Surface((420, 130), SRCALPHA)
		startRect = Rect(1150, 1140, 420, 130)
		screen.blit(start, (1150, 1140))
		border = draw.lines(screen, Orange, True, [(1150, 1140), (1570, 1140), (1570, 1270), (1150, 1270)], 2)
		play = StartFont.render("Start Game", True, (248, 188, 88))
		screen.blit(play, (1200, 1160))
		if startRect.collidepoint(mx, my):
			start.fill((227, 180, 70, 40))
			screen.blit(start, (1150, 1140))
			if click:
				mode = 'Board'
		else:
			start.fill((227, 180, 70, 60))
			screen.blit(start, (1150, 1140))
			play = StartFont.render("Start Game", True, Orange)
			screen.blit(play, (1200, 1160))

	if mode == 'Board':
		screen.fill(Black)
	display.flip()
quit()
