from pygame import *

init()
screen = display.set_mode((0, 0), FULLSCREEN)

running = True
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
	"""
	screen.fill((0, 0, 0))
	for i in range(99):
		draw.circle(screen, (255, 255, 255, 0), (mx, my), i)
	"""
	rect = draw.rect(screen, (255, 255, 255), (1000, 700, 700, 300), 2)
	if rect.collidepoint(mx, my):
		draw.line(screen, (255, 255, 255, ))

	display.flip()
quit()
