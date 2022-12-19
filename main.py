import pygame as pg
from player import Player
from voxel_render import VoxelRender

RES = WIDTH, HEIGHT = 800, 450

class App:
	def __init__(self):
		self.res = self.width, self.height = RES
		self.screen = pg.display.set_mode(RES, pg.SCALED)
		self.clock = pg.time.Clock()
		self.player = Player()
		self.voxel_render = VoxelRender(self)

	def update(self):
		self.player.update()
		self.voxel_render.update()

	def draw(self):
		self.voxel_render.draw()
		pg.display.flip()

	def run(self):
		while True:
			self.update()
			self.draw()
			
			[exit() for event in pg.event.get() if event.type == pg.QUIT]
			self.clock.tick(60)
			pg.display.set_caption(f'FPS: {self.clock.get_fps()}')


if __name__ == '__main__':
	app = App()
	app.run()
