from sys import exit
import os
from character import *
from money import *

# These lists allow us to track if the player has already completed an encounter in a given area.
encountered_areas = []
character_xp = []
listen = []
search = []
key = False
entry_map = []
experience_points = {
	"Giant Rat": "5",
	"Goblin": "5",
	"Skeleton": "10",
	"Rust Monster": "300"
}

def entry_1():
	entry_map.append("entry 1 map")
	print("""
The room you are in is fifty feet square, with 10' wide exits in the middle of the north, south, east, and west walls. 
The ceiling of the room is 15' up, but the corridors are only 10' tall. The walls, floor, and ceiling are made of rough
rock. There are some cracks and crevices in the rock walls, all very small. Standing in the exact center of the room is
a stone statue of a woman in armor. You examine it carefully, and finally even touch it — but it is merely a statue, nothing
magical or special. You have entered this 50' square room by the southern corridor, which leads out to fresh air and sunlight.
The other corridors are dark. The light from your lamp helps, but shadows linger in the corners of this large room.
Do you want to:
1. Stop and listen?
2. Search the room?
3. Go down a corridor?""")
	choice = input("> ")

	if choice == "1":
		listen.append("statue")
		os.system('cls' if os.name=='nt' else 'clear')
		entry_42()
	elif choice == "2":
		search.append("statue")
		os.system('cls' if os.name=='nt' else 'clear')
		entry_57()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_58()
	else:
		entry_1()

def entry_2():
	print("""
You are back outside!
1. Go back inside.
2. Go shopping for supplies.
3. Quit the adventure; your fighter goes back to town.""")
	
	choice = input("> ")
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_1()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_89()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		print("Did you kill any monsters or find any treasure? y/N")

		choice = input("> ").lower()

		if choice == "y":
			entry_88()
		else:
			exit(0)		

def entry_3():
	print("""
You go south, and leave the caves. You may go home, and end this adventure, or 
you can go back to the first room. Press any key to continue...""")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_2()

def entry_4():
	if "rats" in encountered_areas:
		print("You go south from the strange room.")
		print("Press any key to continue...")
		input("> ")
		os.system('cls' if os.name=='nt' else 'clear')
		entry_23()
# If you have already killed the monsters and taken the treasure from this part of the dungeon, read 23. If not, read 44.
	else:
		entry_44()		

