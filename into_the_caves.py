from sys import exit
from functions import *
#from character import *
#from money import *
from entries import *

# These lists allow us to track if the player has already completed an encounter in a given area.
encountered_areas = []
listen = False
search = False
key = False
entry_map = []
treasure_collected = []
experience_points = {
	"Giant Rat": "5",
	"Goblin": "5",
	"Skeleton": "10",
	"Rust Monster": "300"
}

choice = input("> ")
while "3" not in choice:
	entry_1()
	print(f"Listened? {listen}")
	input()
	if choice == "1":
		listen = True
#		clear_screen()
		entry_42()
		entry_1()
	elif choice == "2":
		search = True
#		clear_screen()
		entry_57()
		entry_1()
	else:
#		clear_screen()
		entry_58()
	choice = input("> ")

# elif choice == "4":
# 	clear_screen()
# 	character_sheet()
# 	input()
# 	entry_1()
# 
# 
# 	
# 	choice = input("> ")
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_1()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_89()
# 	else:
# 		clear_screen()
# 		print("Did you kill any monsters or find any treasure? y/N")
# 
# 		choice = input("> ").lower()
# 
# 		if choice == "y":
# 			entry_88()
# 		else:
# 			exit(0)		
# 
# 
# 	input()
# 	clear_screen()
# 	entry_2()
# 
# 
# 		print("Press any key to continue...")
# 		input("> ")
# 		clear_screen()
# 		entry_23()
# # If you have already killed the monsters and taken the treasure from this part of the dungeon, read 23. If not, read 44.
# 	else:
# 		entry_44()		
# 
# 
# 	input()
# 	clear_screen()
# 	entry_1()
# 
# 
# 	input()
# 	clear_screen()
# 	entry_58()
# 
# 
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_9()
# 
# 	input()
# 	clear_screen()
# 	entry_54()
# 
# 
# 
# 	choice = input("> ")
# 
# 	if choice == "1":
# 		clear_screen()
# 		entry_21()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_53()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_36()
# 	else:
# 		clear_screen()
# 		entry_9()
# 
# 
# 		input()
# 		clear_screen()
# 		entry_54()
# 
# 
# 	print("Press any key to continue:")
# 	input()
# 	clear_screen()
# 	entry_83()
# 
# 
# 	input()
# 	clear_screen()
# 	entry_86()
# 
# 
# 	choice = input("> ")
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_62()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_27()
# 	else:
# 		clear_screen()
# 		entry_13()
# 
# 
# 	choice = input("> ")
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_62()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_3()
# 	else:
# 		clear_screen()
# 		entry_14()
# 
# 
# 	input()
# 	clear_screen()
# 	entry_26()
# 
# 	choice = input("> ").lower()
# 
# 	if choice == "y":
# 		entry_28()
# 	else:
# 		entry_62()
# 
# 	print("Press any key to continue:")
# 	input()
# 	clear_screen()
# 	entry_49()
# 
# 	input()
# 	clear_screen()
# 	entry_85()
# 
# 	choice = input("> ")
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_32()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_50()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_63()
# 	else:
# 		clear_screen()
# 		entry_19()
# 
# 	choice = input("> ")
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_64()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_73()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_51()
# 	else:
# 		clear_screen()
# 		entry_20()
# 
# 
# 	global key
# 	key = True
# 	new_character.money.gp += 5
# 	new_character.money.sp += 10
# 	
# 	choice = input("> ")
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_66()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_37()
# 	else:
# 		clear_screen()
# 		entry_21()
# 
# 		mouth_answer = input("Think about it, Type your answer below and then press any key to continue...")
# 		clear_screen()
# 		entry_82(mouth_answer.capitalize())
# 
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_58()
# 
# 	print("Press any key to continue...")
# 	input()
# 	encountered_areas.append("mouth")
# 	clear_screen()
# 	entry_40()
# 
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_58()
# 
# 	choice = input("> ")
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_30()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_47()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_72()
# 	elif choice == "4":
# 		clear_screen()
# 		entry_84()
# 	else:
# 		clear_screen()
# 		entry_26()
# 
# 
# 
# 	choice = input("> ")
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_15()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_14()
# 	else:
# 		clear_screen()
# 		entry_28()
# 
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_58()
# 
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_26()
# 
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_58()
# 
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_85()
# 
# 	choice = input("> ").lower()
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_73()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_87()
# 	else:
# 		clear_screen()
# 		entry_34()
# 
# 	choice = input("> ").lower()
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_73()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_87()
# 	else:
# 		clear_screen()
# 		entry_35()
# 
# 	input()
# 	clear_screen()
# 	entry_58()
# 
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_9()
# 
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_49()
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_40()
# 	choice = input("> ").lower()
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_31()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_4()
# 	else:
# 		clear_screen()
# 		entry_40()
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_58()
# print("Press any key to continue...")
# input()
# clear_screen()
# entry_1()
# 
# 	choice = input("> ").lower()
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_5()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_45()
# 	else:
# 		clear_screen()
# 		entry_43()
# 
# 	print("")
# 	input()
# 	clear_screen()
# 	entry_83()
# 	choice = input("> ").lower()
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_12()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_56()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_86()
# 	else:
# 		clear_screen()
# 		entry_45()
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_62()
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_26()
# 
# def entry_48():
# 	if "rust" in encountered_areas:
# 		clear_screen()
# 		entry_55()
# 	else:
# 		clear_screen()
# 		entry_67()
# 	choice = input("> ").lower()
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_31()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_4()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_22()
# 	else:
# 		clear_screen()
# 		entry_49()
# 	choice = input("> ").lower()
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_69()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_33()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_20()
# 	else:
# 		clear_screen()
# 		entry_50()
# 	choice = input("> ").lower()
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_73()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_87()
# 	else:
# 		clear_screen()
# 		entry_51()
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_9()
# 	input()
# 	clear_screen()
# 	entry_49()
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_58()
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_86()
#  	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_1()
# 
# 	
# 	choice = input("> ")
# 
# 	if choice == "1":
# 		clear_screen()
# 		entry_79()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_43()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_10()
# 	elif choice == "4":
# 		clear_screen()
# 		entry_2()
# 	else:
# 		entry_58()
# 	choice = input("> ")
# 
# 	if choice == "1":
# 		clear_screen()
# 		entry_25()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_74()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_77()
# 	elif choice == "4":
# 		clear_screen()
# 		entry_68()
# 	else:
# 		entry_59()
# 	treasure_collected['gems'].append(300)
# 	choice = input("> ")
# 
# 	if choice == "1":
# 		clear_screen()
# 		entry_15()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_48()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_14()
# 	else:
# 		entry_62()
# 	input()
# 	clear_screen()
# 	entry_85()
# 	choice = input("> ")
# 
# 	if choice == "1":
# 		clear_screen()
# 		entry_87()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_73()
# 	else:
# 		entry_64()
# 	choice = input("> ")
# 
# 	if choice == "1":
# 		clear_screen()
# 		entry_36()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_21()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_53()
# 	else:
# 		entry_65()
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_37()
# 	choice = input("> ")
# 
# 	if choice == "1":
# 		clear_screen()
# 		entry_81()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_41()
# 	else:
# 		entry_67()
# 	input()
# 	clear_screen()
# 	entry_83()
# 	choice = input("> ")
# 
# 	if choice == "1":
# 		clear_screen()
# 		entry_64()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_73()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_34()
# 	else:
# 		entry_69()
# 	choice = input("> ")
# 
# 	if choice == "1":
# 		clear_screen()
# 		entry_28()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_6()
# 	else:
# 		entry_70()
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_83()
#  	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_62()
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_83()
# 	choice = input("> ")
# 
# 	if choice == "1":
# 		clear_screen()
# 		entry_73()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_35()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_87()
# 	else:
# 		entry_75()
# 	choice = input("> ")
# 
# 	if choice == "1":
# 		clear_screen()
# 		entry_17()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_6()
# 	else:
# 		entry_76()
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_83()
# 	choice = input("> ")
# 
# 	if choice == "1":
# 		clear_screen()
# 		entry_17()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_6()
# 	else:
# 		entry_78()
# 		choice = input("> ")
# 
# 		if "statue" in listen and "statue" in search: # 4. If you did both (heard noise and found a note).
# 			clear_screen()
# 			entry_59()
# 		elif "statue" in listen:# 3. If you only heard creature sounds.
# 			clear_screen()
# 			entry_71()
# 		elif "statue" in search: # 2. If you only found a note that mentioned creatures.
# 			clear_screen()
# 			entry_44()
# 		elif "statue" not in listen and "statue" not in search: # 1. If you haven't found or heard any clues.
# 			clear_screen()
# 			entry_11()
# 		else:
# 			entry_79()
# 	else:
# 		entry_76()
# 	print("Press any key to continue...")
# 	input()
# 	clear_screen()
# 	entry_62()
# 	choice = input("> ")
# 
# 	if choice == "1":
# 		clear_screen()
# 		entry_29()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_16()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_86()
# 	else:
# 		entry_81()
# 		print("Press any key to continue...")
# 		input()
# 		clear_screen()
# 		entry_24()
# 	choice = input("> ")
# 	
# 	if choice == "1":
# 		clear_screen()
# 		encountered_areas.append("rats")
# 		entry_78()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_90()
# 	else:
# 		clear_screen()
# 		entry_83()
# 	choice = input("> ")
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_72()
# 	elif choice == "2":
# 		encountered_areas.append("skeletons")
# 		clear_screen()
# 		entry_13()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_90()
# 	else:
# 		clear_screen()
# 		entry_84()
# 	choice = input("> ")
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_73()
# 	elif choice == "2":
# 		encountered_areas.append("2goblins")
# 		clear_screen()
# 		entry_75()
# 	else:
# 		clear_screen()
# 		entry_85()
# 
# 	choice = input("> ")
# 	if choice == "1":
# 		clear_screen()
# 		entry_1()
# 	elif choice == "2":
# 		clear_screen()
# 		entry_28()
# 	elif choice == "3":
# 		encountered_areas.append("rust")
# 		clear_screen()
# 		entry_70()
# 	else:
# 		entry_86()
# 	choice = input("> ")
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_73()
# 	elif choice == "2":
# 		encountered_areas.append("3goblins")
# 		clear_screen()
# 		entry_65()
# 	elif choice == "3":
# 		clear_screen()
# 		entry_90()
# 	else:
# 		clear_screen()
# 		entry_87()
# 	
# 	choice = input("> ")
# 	
# 	if choice == "1":
# 		clear_screen()
# 		entry_1()
# 	else:
# 		exit(0)
# 
# clear_screen()

# character_sheet()


# Tasks:
# Done - Make a variable to check if the monsters have been killed. If not conduct battle. If so, check if treasure has been taken.
# Create a way to escape out of the game at any point by hitting the esc key or q key.
