import random

class DnDCharacter:
    TITLE_MAPPING = {
        0: "Veteran",
        2000: "Warrior",
        4000: "Swordmaster"
    }
    
    def __init__(self, name, strength, dexterity, constitution, intelligence, wisdom, charisma, hit_points, experience_points):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hit_points = hit_points
        self.saving_throws = self.fighter_saving_throws
        self.experience_points = experience_points
        self.money = {"pp": 0, "gp": 0, "sp": 0, "ep": 0, "cp": 0}

    @classmethod
    def create_new_character(cls):
        name = input("Enter character name: ").capitalize()
        strength = cls.roll_stat()
        dexterity = cls.roll_stat()
        constitution = cls.roll_stat()
        intelligence = cls.roll_stat()
        wisdom = cls.roll_stat()
        charisma = cls.roll_stat()
        hit_points = cls.roll_hp()
        experience_points = 0
        return cls(name, strength, dexterity, constitution, intelligence, wisdom, charisma, hit_points, experience_points)
        
    @staticmethod
    def roll_stat():
        # Roll 3d6 and return the total
        return sum(random.randint(1, 6) for _ in range(3))
    
    @staticmethod
    def roll_hp():
        # Roll 1d8 and return the result
        return random.randint(1,8)
    
    @staticmethod
    def fighter_saving_throws():
        drp = int(12)
        mw = int(13)
        potts = int(14)
        db = int(15)
        rsos = int(16)
        return drp, mw, potts, db, rsos
    
    def get_title(self):
        for exp, title in sorted(DnDCharacter.TITLE_MAPPING.items(), reverse=True):
            if self.experience_points >= exp:
                return title
        return "Novice"
    
    @property
    def pp(self):
        return self.money["pp"]

    @pp.setter
    def pp(self, value):
        self.money["pp"] = value 

    @property
    def gp(self):
        return self.money["gp"]

    @gp.setter
    def gp(self, value):
        self.money["gp"] = value

    @property
    def sp(self):
        return self.money["sp"]

    @sp.setter
    def sp(self, value):
        self.money["sp"] = value

    @property
    def ep(self):
        return self.money["ep"]

    @ep.setter
    def ep(self, value):
        self.money["ep"] = value

    @property
    def cp(self):
        return self.money["cp"]

    @cp.setter
    def cp(self, value):
        self.money["cp"] = value
    
    def add_experience(self, points):
        self.experience_points += points

# Create a new character
new_character = DnDCharacter.create_new_character()

# Access the character's name
print(new_character.name)

# Store character information in variables
# playerName = new_character.name
playerClass = new_character.get_title()
playerStrength = new_character.strength
playerDexterity = new_character.dexterity
playerConstitution = new_character.constitution
playerIntelligence = new_character.intelligence
playerWisdom = new_character.wisdom
playerCharisma = new_character.charisma
playerHitPoints = new_character.hit_points
playerSavingThrows = new_character.fighter_saving_throws()
playerExperience = new_character.experience_points
playerPP = new_character.pp
playerGP = new_character.gp
playerEP = new_character.ep
playerSP = new_character.sp
playerCP = new_character.cp
# playerGems = new_character.Gems
# playerGemValue = new_character.GemValue

def character_sheet():
    print(f"Name: {new_character.name}; Class: {playerClass}")
    print(f"Ability Scores: STR: {playerStrength}; DEX: {playerDexterity}; CON: {playerConstitution}; INT: {playerIntelligence}; WIS: {playerWisdom}; CHR: {playerCharisma}")
    print(f"hp: {playerHitPoints}")
    print(f"""Saving Throws:
      Death Ray or Poison: {playerSavingThrows[0]}
      Magic Wands: {playerSavingThrows[1]}
      Paralysis or Turn to Stone: {playerSavingThrows[2]}
      Dragon Breath: {playerSavingThrows[3]}
      Rods, Staves, or Spells: {playerSavingThrows[4]}""")
    print(f"XP: {playerExperience}")
    #print(f"PP: {playerPP}; GP: {playerGP}; EP: {playerEP}; SP: {playerSP}; CP: {playerCP}")
    print(f"GP: {playerGP}; EP: {playerEP}; SP: {playerSP}; CP: {playerCP}")
    #print(f"Gems: {playerGems}; Gems Value: {playerGemValue}")

character_sheet()
#     def calculate_hit_points(self):
#         # Calculate hit points based on class and level
#         if self.class_ == 'Cleric' or self.class_ == 'Magic-User':
#             self.hit_points = 4
#         elif self.class_ == 'Fighter':
#             self.hit_points = 8
#         elif self.class_ == 'Thief':
#             self.hit_points = 6
#             
#     def calculate_proficiency_bonus(self):
#         # Calculate proficiency bonus based on level
#         if self.level < 5:
#             self.proficiency_bonus = 2
#         elif self.level < 9:
#             self.proficiency_bonus = 3
#         elif self.level < 13:
#             self.proficiency_bonus = 4
#         elif self.level < 17:
#             self.proficiency_bonus = 5
#         else:
#             self.proficiency_bonus = 6
#             
#     def add_weapon(self, weapon):
#         # Add a weapon to the character's inventory
#         self.weapons.append(weapon)
#         
#     def add_equipment(self, item):
#         # Add an item of equipment to the character's inventory
#         self.equipment.append(item)
#         
#     def add_treasure(self, treasure):
#         # Add treasure to the character's inventory
#         self.treasure.append(treasure)
#         
#     def gain_experience_points(self, experience_points):
#         # Gain experience points
#         self.experience_points += experience_points
#         self.level_up()
#         
#     def level_up(self):
#         # Level up if the character has enough experience points
#         if self.experience_points >= 1000 * self.level:
#             self.level += 1
#             self.experience_points = 0
#             print(f'{self.name} has reached level {self.level}!')
#             self.calculate_hit_points()
#             self.calculate_proficiency_bonus()
# 
# 
# 