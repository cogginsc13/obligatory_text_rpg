from characters import *

#### Base class for all items
class item:
	def __init__(self, name, description):
		self.name = name
		self.description = description
	def __str__(self):
		return '\n============\n{}\n{}'.format(self.name, self.description)
#### Weapon Class Super
class Weapon(item):
	def __init__(self, name, description, hit_range, damage, damage_type):
		self.hit_range = hit_range
		self.damage = damage
		self.damage_type = damage_type
		super().__init__(name, description)

	def __str__(self):
		return '\n{}\n     {}\n     Damage: {}'.format(self.name, self.description, self.damage)

#### Reusable (Equipped) Items
class Pistol(Weapon):
	def __init__(self):
		super().__init__(name = 'Pistol',
						 description = 'A standard issue pistol.',
						 hit_range = [4,5,6],
						 damage = 2,
						 damage_type = 'physical')
class Blaster(Weapon):
	def __init__(self):
		super().__init__(name = 'Blaster',
						 description = 'A standard issue blaster',
						 hit_range = [4,5,6],
						 damage = 2,
						 damage_type = 'energy')
pistol = Pistol()
blaster = Blaster()