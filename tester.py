#Escape the space station game
#import

import cmd
import textwrap
import sys
import os
import time
import random
from characters import *
from enemies import *
from items import *
from rooms import *

screen_width = 100

#Title Screen
def title_screen():
	os.system('cls')
	print('#################################')
	print('##### ESCAPE THE STATION ########')
	print('#################################')
	print('        -[P]LAY-                   ')
	print('        -[H]ELP-                   ')
	print('        -[QUIT]-                   ')
	title_screen_selections()

def title_screen_selections():
	option = input().lower()
	if option == 'p':
		setup_game()
	elif option == 'h':
		help_menu()
	elif option == 'quit':
		os.system('cls')
		sys.exit()
	elif option not in ['play','help','quit']:
		input('Please select an item from the menu')
		title_screen()
			
def help_menu():
	print("Put the rules in here")
	finished = input('Press Enter to return to the menu.')
	if finished != 0:
		title_screen()

def setup_game():
	os.system('cls')
	question1 = "Hello, what is your name?\n"
	for character in question1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.0)
	name = input()
	choose_class(name)
	
def choose_class(name):	
	question2= "Hello, {}, what is your profession?\n".format(name)
	question2add = "Choose between: [S]oldier, S[c]ientist, or [P]ilot.\n"
	for character in question2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.0)
	for character in question2add:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.0)

	player_prof = input().lower()
	if player_prof == 's':
		player = Soldier()
		player.name = name
	elif player_prof == 'c':
		player = Scientist()
		player.name = name
	elif player_prof == 'p':
		player = Pilot()
		player.name = name
	elif player_prof not in ['s', 'c', 'p']:
		input('Please select a valid option')
		choose_class(name)
	welcome(player)

def welcome(player):
	os.system('cls')			
	welcome1 = 'Welcome, {}, you are now a {}!\n'.format(player.name, player.prof)
	for character in welcome1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.0)
	input('>')	
	start_game(player)

def start_game(player):
	speech1 = "The Station has been your home for as long as you remember\n"
	speech2 = "But there have been whispers of troubles recently...\n"
	speech3 = "For one reason or another, you'll need to ESCAPE THE STATION!\n"
	for character in speech1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.0)
	for character in speech2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.0)
	for character in speech3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.0)
	time.sleep(.0)
	input('\nPress "Enter" to continue')
	main_game_loop(player)

def main_game_loop(player):
	while player.game_over is False:
		room_prompt(player)
		if player.game_over == True:
			print('You Died')
			input()
		if player.win == True:
			print('You Did It!')

#Game interactivity
def room_prompt(player):
	os.system('cls')
	if ROOMS[player.location]['BADDIE'] == True:
		baddie = random.choice(baddies)
		if baddie.hp > 0:
			room1 = 'You have arrived in the {}.\n'.format(ROOMS[player.location]['ROOM_NAME'])
			room2 = '{}.'.format(ROOMS[player.location]['DESCRIPTION'])
			for character in room1:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.0)
			for character in room2:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.0)
			input('\n>')
			combat1 = 'You ran into a {}!\n'.format(baddie.name)
			for character in combat1:
				sys.stdout.write(character)
				sys.stdout.flush()			
				time.sleep(0.0)
			combat(player, baddie)

	elif ROOMS[player.location]['BADDIE'] == False:
		room1 = '\nThe room seems empty.'
		for character in room1:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.0)
		print('\n' + '=====================================')
		room2 = 'What would you like to do?'
		for character in room2:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.0)
		print('\n- [M]ove On -')
		print('-  [S]earch -')
		print('-  [E]quip  -')
		print('-  [Quit]   -')
		action = input().lower()
		acceptable_actions = ['s', 'm','e','quit',]
		#while action not in acceptable_actions:
		#	print('Please select an option from the list')
		if action == 'quit':
			os.system('cls')
			sys.exit()
		elif action == 'm':
			del ROOMS[player.location]
			next_room(player)
		elif action == 's':
			room_search()
		elif action == 'e':
			equip()
	else:
		input('Please select a valid option')
		room_prompt(player)

def combat(player, baddie):
	if player.action_points == 0:
		enemy_atk(baddie, player, baddie.hit_range, baddie.attacks)
	if player.hp > 0 and baddie.hp > 0:
		print('\n(A)ttack')
		print('(T)ake Cover')
		print('(C)harge')
		cmd = input("\nIt's your move:").lower()
		if cmd == 'a':
			atk(player, baddie, player.equipped)
		elif cmd == 't':
			take_cover(player, baddie)
		elif cmd == 'c':
			charge()
		else:
			cmd not in ['a', 't', 'c']
			input('Please select a valid option')
			combat(player,baddie)
	elif player.hp <= 0:
		player.game_over = True
	else:
		pass

def atk(player, baddie, weapon):
	os.system('cls')
	dmg = 0
	rolls = roll(weapon.damage)
	for die in rolls:
		if die in weapon.hit_range:
			dmg += 1
	baddie.hp = baddie.hp - dmg
	if baddie.hp <= 0:
		print('\nThe {} has been defeated!'.format(baddie.name))
		print('\nVictory!')
		ROOMS[player.location]['BADDIE'] = False
		baddies.remove(baddie)
		player.action_points += 2
		input('>')
		
	else:
		print('\nThe {} took {} damage!'.format(baddie.name,dmg))
		print(baddie.name + ' HP: ' + str(baddie.hp))

	player.action_points -= 1	
	combat(player, baddie)

def take_cover(player, baddie):
	player.cover = True
	player.action_points -= 1
	input('You dive behind {}!'.format(ROOMS[player.location]['COVER_ITEM']))
	combat(player,baddie)

def enemy_atk(baddie, player, hit_range, attacks):
	print('The {} attacks!'.format(baddie.name))
	player.action_points += 2
	dmg = 0
	rolls = roll(attacks)
	for die in rolls:
		if die in baddie.hit_range:
			dmg += 1
		else:
			dmg = 0
		print('dmg =' + str(dmg))
		input()
	if dmg >0 and player.cover == True:
		dmg -= 1
	player.hp = player.hp - dmg
	if player.hp <= 0:
		player.game_over = True
	else:
		print('You took {} damage!'.format(dmg))
		print('HP: ' + str(player.hp))
		combat(player, baddie)

def roll(n):
	return [random.randint(1,6) for x in range(n)]


def next_room(player):
	
	avail_rooms = []
	for key in ROOMS.keys():
		avail_rooms.append(key)
	if avail_rooms == False:
		avail_rooms = [1]
		player.win = True
		main_game_loop(player)
	else:
		player.location = random.choice(avail_rooms)
	main_game_loop(player)
	

#Game functionality







title_screen()

