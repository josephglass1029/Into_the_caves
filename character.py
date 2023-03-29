import random
from money import Money

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
        self.money = Money() # create instance of Money class

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
    
    def add_experience(self, points):
        self.experience_points += points

# Create a new character
new_character = DnDCharacter.create_new_character()

# Access the character's name
print(new_character.name)

def character_sheet():
    print(f"Name: {new_character.name}; Class: {new_character.get_title}")
    print(f"Ability Scores: STR: {new_character.strength}; DEX: {new_character.dexterity}; CON: {new_character.constitution}; INT: {new_character.intelligence}; WIS: {new_character.wisdom}; CHR: {new_character.charisma}")
    print(f"hp: {new_character.hit_points}")
    print(f"""Saving Throws:
      Rods, Staves, or Spells: {new_character.fighter_saving_throws()}""")
    print(f"XP: {new_character.experience_points}")
    print(f"PP: {new_character.money.pp}; GP: {new_character.money.gp}; EP: {new_character.money.ep}; SP: {new_character.money.sp}; CP: {new_character.money.cp}")
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