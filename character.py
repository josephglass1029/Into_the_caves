import random

class DnDCharacter:
    def __init__(self, name, race, class_):
        self.name = name
        self.race = race
        self.class_ = class_
        self.level = 1
        self.strength = self.roll_stat()
        self.dexterity = self.roll_stat()
        self.constitution = self.roll_stat()
        self.intelligence = self.roll_stat()
        self.wisdom = self.roll_stat()
        self.charisma = self.roll_stat()
        self.hit_points = 0
        self.proficiency_bonus = 0
        self.weapons = []
        self.equipment = []
        self.treasure = []
        self.experience_points = 0
        
        self.calculate_hit_points()
        self.calculate_proficiency_bonus()
        
    def roll_stat(self):
        # Roll 3d6 and return the total
        return sum(random.randint(1, 6) for _ in range(3))
        
    def calculate_hit_points(self):
        # Calculate hit points based on class and level
        if self.class_ == 'Cleric' or self.class_ == 'Magic-User':
            self.hit_points = 4
        elif self.class_ == 'Fighter':
            self.hit_points = 8
        elif self.class_ == 'Thief':
            self.hit_points = 6
            
    def calculate_proficiency_bonus(self):
        # Calculate proficiency bonus based on level
        if self.level < 5:
            self.proficiency_bonus = 2
        elif self.level < 9:
            self.proficiency_bonus = 3
        elif self.level < 13:
            self.proficiency_bonus = 4
        elif self.level < 17:
            self.proficiency_bonus = 5
        else:
            self.proficiency_bonus = 6
            
    def add_weapon(self, weapon):
        # Add a weapon to the character's inventory
        self.weapons.append(weapon)
        
    def add_equipment(self, item):
        # Add an item of equipment to the character's inventory
        self.equipment.append(item)
        
    def add_treasure(self, treasure):
        # Add treasure to the character's inventory
        self.treasure.append(treasure)
        
    def gain_experience_points(self, experience_points):
        # Gain experience points
        self.experience_points += experience_points
        self.level_up()
        
    def level_up(self):
        # Level up if the character has enough experience points
        if self.experience_points >= 1000 * self.level:
            self.level += 1
            self.experience_points = 0
            print(f'{self.name} has reached level {self.level}!')
            self.calculate_hit_points()
            self.calculate_proficiency_bonus()
