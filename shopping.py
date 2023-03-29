class DnDCharacter:
    # existing methods here
    
    def go_shopping(self, weapons_dict, equipment_dict):
        print(f"Welcome to the shop, {self.name}!")
        print("Here's what we have in stock:")
        
        # Display weapons
        print("Weapons:")
        for weapon, cost in weapons_dict.items():
            print(f"{weapon}: {cost} gold")
        
        # Display equipment
        print("Equipment:")
        for item, cost in equipment_dict.items():
            print(f"{item}: {cost} gold")
        
        # Allow the character to buy items
        while True:
            print(f"You have {self.gold} gold.")
            choice = input("What would you like to buy? (Enter 'done' when finished) ")
            if choice == 'done':
                break
            elif choice in weapons_dict:
                cost = weapons_dict[choice]
                if self.gold >= cost:
                    self.gold -= cost
                    self.add_weapon(choice)
                    print(f"You bought a {choice} for {cost} gold!")
                else:
                    print("You don't have enough gold to buy that.")
            elif choice in equipment_dict:
                cost = equipment_dict[choice]
                if self.gold >= cost:
                    self.gold -= cost
                    self.add_equipment(choice)
                    print(f"You bought a {choice} for {cost} gold!")
                else:
                    print("You don't have enough gold to buy that.")
            else:
                print("Sorry, we don't have that in stock.")



weapons_dict = {'Longsword': 50, 'Shortbow': 25, 'Dagger': 10}
equipment_dict = {'Backpack': 2, 'Rope': 1, 'Torch': 1}

character = DnDCharacter('Gimli', 'Dwarf', 'Fighter')
character.go_shopping(weapons_dict, equipment_dict)
