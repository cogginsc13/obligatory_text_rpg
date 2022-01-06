import random

class enemy:
	def __init__(self, name, hp, hit_range, attacks):
		self.name = name
		self.hp = hp
		self.hit_range = hit_range
		self.attacks = attacks
	def is_alive(self):
		return self.hp > 0
	def __str__(self):
		return '\n============\n{} \nhp = {}\nstrength = {}\n'.format(self.name, self.hp, self.hit_range)

class Cyborg(enemy):
	def __init__(self):
		super(Cyborg, self).__init__(name = 'Cyborg', hp = 5, hit_range = [5,6], attacks = 2)

class BattleDrone(enemy):
        def __init__(self):
                super(BattleDrone, self).__init__(name = 'Battle Drone', hp = 3, hit_range = [4,5,6], attacks = 1)

class CyberPunk(enemy):
        def __init__(self):
                super(CyberPunk, self).__init__(name = 'CyberPunk', hp = 3, hit_range = [5,6], attacks = 1)


class SpacePirate(enemy):
        def __init__(self):
                super(SpacePirate, self).__init__(name = 'Space Pirate', hp = 2, hit_range = [3,4,5,6], attacks = 2)

class AutoTurret(enemy):
        def __init__(self):
                super(AutoTurret, self).__init__(name = 'Auto Turret', hp = 7, hit_range = [5,6], attacks = 4)

cyborg = Cyborg()
battle_drone = BattleDrone()
cyber_punk = CyberPunk()
space_pirate = SpacePirate()
auto_turret = AutoTurret()

baddies = [cyborg, battle_drone, cyber_punk, space_pirate, auto_turret]