def entry_5():
	print("You decide to go back to the statue room. Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_1()

def entry_6():
	print("You go back to the statue room. Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_58()

def entry_7():
	print("You turn the corner and follow the passage back to a room.")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_9()

def entry_8():
	entry_map.append("entry 8 map")
	print("After the turn, the corridor goes 50' west and opens into a room. Press any key to continue:")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_54()

def entry_9():
	print("""
You may go one of three ways. Do you want to:
1. Go North?
2. Go East?
3. Go back to the Statue room?""")

	choice = input("> ")

	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_21()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_53()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_36()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_9()

def entry_10():
	if "2goblins" in encountered_areas:
		entry_9()
	else:
		print("""
The corridor goes 20' north from the room and then turns right. You peek around the corner, and see that the corridor goes 20'
and opens into another room. Press any key to continue...""")
		input()
		os.system('cls' if os.name=='nt' else 'clear')
		entry_54()

def entry_11():
	print("""
You quietly approach the room, and you don't see anything unusual. But as you step into the room, some giant rats leap out
from the corner to your right, and attack! Two of them hit you, for a total of 3 points of damage. You are suddenly in battle,
and cannot escape.""")
	print("Press any key to continue:")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_83()

def entry_12():
	print("""
Talking to the creature doesn't do any good. It attacks, and gets one free swing while you are talking! Give the monster one 
free attack and press any key to run the battle normally...""")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_86()

def entry_13():
	print("""
You kill the two skeletons! As each one "dies," its bones collapse in a heap, and the rusty sword drops to the floor with a clang.
You search the area, but find no treasure. However, there is a door in the east wall of the room. Do you want to:
1. Go South?
2. Open the door?""")
	choice = input("> ")
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_62()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_27()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_13()

def entry_14():
	print("""You go west, and come to another room. It has an exit south, leading outside, and another corridor heading west.
You don't want to go west, the ghouls are in that direction. You recognize this room as the entrance for your very first adventure!
This is where you hit the goblin, and he ran away. Do you want to:
1. Go back East?
2. Go South?""")
	choice = input("> ")
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_62()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_3()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_14()

def entry_15():
	if "skeletons" in encountered_areas:
		entry_61()
	else:
		print("""
The corridor goes north and opens into a room. As you peer into the room, you see two skeletons with rusty swords standing about
10' from you, around the corner. Without making a sound, they step forward, grinning horribly, and swing at you. One of them hits,
for 2 points of damage. Press any key to continue the battle...""")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_26()

def entry_16():
	print("You are leaving the Rust Monster room, heading west. Have you mapped this part of the dungeon yet? (y/n)")
	choice = input("> ").lower()

	if choice == "y":
		entry_28()
	else:
		entry_62()

def entry_17():
	print("""
The corridor goes north 30', and then there is a side passage to the left (west). The main corridor continues another 30' and 
then turns left. When you get to the side passage, you see that it goes 10' west and opens into a strange room.""")
	print("Press any key to continue:")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_49()

def entry_18():
	print("""
You carefully enter the room, and see two goblins in a far corner. They have swords, and seem to be expecting you. They attack,
and each gets a free swing before you can react. Give each goblin one free swing to start and press any key to run the battle normally...""")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_85()

def entry_19():
	print("""
You think that there are goblins up here, so you keep your lantern shuttered and sneak up to peek into the room. You hear soft
talking in a language you don't understand. Peeking around the corner, you see two goblins to your right, at the south end of the room.
They seem to be talking about something and don't notice you. Do you want to:
1. Go back?
2. Talk to them?
3. Attack?""")
	choice = input("> ")
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_32()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_50()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_63()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_19()

def entry_20():
	print("""
You decide to leave the goblins alone. But as you start to back off, the goblin you have been talking to draws its sword and 
attacks! The other one leaves, going north and turning left. Do you want to:
1. Fight the goblin?
2. Run away?
3. Keep talking?""")
	choice = input("> ")
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_64()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_73()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_51()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_20()

def entry_21():
	if "entry 21 map" in entry_map:
		entry_52()
	else:
		entry_map.append("entry 21 map")
		print("""
Starting from the north wall of this room, the corridor goes 10' north, turns left (west) and goes 10' further, opening into 
the east wall of another room. There are more goblins here! But when they see you, they shriek and run through a stout door on
the north wall, slamming it behind them. You search the room carefully and find one small bag by the door, apparently dropped 
by one of the goblins. The bag contains 10 sp, 5 gp, and — a key! Now do you want to:
1. Open the door?
2. Go back?""")
	global key
	key = True
	new_character.money.gp += 5
	new_character.money.sp += 10
	
	choice = input("> ")
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_66()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_37()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_21()

def entry_22():
	entry_map.append("entry 22 map")
	if "mouth" in encountered_areas:
		entry_39()
	else:
		print("""
You enter the strange room to investigate. The room is empty and clean, and the only feature is the orange mouth on the
far wall, about 8' long. You search the room, listening and looking carefully, but you find nothing. Suddenly, as you are
about to leave, the lips of the giant mouth move, and in a big booming bass voice it says, "Surprise! You are here for 
double-or-nothing! Ready or not, here we go. O-T-T-F-F-S-S. What's next in line? If you solve this riddle, your treasure 
will double. If you fail, it will all disappear. What is your answer?" If you try to leave, you find the way blocked by an
invisible force. "You must answer, y'know!" bellows the mouth.""")
		mouth_answer = input("Think about it, Type your answer below and then press any key to continue...")
		os.system('cls' if os.name=='nt' else 'clear')
		entry_82(mouth_answer.capitalize())

def entry_23():
	print("You go back to the room where the giant rats were and continue through, arriving back at the first room.")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_58()

def entry_24():
	print("""
The mouth laughs and says "Come back again some time!" The invisible barrier is gone, and you can leave the room. You cannot 
find anything more here, nor will the mouth speak to you again.""")
	print("Press any key to continue...")
	input()
	encountered_areas.append("mouth")
	os.system('cls' if os.name=='nt' else 'clear')
	entry_40()

def entry_25():
	print("You decide that the rats look dangerous, and you head back the way you came. The rats don't notice.")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_58()

def entry_26():
	print("""You are facing two skeletons. Do you want to:
1. Talk to them?
2. Turn them?
3. Run away?
4. Fight?""")
	choice = input("> ")
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_30()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_47()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_72()
	elif choice == "4":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_84()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_26()

def entry_27():
	if key == True:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_80()
	elif key == False:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_46()

def entry_28():
	print("""
The corridor goes only 10' west before connecting to another corridor heading north; the main corridor continues west, into 
darkness. The north corridor goes 30' and opens into a room. Do you want to:
1. Go North?
2. Continue West?""")
	choice = input("> ")
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_15()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_14()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_28()

def entry_29():
	print("""You go back to the statue room.""")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_58()

def entry_30():
	print("""The skeletons ignore your chatter, and swing again. One of them hits you,
doing 2 more points of damage.""")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_26()

def entry_31():
	if "2goblins" in encountered_areas:
		print("You go north from the strange room.")
		entry_7()
	else:
		entry_8()

def entry_32():
	print("You decide to go back. The goblins don't notice you, and you return to the statue room.")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_58()

def entry_33():
	print("You decide to attack the goblins before they can get help. You leap out and block the first goblin's escape, and they both draw swords and attack you. Press any key to run the battle normally.")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_85()

def entry_34():
	print("""
As you keep talking to the goblin you see 3 more coming from the north. They look mad. Do you want to:
1. Run away?
2. Fight?""")
	choice = input("> ").lower()
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_73()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_87()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_34()

def entry_35():
	print("""
Although you try to talk to them, the goblins are ferocious and ready for a fight. One swings and hits you, for 2 points of damage. 
Do you want to:
1. Run away?
2. Fight?""")
	choice = input("> ").lower()
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_73()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_87()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_35()

def entry_36():
	print("""
You decide to go back to the start. Going west from here, the corridor turns south.
You follow it back to the statue room. Press any key to continue...""")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_58()

def entry_37():
	print("You go back to the room where you first found the goblins.")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_9()

def entry_38():
	print("You go east down the long corridor, around the corner heading south, and come to the side passage leading into the strange room.")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_49()

def entry_39():
	print("The mouth roars, \"YOU again?! Go away, pest!\" You can't find anything of value here.")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_40()

def entry_40():
	print("""From here, do you want to:
1. Go North?
2. Go South?""")
	choice = input("> ").lower()
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_31()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_4()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_40()

def entry_41():
	print("The creature is feasting on rust, and ignores you. You run past it through the room and arrive back at the statue room.")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_58()

def entry_42():
	print("You stop and listen, and hear squeaking noises to the east.")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_1()

def entry_43():
	entry_map.append("entry 43 map")
	print("""The corridor goes 20' to the west and opens into a room. The room is empty, except for a few small piles of reddish
dust. Do you want to:
1. Go back?
2. Continue?""")
	choice = input("> ").lower()
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_5()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_45()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_43()

def entry_44():
	print("""
As you approach a room, a giant rat jumps out of the shadows and bites you! You see 2 more giant rats in the room. Take 2 
points of damage, and press any key to continue...""")
	print("")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_83()

def entry_45():
	print("""
You go into the room and look around. There is nothing here but the reddish dust. When you look closely at the dust, however, 
you realize that it's rust! You hear a snort, and when you look up, you see a strange looking creature coming into the room 
from the western corridor. It looks like a giant armadillo with a long tail, and has 2 feathery feelers on the front. It charges
at you! Do you want to:
1. Talk to it?
2. Run away?
3. Fight?""")
	choice = input("> ").lower()
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_12()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_56()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_86()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_45()

def entry_46():
	print("""
You try to bash the door open without using a key, but without success. The solid door remains securely closed.
You eventually give up, passing the scattered skeleton bones as you head out to the main corridor.""")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_62()

def entry_47():
	print("""You try to Turn the skeletons like the cleric Aleena Turned the ghouls, but nothing happens. It's a special talent
that clerics have, not fighters. Each skeleton swings at you again, but they both miss.""")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_26()

def entry_48():
	if "rust" in encountered_areas:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_55()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_67()
		
def entry_49():
	print("""You may go in and investigate the strange room, or you can go north or south. Do you want to:
1. Go North?
2. Go South?
3. Investigate?""")
	choice = input("> ").lower()
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_31()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_4()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_22()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_49()

def entry_50():
	print("""You greet the goblins in your own language, the Common Tongue. They look up, startled, and one growls something in its own language.
The other smiles at you, and says "Why, hello there! What can we do for you?"
The growling goblin starts heading north, apparently leaving the room. Do you want to:
1. Keep talking?
2. Attack?
3. Go back?""")
	choice = input("> ").lower()
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_69()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_33()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_20()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_50()

def entry_51():
	print("""You try to keep talking, but the goblin attacks; it misses.
You suddenly hear more goblin noises to the north, and see 2 more goblins coming, with their swords out and looking very angry.
Do you want to:
1. Run away?
2. Fight?""")
	choice = input("> ").lower()
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_73()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_87()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_51()

def entry_52():
	print("You go around the corner and look in the room, but nobody is there. There is nothing here to find, so you go back around the corner to the last room you were in.")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_9()

def entry_53():
	entry_map.append("entry 53 map")
	if "entry 53 map" in entry_map:
		entry_38()
	else:
		print("""
If you have already mapped this of the dungeon, read 38. If not, continue: The corridor goes 50' east from the room and then 
turns right, to the south. Peering around the corner, you see that the corridor goes 30' south, and a side passage then opens
to the west. When you get to that point, you see that the side passage goes 10' west and opens into another room, with blue 
walls and a huge orange mouth on the opposite wall. Add Entry 53 Map to your map and press any key to continue...""")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_49()

def entry_54():
	entry_map.append("entry 54 map")
	print("The room looks like Entry 54 Map (add it to your map):")
	if "statue" in listen or "statue" in search:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_19()
	elif "statue" not in listen or "statue" not in search:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_18()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_54()

def entry_55():
	print("You continue through the Rust Monster room, and get back to the statue room.")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_58()

def entry_56():
	print("As you turn to run away, the monster quickly attacks, and gets in your way. You cannot retreat!")  
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_86()
 
def entry_57():
	entry_map.append("entry 57 map")
	print("""
You search the room carefully, and you find a small scrap of paper in a niche (small hole) in one wall.
Opening it, you discover a note, written in the Common tongue:
		RATS EAST
		GOBLINS NORTH
		BEWARE WEST!
You can also see parts of the corridors leading out of the room, which look like Entry 57 Map.
You find nothing else in the room.""")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_1()

def entry_58():
	print("""From this room, you can go many ways. Do you want to:
1. Go East?
2. Go West?
3. Go North?
4. Go South?""")
	
	choice = input("> ")

	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_79()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_43()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_10()
	elif choice == "4":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_2()
	else:
		entry_58()

def entry_59():
	print("""
As you approach the room, you hear more squeaks. You wisely shutter your lantern, leaving only a dim reddish glow, and peek
into the room. You see three giant rats scurrying around and some scattered treasure nearby. Do you want to:
1. Go back?
2. Talk to them?
3. Try to scare them?
4. Attack?""")
	choice = input("> ")

	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_25()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_74()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_77()
	elif choice == "4":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_68()
	else:
		entry_59()

def entry_60():
	print("""
Your armor, shield, sword, and dagger have all been turned to rust by the fearsome Rust Monster! But now that you have no more
metal, the creature turns away from you, not interested any more. You can see, now, that it has no teeth or claws, and can't 
actually hurt you! You watch as it ambles over to one of the piles of rust, and it starts to eat, ignoring you completely.
Keeping a careful eye on the creature, you look around the room. There are gems here and there, some covered by rust; you collect
six of them! Their total value is 300 gp. Since you are unprotected and unarmed, you go east to the first room and then go outside,
heading for town. To find how many Experience Points you have earned, read 88. You will also have to go shopping for more armor and
weapons. The shopping list is given in 89.""")
	treasure_collected['gems'].append(300)

def entry_61():
	if "treasure" in encountered_areas:
		os.system('cls' if os.name=='nt' else 'clear')
		print("You peer into the skeleton room, and see that nothing has changed.")
		entry_62()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_27()
#        
#If you already investigated the door, there is nothing more to do here; read 62.
#If you want to investigate the door in this room, read 27.""")  

def entry_62():
	print("""
You are at an intersection of the corridor to the north and the east-west corridor. Do you want to:
1. Go North
2. Go East
3. Go West""")
	choice = input("> ")

	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_15()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_48()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_14()
	else:
		entry_62()

def entry_63():
	print("""
You leap out and attack the goblins! You will get two free swings before they can get their swords out. Take your 2 free attacks
and press any key to run the battle normally...""")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_85()

def entry_64():
	print("""
You attack the goblin. Your first swing misses, and the goblin misses you. But you see, coming from the north corridor, two more
goblins, waving swords and looking very angry. Do you want to:
1. Keep fighting?
2. Run away?""")
	choice = input("> ")

	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_87()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_73()
	else:
		entry_64()

def entry_65():
	print("""
You have won the great goblin fight. Congratulations! It was a tough battle for one lonely fighter. Don't forget that you started
the adventure with a Potion of Healing, which can cure all your damage if you haven't already used it. Searching the area, you 
find 100 sp and 50 gp in small sacks that the goblins were carrying. Their swords look rusty and worthless, and they have nothing
else of value. Do you want to:
1. Go west?
2. Go north?
3. Go east?""")
	new_character.money.sp += 100
	new_character.money.gp += 50
	choice = input("> ")

	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_36()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_21()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_53()
	else:
		entry_65()

def entry_66():
	print("""
You try to open the door, but without success. Your key doesn't seem to work. You hear a goblin voice say from the other side,
in Common, "Go away! We don't want any!" You may keep trying, if you wish, but the goblins seem to have barred the door. You must
eventually go back.""")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_37()

def entry_67():
	print("""Since you didn't kill the Rust Monster, it's still there, eating rust. Are you dragging a large chest full of coins?
1. Yes
2. No""") 
	choice = input("> ")

	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_81()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_41()
	else:
		entry_67()

def entry_68():
	print("You jump out and swing at the rats and take 2 free swings before the rats can do anything! Press any key to run the rest of the fight normally.") 
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_83()

def entry_69():
	print("""You keep talking as one goblin leaves, going north and turning left.
The other tries to seem friendly, but you can tell that he doesn't like you.
Suddenly, you hear more goblin noises from the north. Do you want to:
1. Attack?
2. Run away?
3. Keep talking?""")
	choice = input("> ")

	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_64()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_73()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_34()
	else:
		entry_69()

def entry_70():
	encountered_areas.append("rust")
	print("""You have slain the horrible Rust Monster!
Searching the room, you find 10 gems laying about, some in cracks and crevices, and some in the piles of rust.
The total value of the gems is 600 gp! Now do you want to:
1. Go west?
2. Go back east?""")
	choice = input("> ")

	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_28()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_6()
	else:
		entry_70()

def entry_71():
	print("""You approach the room with caution, listening to the squeaking.
But suddenly, three giant rats jump out of the shadows and attack! One of them bites you for 1 point of damage.""")  
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_83()
 
def entry_72():
	print("""You turn to run and a skeleton hits you again for 1 more point of damage.
If you are still alive, you run south to a corridor, where you can turn east or west.
Looking back, you see that the skeletons are not following you. You stop and catch your breath.""")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_62()

def entry_73():
	print("""You decide to flee. As you turn to run, you are hit by one goblin's sword for 2 points of damage.
(If your hit points reach zero, you are dead unless you can drink the potion; otherwise, continue.)
You run back into the first room, and continue through it and out the south passage, toward sunlight.
A group of goblins is running after you, shouting and waving their swords.
They stop at the cave entrance, and keep screaming and waving their swords; but there are too many of them.
You decide to go home.""")
	print("""This is the end of this adventure. Read 88 to find your Experience Points and treasures.
If you wish to buy some supplies, the Equipment List is given in 89.""")

def entry_74():
	print("""You try to talk to the rats, but talking doesn't work. You only give yourself away, and they attack!
One of them bites you for 1 hit point of damage. Press any key to run the rest of the battle.""")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_83()

def entry_75():
	print("""You have defeated the pair of goblins! But before you can look around the room, you hear noises from the north.
Three more goblins are coming down the north corridor. They have their swords out and look angry. Do you want to:
1. Run away?
2. Talk?
3. Fight?""")
	choice = input("> ")

	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_73()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_35()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_87()
	else:
		entry_75()

def entry_76():
	print("""You arrive in the rat room; it is empty. Do you want to:
1. Go North?
2. Go West?""")
	choice = input("> ")

	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_17()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_6()
	else:
		entry_76()

def entry_77():
	print("""You decide to scare the rats. You leap out and scream, waving your sword and flashing the light around.
One of the giant rats runs off to the north, but the others attack you!""")
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_83()

def entry_78():
	print(new_character.experience_points)
	print("""You have won the battle with the giant rats!
Searching the room, you find 100 cp and 100 sp scattered in the messy rat lair, and you put them in the sacks that you are carrying. Now do you want to:
1. Go North?
2. Go West?""")
	new_character.money.sp += 100
	new_character.money.cp += 100
	# print(f"You now have {new_character.money.pp} PP, {new_character.money.gp} GP, {new_character.money.ep} EP, {new_character.money.sp} SP, {new_character.money.cp} CP")
	new_character.money.current_money()
	choice = input("> ")

	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_17()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_6()
	else:
		entry_78()

def entry_79():
	if "rats" not in encountered_areas:
		print("The corridor goes 50' east and opens into another room.")
				# If you have already been through this part of the dungeon, read 76. Otherwise, continue:
				# What are you expecting here, and why? You may have found one or two clues.

		choice = input("> ")

		if "statue" in listen and "statue" in search: # 4. If you did both (heard noise and found a note).
			os.system('cls' if os.name=='nt' else 'clear')
			entry_59()
		elif "statue" in listen:# 3. If you only heard creature sounds.
			os.system('cls' if os.name=='nt' else 'clear')
			entry_71()
		elif "statue" in search: # 2. If you only found a note that mentioned creatures.
			os.system('cls' if os.name=='nt' else 'clear')
			entry_44()
		elif "statue" not in listen and "statue" not in search: # 1. If you haven't found or heard any clues.
			os.system('cls' if os.name=='nt' else 'clear')
			entry_11()
		else:
			entry_79()
	else:
		entry_76()

def entry_80():
	entry_map.append("entry 80A map")
	entry_map.append("entry 80B map")
	print("""
You put the key in the lock and turn until you hear it "click." Putting the key away you open the door. There is a small room 
behind the door! The room is empty except for one large chest by one wall. You walk over to it, and discover that it's made of
heavy wood with metal bands around it. It isn't locked (luckily), so you carefully open it. But alas — it's trapped. Make a 
saving throw vs. Magic Wands! (You need to roll a 13 or higher on 1d20.) This Saving Throw is used for many things. Generally,
it indicates whether you jump out of the path of danger — such as the beam of a magic wand. However, in this case, the danger is
a blade, mounted on the edge of the chest and connected to a metal spring. When you open the lid, the blade sweeps out toward you. 
If you made the Saving Throw, you jump back as the blade misses you. However, if you missed the Saving Throw, you take 4 points 
of damage! If you are struck down to zero hit points or less, you can grab your potion — if you still have it — and drink it before
you pass out. It will cure you somewhat, but only back up to 4 hit points. If you don't have the potion left — sorry, but you are dead!
(Special note: In group games, you will not be allowed to do this. Zero hit points indicates death, with no extra time to do anything.) 
If the trap kills you, read 90. But if you survived the trap, continue reading. You look in the chest and see hundreds of coins — 
500 cp, 200 sp, and 200 ep. You start to close the chest and drag it out with you. But as you close the lid, you see a peep hole in the
north wall, about an inch across. It was blocked by the door as you entered. You look through, and see a short corridor that goes north 
20' and turns left. To the east, by the turn, is a large door with two stout bars across it. A goblin is standing by the door, apparently
on guard. The area looks like Entry 80B Map. There is a crack in the wall near this peep hole. You suddenly realize that the crack might 
be the edge of a secret door! This treasure chest must belong to goblins! However, you can't open the secret door, so you drag the chest 
back out, past the scattered bones of the dead skeletons and south to the main corridor.""")
	treasure_collected['cp'].append(500)
	treasure_collected['sp'].append(200)
	treasure_collected['ep'].append(200)
	print("Press any key to continue...")
	input()
	os.system('cls' if os.name=='nt' else 'clear')
	entry_62()

def entry_81():
	print("""
Oops! As you enter the room, the Rust Monster looks up from its feeding, grunts, and runs toward you. It rushes to the chest you are dragging,
and before you can escape, it dissolves the metal bands around the chest. The chest comes apart, coins falling everywhere, and the creature 
gleefully turns all the coins to rust! Do you want to:
1. Go East?
2. Go West?
3. Attack the creature?""")
	choice = input("> ")

	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_29()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_16()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_86()
	else:
		entry_81()

def entry_82(mouth_answer):
	if mouth_answer == "E":
		print("Correct! The answer is \"E.\" The letters stand for One, Two, Three, Four, Five, Six, and Seven.")
		print("The \"next in the series\" is Eight!.")
		print("You suddenly feel different, more weighted down as whatever treasure you had is now doubled!")
		print("Press any key to continue...")
		input()
		os.system('cls' if os.name=='nt' else 'clear')
		entry_24()
# print("""If you guess the answer correctly, you may double the amount of treasure you have. If not, it all disappears, and your character is left with none.
	else:
		print("Wrong! The answer is \"E.\" The letters stand for One, Two, Three, Four, Five, Six, and Seven.")
		print("The \"next in the series\" is Eight!.")
		print("You suddenly feel different, less weighted down as whatever treasure you had is now gone!")
		print("Press any key to continue...")
		input()
		os.system('cls' if os.name=='nt' else 'clear')
		entry_24()

def entry_83():
	entry_map.append("entry 83 map")
	print("""You are having a battle with giant rats. Three of them are here, unless you scared one off. The area looks like Entry 83 Map.
GIANT RATS:	17
You:		10
D:		1d3
hp:		2 each
Run the battle normally, using the Combat Checklist to be sure that you are doing it correctly. If you don't remember what "1d3" means, read the section on "Dice" again (page 12).
All the rats will fight until dead. If you decide to run away, one rat will bite you as you turn to run (roll for damage). But then, if you are still alive, you can go back to the statue room. If so, read 58.
1. If you kill all the rats.
2. If the rats kill you""")
	choice = input("> ")
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		encountered_areas.append("rats")
		entry_78()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_90()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_83()

def entry_84():
	print("""You are fighting two skeletons.
SKELETONS:	16 
You:		10
D:		1d6
hp:		4 each
Use the checklist to run the battle. The skeletons will fight until slain.
1. Run away.
2. If you kill the skeletons.
3. If the skeletons kill you.""")
	choice = input("> ")
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_72()
	elif choice == "2":
		encountered_areas.append("skeletons")
		os.system('cls' if os.name=='nt' else 'clear')
		entry_13()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_90()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_84()

def entry_85():
	print("""You are fighting two goblins!
GOBLINS:	17
You:		11
D:		1d6
hp:		5 each
Remember to make two rolls for the monsters; each one gets a swing after you make yours.
Use the checklist to be sure that you are running the battle correctly.
1. Run away.
2. Kill the goblins.""")
	choice = input("> ")
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_73()
	elif choice == "2":
		encountered_areas.append("2goblins")
		os.system('cls' if os.name=='nt' else 'clear')
		entry_75()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_85()

def entry_86():
	print("""You are fighting the Rust Monster!
RUST MONSTER:	13
You:		15
Damage:		rust
hp:		15
Use the checklist to be sure that you are running the battle correctly. If the 
rust monster hits you, it does no damage at all. Instead, it makes metal turn 
to rust!
1. Run east
2. Run west
3. You killed the Rust Monster!""")
# As you run the battle, use the following notes to find the effects of each hit.
# If you decide to run away, the monster gets one free attack, but only needs a Hit Roll 9 or better.
# You can run away after that, but you can only run either #east (back to the statue room) or west.
# If you run east, read 1; if you go west, read 28.
# If you kill the rust monster, read 70.
# If you have been here before, you might not have some of the items mentioned below.
# Resume the battle wherever you left off, and remember to keep track of the equipment you have left.
# First Hit: your shield turns to rust and falls apart. Now the Rust Monster only needs an 11 or better to hit you. Read the "Special Note" below.
# Second Hit: Your Armor turns to rust. Now the creature only needs a roll of 6 or higher to hit.
# Third Hit: Your sword turns to rust! You must get out a dagger if you want to continue the fight.
# Fourth Hit: Your dagger turns to rust! You have no more weapons. Read 60.
# Special Note: When you lose your armor or shield, you become easier to hit. 
# All monsters you encounter afterward will gain bonuses to their Hit Rolls. 
# If you lose your shield, give them a +1 bonus. If you lose your armor, give them a total bonus of + 7 to their Hit Rolls.
# Note this special bonus on your scrap paper, and apply it to all battles until you get new armor or shield.

	choice = input("> ")
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_1()
	elif choice == "2":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_28()
	elif choice == "3":
		encountered_areas.append("rust")
		os.system('cls' if os.name=='nt' else 'clear')
		entry_70()
	else:
		entry_86()

def entry_87():
	print("""You are fighting three goblins!
GOBLINS:	17
You:		11
D:		1d6
hp:		5 each
Remember to make three rolls for the monsters; each one gets a swing after you take yours.
Use the checklist to be sure that you are running the battle correctly. 
1. If you decide to run away.
2. If you kill the goblins.
3. If the goblins kill you.""")
	choice = input("> ")
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_73()
	elif choice == "2":
		encountered_areas.append("3goblins")
		os.system('cls' if os.name=='nt' else 'clear')
		entry_65()
	elif choice == "3":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_90()
	else:
		os.system('cls' if os.name=='nt' else 'clear')
		entry_87()

def entry_88():
	print("""
When you complete this adventure, you get Experience Points. First, add up all the treasure you brought out of the dungeon
(ignore anything you lost), and figure out how much it is all worth, in gold pieces. You will get 1 XP for each 1 gp worth
of treasure you find — in addition to getting the treasure. After adding up the treasure, find out how much Experience you 
get for slaying monsters, according to this chart:
Giant Rats --> 5 each
Goblins --> 5 each
Skeletons --> 10 each
Rust Monster --> 300
Add that total to your treasure total to get the total number of Experience Points awarded for this adventure. To determine 
your +10% bonus, drop the last number, and add it to the total awarded. Then add the adjusted total XP earned to the current
XP on the back of your character sheet, to find your new total overall. To finish up, add the treasure you found to the money
you already had. Example: Imagine that you killed the Rust Monster and found 6 gems there, with a value of 600 gp. You also 
killed 3 giant rats, finding 100 cp and 100 sp. Imagine that you have no other notes. Looking on the conversion chart, you see that 100 cp = 1 gp; 100 sp = 10 gp.
Adding that to the gem value, your newly found treasure is worth a total of 611 gp.
For monsters, you get 300 XP for the rust monster, plus 15 XP for the giant rats (5 each).
That total is 315. Adding it to the 611 for treasure, your total XP award is 926.
To find your 10% bonus, drop the 6. Add the bonus of 92 to the award of 926, for an adjusted total XP of 1018.
Then you add that to your current 523 XP, for a new total XP of 1541 — less than 500 XP from 2nd Level!
Lastly, you add the actual treasure — 6 gems (worth 600 gp), 100 cp, and 100 sp — to your treasure list.
That finishes this adventure. You may go to the next adventure, or you may wish to go shopping.
Would you like to go shopping now? (Y/n)""")

def entry_89():
	print("""You want to go shopping. Instead of making an adventure out of it (like the beginning of this trip), you may simply imagine that you are visiting the various shops in town, buying whatever you need. The items you may buy — armor, weapons, and other equipment — are listed below, along with their prices. To make a shopping trip, first write down the items you want, and their prices, on a piece of scrap paper. Then add up the total cost. If you can afford what you want, subtract that total cost from your treasure. Write the items in the "Normal Items" section on the back of the Character Sheet. Be sure to write the new total treasure in the Money box.
WEAPONS AND EQUIPMENT
Item Cost (in gp)

weapons = {
	"Dagger": "3",
	"Sword": "10"
}

armor = {
	"Leather Armor": "20",
	"Chain Mail Armor": "40",
	"Plate Mail Armor": "60",
	"Shield": "10"
}

other_equipment = {
	"Backpack, leather": "5",
	"Flask of Oil": "2",
	"Lantern": "10",
	"Mirror (hand-sized, steel)": "5",
	"Pole (wood, 10' long)": "1",
	"Rope (50' long)": "1",
	"Tinder Box (flint, steel, dry wood shavings and twigs)": "3",
	"Torches (6)": "1",
	"Waterskin (or wineskin)": "1",
	"Wine (1 quart)": "1"
}

sacks = {
	"Small": "1",
	"Large": "2"
}

rations = {
	"Iron Rations (preserved food for 1 person for 1 week)": "15",
	"Standard Rations (unpreserved food for 1 person for 1 week)": "5"
}
(Note: There are more weapons and equipment available in group adventures. See the complete list in the center of this book.)""")  

def entry_90():
	print("""
Your character has been lost in the dungeon. Don't be upset; it can happen in any DUNGEONS & DRAGONS game, and often does, 
through no fault of yours. That is the end of this adventure. You may start over, if you wish. To do that, be sure not to keep
any treasure you may have found before you died. The character should have exactly the same equipment, treasure, and hit points
as when you started this adventure. In other words, you start over.
1. Start over.
Press any other key to exit the game.""")
	
	choice = input("> ")
	
	if choice == "1":
		os.system('cls' if os.name=='nt' else 'clear')
		entry_1()
	else:
		exit(0)

os.system('cls' if os.name=='nt' else 'clear')

# character_sheet()
entry_1()

# Tasks:
# Done - Make a variable to check if the monsters have been killed. If not conduct battle. If so, check if treasure has been taken.
# Create a way to escape out of the game at any point by hitting the esc key or q key.
