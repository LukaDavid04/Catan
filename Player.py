from random import *


class Player:
	def __init__(self, name, colour, brick_total, ore_total, wood_total, sheep_total, grain_total, victory_points):
		self.name = name
		self.colour = colour
		self.brick = brick_total
		self.ore = ore_total
		self.sheep = sheep_total
		self.grain = grain_total
		self.wood = wood_total
		self.v_points = victory_points

	def get_brick(self, Bank, num):
		self.brick += num
		Bank.brick -= num

	def get_ore(self, Bank, num):
		self.ore += num
		Bank.ore -= num

	def get_wood(self, Bank, num):
		self.wood += num
		Bank.wood -= num

	def get_sheep(self, Bank, num):
		self.sheep += num
		Bank.sheep -= num

	def get_grain(self, Bank, num):
		self.grain += num
		Bank.grain -= num

	def items(self):
		print("Bricks: " + str(self.brick) + " Ore: " + str(self.ore) + " Wood: " + str(self.wood) + " Sheep: " + str(
			self.sheep) + " Grain: " + str(self.grain))


class Board:
	def __init__(self, tiles):
		self.tiles = tiles
		shuffle(tiles)

	def print(self):
		print(self.tiles)

	def at(self, n):
		return self.tiles[n]


class Bank:
	def __init__(self, brick=19, ore=19, wood=19, sheep=19, grain=19):
		self.brick = brick
		self.ore = ore
		self.wood = wood
		self.sheep = sheep
		self.grain = grain

	def total(self):
		print("Bricks: " + str(self.brick) + " Ore: " + str(self.ore) + " Wood: " + str(self.wood) + " Sheep: " + str(
			self.sheep) + " Grain: " + str(self.grain))


class House:
	def __init__(self, level, type, colour):
		self.level = level
		self.type = type
		self.colour = colour

	def print(self):
		print('Level: ' + str(self.level) + ' Type: ' + str(self.type) + ' Colour: ' + str(self.colour))


def roll_dice():
	x = randint(1, 6)
	y = randint(1, 6)
	return x + y
