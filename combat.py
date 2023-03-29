class DnDCharacter:
    # existing methods here
    
    def basic_combat_sequence(self, monster):
        print(f"A {monster.name} appears!")
        
        # Combat loop
        while True:
            # Character's turn
            character_hit = random.randint(1, 20) + self.attack_bonus()
            if character_hit >= monster.AC:
                damage = self.roll_damage()
                monster.HP -= damage
                print(f"You hit the {monster.name} for {damage} damage!")
                if monster.HP <= 0:
                    print(f"You defeated the {monster.name}!")
                    break
            else:
                print(f"You missed the {monster.name}!")
            
            # Monster's turn
            monster_hit = random.randint(1, 20) + monster.THAC0
            if monster_hit >= self.AC:
                damage = monster.damage_roll()
                self.HP -= damage
                print(f"The {monster.name} hits you for {damage} damage!")
                if self.HP <= 0:
                    print("You have been defeated!")
                    break
            else:
                print(f"The {monster.name} misses you!")
