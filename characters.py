from items import *

#### Base character class
class character:
	def __init__(self, name, prof, hp, action_points, strength, intelligence, inventory, equipped, cover, location, game_over, win):
		self.name = name
		self.prof = prof
		self.hp = 0
		self.action_points = 2
		self.strength = 0
		self.intelligence = 0
		self.inventory = []
		self.equipped = equipped
		self.location = 1 
		self.game_over = False
		self.win = False
	def __str__(self):
		return '\n===================\n{} \nProfession: {}\nHP: {}\nSTR: {}\nEquipped: {}\nLocation: {}'.format(self.name, self.prof, self.hp, self.strength, self.equipped, self.location)


class Soldier(character):
	def __init__(self):
		self.name = ''
		self.prof = 'Soldier'
		self.hp = 12
		self.action_points = 2
		self.strength = 5
		self.intelligence = 3
		self.inventory = [pistol]
		self.equipped = pistol
		self.cover = False
		self.location = 1 
		self.game_over = False
		self.win = False
		#super(Soldier, self).__init__(name = 'name', prof = 'Soldier', hp = 12, strength = 5, intelligence = 3, inventory = [pistol], equipped = pistol, location = 1, game_over = False)


class Pilot(character):
	def __init__(self):
		self.name = ''
		self.prof = 'Pilot'
		self.hp = 10
		self.action_points = 2
		self.strength = 4
		self.intelligence = 4
		self.inventory = [pistol]
		self.equipped = pistol
		self.cover = False
		self.location = 1 
		self.game_over = False
		self.win = False
		#super().__init__(name = '', prof = 'Pilot', hp = 10, strength = 4, intelligence = 4, inventory = [pistol], equipped = pistol, location = 1, game_over = False)

class Scientist(character):
	def __init__(self):
		self.name = ''
		self.prof = 'Scientist'
		self.hp = 8
		self.action_points = 2
		self.strength = 3
		self.intelligence = 5
		self.inventory = [blaster]	
		self.equipped = blaster
		self.cover = False
		self.location = 1 
		self.game_over = False
		self.win = False

player_name = ''
player_prof= ''

