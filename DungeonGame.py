import os
import sys

  #Class for an array-based queue (used for enemies)
class Queue: 
  def __init__(self):
    self.array=[]
  #Adds an enemy to the back of the queue
  def enqueue(self, enemy):
    self.array.append(enemy)
  #Removes and returns the enemy from the fron of the queue
  def dequeue(self):
    self.array.pop(0)
  #Returns, but does not remove, enemy from front of queue
  def peek(self):
    return self.array[0]
  #Checks if queue is empty. Returns true if it is, false otherwise
  def isEmpty(self):
    return len(self.array)==0
  #Returns length of queue
  def getLength(self):
    return len(self.array)



def clear_screen(): #
    os.system('cls' if os.name=='nt' else 'clear')

    # Start screen for the game. Will advance to character creation once player hits 'Enter'
def title_screen(): #
  print(r"""     
          _____
          |    |  |    |  |\    |  ------  ------  -----  |\    |
          |    |  |    |  | \   |  |       |      |     | | \   |
          |    |  |    |  |  \  |  |  ___  |_____ |     | |  \  |
          |    |  |    |  |   \ |  |     | |      |     | |   \ |
          -----   ------  |    \|  |_____| |_____ |_____| |    \|
      ----------------------------------------------------------------
          _____   ____  _____           _____  _____
          |       |     |         /\    |   |  |          
          |____   |__   |        /  \   |___|  |____ 
          |          |  |       /____\  |      |       
          |____   ___|  |____  /      \ |      |____          
      """)
  print('\nWelcome to the Stanislaus Dungeon! Untold power awaits inside! BUT BEWARE!\nCollect items and defeat the creatures in each room to safely claim \nthe power star for yourself!\n')
  input('Press \'Enter\' to play IF YOU DARE!: \n')

class Player:
            # Initialize player's attributes
      def __init__(self, name, player_class='', health=100, attack=20, inventory=[]): #
          self.name=name
          self.player_class=player_class
          self.health=health
          self.attack=attack
          self.inventory=inventory

          # Decrease player health by damage amount
      def take_damage(self, damage): 
          self.health-=damage

          # Perform player's attack on the enemy
      def attack_enemy(self, enemy): 
          enemy.take_damage(self.attack)

          # Add an item to player's inventory
      def grab_item(self, item):
          self.inventory.append(item)

          # Depending on what potion player uses, either health or attack will increase and 
          # the item will be removed from the player's inventory
      def use_item(self, item):
          if item=='Health Potion':
            self.health+=200
            self.inventory.remove(item)
          elif item=='Attack Potion':
            self.attack+=50
            self.inventory.remove(item)

class Enemy: 
      def __init__(self, name, health=50, attack=10):
        # Initialize enemy attributes for name, health, and attack
        self.name = name
        self.health = health
        self.attack = attack 

      def take_damage(self, damage): 
        # Decrease enemy health by damage amount dealt by player
        self.health -= damage

      def attack_player(self, player): 
        # Perform enemy's attack on the player
        player.health -= self.attack


  
class EnemyBehemoth(Enemy): 
  def __init__(self):
    super().__init__("Behemoth", health = 1200, attack = 100) 
   
  def ascii_art(self):
    print(r"""      @@ %%  %%%# #%@@%  @@@@@                      
                   @%%@@%% %#*#%#* **%**% *#%%%%#%                     
                  @@@%##%%####+*#***#*#**%#*##*#+%@@%@@@               
                 @%%%###*##%#*###%#+***#*#**##*#*%##%                  
               @@%%##%#####*#####%#*++*##%%#***%%#%%%@                 
               @%%##%#####%%###%#*+++*#%#*+****++#%%                   
         @%%#####**##*#%#%#+==#*+***#%*#*####*##*+*%          @@@@     
       %%%####**##**#**###%%%%*##*#%@#*%%###%%%%*##*%%%%#%####%@   @   
               %##**##%%%%%%%%%####%%%###%%#%%#+##**#%%%#%%%@  @@%%@   
               @#***+*##+*#%*=------=*#%%%####%%#%%#****%*##*####@     
               @%%%%%%%%#%#+=====----=*#%%*+=+++*#@%%%%#%%#%%%%@       
            %%#***+*#*#%%%#****==++=+++**%%##*+  +#%                   
         @%#**###%%%%%%##%%#*+++===*#####  %#*%#++*+#@                 
       %#*##%#+=+*%###*=*%#*+=--=++=+*##%%%%  ##%##*%                  
     %##%%%%#*==+*%#*##**%#*#+==-==+==**#*#%##   %#%                   
    @@@ @%%##*##%%%%%%%##%%####*+++*+-+##*#%%%%%                       
        @#*=+*##%%%##%%%#%%##**+=-=++*+*##%@ @@           @%%@         
         %#**%%###%%%#%%%%%%###***##*##%#*#%#**#%%@     @%*=##%%%%     
          @@%##%%@  %%###%%%#####***##%#*%#+====***%@@%#*====+*###%@   
          %##%@  @%####%%%%##%%%%##*+#%%%###*=--++**+++==+++==+*#%*#   
         %%%   @%###%%%##%%##%%%%%###%%#+==+++==+=====++**++*#%##*%#@  
        @%   %%#%%%@@%%####%%#####%%%%#*+=====+***#***#%%%###%@%##%@@  
           @%%%@  @%#%%%%%###*++*#####%%###########%%%%   @@  @##%     
           @@    @%###%#+*#+=+****######%%%%%%%%%%@           @%@      
                @%*+##%%##+----=*####==+*+**#######%@                  
                %%#**%#%%*+--=+=+*#####*+=--==+##*#%%                  
                 %%%%###***+==+*+*##%%#+++=----=*#*#%%      %%%@@      
                @%%%#+--==+***#**#*%%####*+=----=+###%@    %*#@  @@    
               %##%#+--=====+**##*#%#*##*##+===--=+###%%  @@#*%@%%     
             %#****+++====++++*###%%##*+=+==*+=---=*#*#%@@%@#*#%##% @@ 
           @%##*+=-===++**++**#*##%%###*=---=**=-==+**=*%@#%#*##**%@%@ 
         @%#%%##+---=====*####*###%%#**#**=--===++=+**-+#%%+#*##***##%@
        %#*++**+++*+++++++*##%#####%%#***##*+===+*****+*%%@#+#*******#%
       %#*++===-----=+########%#####%%#*****###*+++**+=*#%%%**#**#*#+#%
      %%#*+====++=--==+##%%%##%#######%%%%#*******#+++*#%@ %#**+##*#*#%
     %%##*++==+++===+=----=+*#%%%%%%%%@@@@%%%%##***#####%@  %#*#%*+*##%
     %%###*++++==++==------=++==*#%%@@@@%##**#%####**##%%    %%#%*=+#% 
     %%##****+==*++=====-===*====++**#%%%%####%%%#######%@     %#+-=*% 
     %###***##+**++=======--==-----=+****###%%%%%######%@   @%#*=-=+*% 
     @%##%#****##**+++++=+==+=======---=--===+==+**%%%%%####+===+=+*#% 
       %%%####**#*+++++++++++++==++==========-----==---====-==++*+*#%  
        @@%%####%##**++++++***+++*+++++++=++===+=++======+++++**#%#%@  
       @@@@@%###%%###*****+***+++**++++++**++*+++***++++*+***###%#%%   
         @@@@@@@@%%############**##*+****+++***+*##*****#*####%%@@     
             @@@@@@@%%%%###################***####%#######%%%@@@@@@    
                    @@@@@@@@@@%%%%@%%######%%####%%%%%%%@@@@@@@@@
                    """)

class EnemyGoblin(Enemy): 
  def __init__(self):
    super().__init__("Goblin", health = 400, attack = 40)

  def ascii_art(self): 
    print(r"""
        ( \  / )
        (  \/  )
         ( 00 )    <|>
          (VV)     <|>
           ^^      <|>
         __||__     |
       /|______|\  /|
      / |______| \/ |
     /  -|____|-
    /     |  |
          |  |
          |  |
         <|  |>
      """) 
  
class EnemySkeleton(Enemy): 
  def __init__(self):
    super().__init__("Skeleton", health = 300, attack = 30)
  def ascii_art(self): 
    print(r"""     
             _____
            / 0 0 \      |
            \     /      |
             |TTT|       |
             -----       |
              _|_      __|__
            /__|__\      |
          / |__|__|-----/|
         /  \__|__/      |
        /      |
               |
             /   \
            |     |
            |     |
           _|     |_

      """)
class EnemyDragon(Enemy): 
  def __init__(self):
    super().__init__("Dragon", health = 1000, attack = 50)
  def ascii_art(self): 
    print(r"""   

            /\     /\
           /^ \___/ ^\
           |  \   /  |       ______________________    ____
           |  o   o  |      /   _____________    /    /  __\
            \       /      / ____________       /    /  /
             \@  @ / _____/ __________         /____/  /   
              \__ /       \_______            /       /
                \          \_________________/       /    
                 \____  __________          ________/
                (  ) (  )         (   ) (   )
                / /  / /         /  /   /  /
              (((   (((          |  |  |  |
                                 (((   (((    
      """) 

class Room: 
  def __init__(self, name='', items=[], description=''): #
    # Initialize room attributes (room name, items in room, and description of the room).
    self.name=name
    self.items=items
    self.description=description
    # Determines which room is to the north, south, east or west of the room player is currently in
    self.north_room=None
    self.south_room=None
    self.east_room=None
    self.west_room=None
    self.previous=None
    # Initializes a queue for enemies
    self.enemyQueue=Queue()

  def enter_room(self): #
      # Implement room logic (e.g., battle, item pickup)
      # Prints the name of the room and the description
    print(f'\n\nYou are now at the {self.name}: {self.description}')

      # If there are items in the room, the following will show the available items
    if len(self.items)>0:
      print('\nYou see the following items in front of you:\n')
      for items in self.items:
        print(items)

      #If there are enemies in the room, name and picture of enemy will appear until defeated
    if self.enemyQueue.isEmpty() is False:
        print(f'\n\nYou are being attacked by a {self.enemyQueue.peek().name}!!!')
        self.enemyQueue.peek().ascii_art()


  def set_north(self, room): 
    self.north_room=room

  def set_south(self, room):
    self.south_room=room

  def set_east(self, room):
    self.east_room=room

  def set_west(self, room):
    self.west_room=room

  def set_prev(self, room):
    self.previous=room

class DungeonGame: 
  def __init__(self): 
# Initializes the game (player, current room, current enemy, what the player types in for a command, and the result of the command)
    self.player = Player('')
    self.current_room = Room('')
    self.rooms = []
    self.enemy=Enemy('',0,0)
    self.player_action=''
    self.result='(The results of your previous action will be displayed here.)'

  def player_input(self): #
# Prompting the player for a command. The command will be split into different words using the 'split()' function
    self.player_action=input('\nWhat will you do now?: ')
    self.player_action=self.player_action.split(' ')

  def create_player(self, name, player_class, health, attack): #
  # Creating a new player based on what the user entered as a name and choice of class (mage, warrior, battlemage)
    self.player=Player(name, player_class, health, attack)

    #Function to manage traversing through levels  #
  def game_layout(self): # (EDDY-Room Descriptions)
      #Each room is an object of the 'Room' class. Each room's argument includes a name, items in the room, and the description
    entrance=Room('Entrance',['Health Potion'], '\nThe entrance is guarded by a rusty metal gate.')
    court_yard=Room('Courtyard', ['Health Potion', 'Attack Potion'], '\nThe courtyard blows a crisp and cold air\nwith the sounds of a fountain trickling water.')
    haunted_manor=Room('Haunted Manor', [], '\nEntering the Haunted Manor, it gives an eerie atmosphere.\nDim lights shine in the distance')
    goblin_den=Room('Goblin Den', ['Health Potion', 'Attack Potion'], '\nGreen slime seeps from the ceiling.')
    dragon_lair=Room("Dragon's Lair", ['Health Potion'], '\nDeep in the dungeon, a dragon lurks\noccupying the riches and gold of the lair.')
    behemoth_tower=Room("Behemoth's Tower", [], '\nAT the very top of the dungeon,\nMist covers the tower hiding a nightmaric beast.')
    graveyard=Room('Graveyard', ['Attack Potion'], '\nYou see several tombstones. And the very ground seems to be moving...')
    library=Room('Abandoned Library', ['Health Potion'], '\nYou see a large library that seems to be from centuries ago.\nAll the books are worn and dusty.')
    exit=Room('Exit', [], '')

      #
  #Depending on which direction the player chooses to move when inside a certain room, will move character to another room
    entrance.set_east(court_yard)
    entrance.set_south(graveyard)
    entrance.set_prev(entrance)
    graveyard.set_north(entrance)
    graveyard.set_prev(entrance)
    court_yard.set_north(library)
    court_yard.set_west(entrance)
    court_yard.set_prev(entrance)
    haunted_manor.set_east(dragon_lair)
    haunted_manor.set_north(library)
    haunted_manor.set_prev(library)
    library.set_south(haunted_manor)  
    library.set_prev(court_yard)    
    dragon_lair.set_west(haunted_manor)
    dragon_lair.set_south(behemoth_tower)
    dragon_lair.set_prev(haunted_manor)
    behemoth_tower.set_north(dragon_lair)
    behemoth_tower.set_prev(dragon_lair)
    behemoth_tower.set_east(exit)

      #
      #Enemy queue for graveyard
    graveyard.enemyQueue.enqueue(EnemySkeleton())
    graveyard.enemyQueue.enqueue(EnemySkeleton())
      #Enemy queue for Courtyard
    court_yard.enemyQueue.enqueue(EnemyGoblin())
    court_yard.enemyQueue.enqueue(EnemySkeleton())
      #Enemy queue for Haunted Manor
    haunted_manor.enemyQueue.enqueue(EnemyGoblin())
    haunted_manor.enemyQueue.enqueue(EnemySkeleton())
    haunted_manor.enemyQueue.enqueue(EnemySkeleton())
      #Enemy queue for Abandonded Library
    library.enemyQueue.enqueue(EnemySkeleton())
    library.enemyQueue.enqueue(EnemySkeleton())
      #Enemy queue for Goblin's Den
    goblin_den.enemyQueue.enqueue(EnemyGoblin())
    goblin_den.enemyQueue.enqueue(EnemyGoblin())
      #Enemy queue for Dragon's Lair
    dragon_lair.enemyQueue.enqueue(EnemyGoblin())
    dragon_lair.enemyQueue.enqueue(EnemySkeleton())
    dragon_lair.enemyQueue.enqueue(EnemyDragon())
      #Enemy queue for Behemoth's Tower
    behemoth_tower.enemyQueue.enqueue(EnemySkeleton())
    behemoth_tower.enemyQueue.enqueue(EnemyGoblin())
    behemoth_tower.enemyQueue.enqueue(EnemyBehemoth())

    #Initializes current room to start at the entrance
    self.current_room=entrance
    

#Function for how players move around different rooms. If room does not exist, then will return 0, meaning player cannot go that way
  def move(self, direction): #
    if direction == 'North' and self.current_room.north_room is not None:
      self.current_room=self.current_room.north_room
    elif direction=='South' and self.current_room.south_room is not None:
      self.current_room=self.current_room.south_room
    elif direction=='East' and self.current_room.east_room is not None:
      self.current_room=self.current_room.east_room
    elif direction=='West' and self.current_room.west_room is not None:
      self.current_room=self.current_room.west_room
    else:
      return 0
    

  def instructions(self): #
        # Displays player's current status and the controls for the game.
        print()
        print('-'*60)
        print(f'Name: {self.player.name.title()}')
        print(f'Class: {self.player.player_class}')
        print(f'Current Health: {self.player.health}')
        print(f'Attack: {self.player.attack}')
        print(f'Inventory: {self.player.inventory}')
        print('-'*60)
        print('\nINSTRUCTIONS:\n\nType \'Move\' followed by \'North\', \'South\' ,\'East\', or \'West\' to move forward')
        print('Type \'Attack\' followed by the enemy name to attack')
        print('Type \'Grab\' followed by the potion name to take a potion')
        print('Type \'Use\' followed by the potion name to use a potion')
        print('Type \'Exit\' to exit the game and save your progress')

    # Player creation. Will not exit loop until one of three classes is correctly chosen (mage, warrior, battlemage)
  def player_creation(self): #
    player_name=input('\nWhat is your name?:  ')
    player_class=''
    print('\n\nPlease choose a class: \'Warrior\', \'Mage\', or \'Battlemage\'  ')
    print('\n** Warriors deal the least amount of damage, but have the most health.')
    print('\n** Mages deal the most amount of damage, but have the least amount of health.')
    print('\n** Battlemages have more health than Mages, but less than Warriors.\nThey also deal more damage than Warriors, but less than Mages.')
    while player_class!='Warrior' and player_class!='Mage' and player_class!='Battlemage':
      player_class=input('\n\nPlease type your class here:  ')
      player_class=player_class.title()
      if player_class=='Warrior' or player_class=='Mage' or player_class=='Battlemage':
        player_name=player_name.split(' ')
        print(f'\n\nWell met, {player_class} {player_name[0].title()}. Adventure awaits!')
        input('\n\nPress \'Enter\' to enter the dungeon.')
        break
      else:
        print('\nInvalid class. Please try again.\n')
      # EUGENE
      # Create player based on choice in character creation.
    if player_class=='Warrior':
      self.create_player(player_name[0], player_class, 400, 200)
    elif player_class=='Mage':
      self.create_player(player_name[0], player_class, 200, 400)
    else:
      self.create_player(player_name[0], player_class, 300, 300)


  

    #Function that manages the player's progression through the dungeon.
  def play_game(self): #

      #Player creation (player chooses name and class)
    self.player_creation() #

      #Creates all rooms in the game along with their respective enemy queues
    self.game_layout() #
    
      # Main loop for the game. If player breaks out of the loop, game will end.
    while True: #
      clear_screen()
      self.instructions()

      # Message that prints the result of player's last move
      print(f'\n\n-------------> {self.result}')
      self.current_room.enter_room()
      #Once player enters Abandoned Library, player cannot go backwards
      if self.current_room.name=='Abandoned Library':
        print('\n\nYou look back and see that several boulders have blocked your way back to the courtyard...')

        #Function to ask for player's input
      self.player_input()

          # If player chooses to grab an item and if the room has at least one item. player can pick up item
      if self.player_action[0].title()=='Grab': #
        try: #
          #If room has no potions, will tell player that there are no items
          if len(self.current_room.items)<=0:
            self.result='Nothing to grab.'
            
          #Ensures players cannot pick up items during combat
          elif self.current_room.enemyQueue.getLength()>0:
            self.result='You cannot pick up items during combat!'

          # If player at least types 'Health' or 'Attack' for the second word, player will pick up potion.
          elif self.player_action[1].title()=='Health':
            new_item='Health Potion'
            if new_item not in self.current_room.items:
              self.result='There are no Health Potions to pick up.'
            elif new_item not in self.player.inventory and new_item in self.current_room.items:
              self.player.grab_item(new_item)
              self.result=f'{new_item} added to inventory!'
              self.current_room.items.remove(new_item)
            
            # If the potion is already in the player's inventory, then player cannot pick it up
            else:
              self.result=f'Cannot carry any more {new_item}s'

          elif self.player_action[1].title()=='Attack':
            new_item='Attack Potion'
            if new_item not in self.current_room.items:
              self.result='There are no Attack Potions to pick up.'
            elif new_item not in self.player.inventory and new_item in self.current_room.items:
              self.player.grab_item(new_item)
              self.result=f'{new_item} added to inventory!'
              self.current_room.items.remove(new_item)
              
            # If the potion is already in the player's inventory, then player cannot pick it up
            else:
              self.result=f'Cannot carry any more {new_item}s'

              # If player tries to grab something that is not a health or attack potion, 
              # it will raise a TypeError and tell player that the action is not possible
          elif self.player_action[1].title()!='Health' and self.player_action[1].title()!='Attack':
            raise TypeError

            #If the player only types 'Grab' it will raise an IndexError and tell
            #player to specify what to grab
        except IndexError: #
          self.result='Please specify what you would like to grab.'

        except TypeError: #
          if self.player_action[1].title()=='Potion' or self.player_action[1].title()=='Item' or self.player_action[1].title()=='':
            self.result='Please specify which potion or item you want to grab.'
          else:
            self.result=f'Cannot grab {" ".join(self.player_action[1:])}'


      # Conditional statement for when player chooses to use an item.
      elif self.player_action[0].title()=='Use': #
        try: #
          # If the player's inventory is empty, will tell player that no items are available to use
          if len(self.player.inventory)<=0:
              self.result='No items in inventory.'

          # If player at least types 'Health' for the second word, player will use health potion.
          # If the potion is not in the player's inventory, then player cannot use potion
          elif self.player_action[1].title()=='Health':
            used_item='Health Potion'
            if used_item in self.player.inventory:
              self.player.use_item(used_item)
              self.result=f'{used_item} was used!'
            else:
              self.result=f'You do not have any {used_item}s'

          # Similar logic from above applies to attack potions
          elif self.player_action[1].title()=='Attack':
            used_item='Attack Potion'
            if used_item in self.player.inventory:
              self.player.use_item(used_item)
              self.result=f'{used_item} was used!'
            else:
              self.result=f'You do not have any {used_item}s'

          elif self.player_action[1].title()!='Health' and self.player_action[1].title()!='Attack':
            raise TypeError

        #If no item name is given, will ask player to be specific
        except IndexError: #
          self.result='Please specify what you would like to use.'

            # If player tries to use something that is not a health or attack potion, it
            # will tell player that action is not possible
        except TypeError: #
          if self.player_action[1].title()=='Potion' or self.player_action[1].title()=='Item' or self.player_action[1].title()=='':
            self.result='Please specify which potion or item you want to use'
          else:
            self.result=f'Cannot use {" ".join(self.player_action[1:])}'

          # Conditional statement for when player chooses to move a direction.
      elif self.player_action[0].title()=='Move': #
        try: #
              # If the player tries to leave during combat, it will tell the player that it is not possible
            # since there are still enemies in the enemy queue
          if self.current_room.enemyQueue.getLength()>0:
            self.result='You cannot leave while there are enemies!'
            
              # If player reaches final level and moves in the correct direction, player will exit dungeon
              # and game will end.
          
            if self.current_room.name=='Exit': # (Star)
                print(r"""   

                                       @@@@                             
                                       @@@@                             
                                    @@@*::*@@@                          
                                    @@@*::*@@@                          
                                    @@@*::*@@@                          
                                 @@@*--::::--*@@@                       
                                 @@@*::::::::*@@@                       
                                 @@@*::::::::*@@@                       
                   @@@@@@@@@@@@@@#*+=::::::::=+*#@@@@@@@@@@@@@@@        
                  @@@@@@@@@@@@@@@*::::::::::::::*@@@@@@@@@@@@@@@        
                  @@@%::::::::::::::+@@*::*@@+::::::::::::::%@@@        
                  @@@%==-:::::::::::+@@*::*@@+:::::::::::-==%@@@        
                     @@@#:::::::::::+@@*::*@@+:::::::::::#@@@           
                        @@@#::::::::+@@*::*@@+::::::::#@@@              
                        @@@#::::::::+@@*::*@@+::::::::#@@@              
                           @@@#::::::::::::::::::::#@@@                 
                        @@@%==-::::::::::::::::::::-==%@@@              
                        @@@#::::::::::::::::::::::::::#@@@              
                        @@@#::::::::::::::::::::::::::#@@@              
                     @@@%**+:::::::::::-++-:::::::::::+**%@@@           
                     @@@#::::::::::::::+@@+::::::::::::::#@@@           
                     @@@#::::::::+@@@@@@  @@@@@@+::::::::#@@@           
                   @@@%%*:::-----+@@@@@@  @@@@@@+-----:::*%%@@@         
                  @@@%:::::-@@@@@@              @@@@@@=:::::%@@@        
                  @@@@@@@@@@@@@@@                @@@@@@@@@@@@@@@        
                  @@@@@@@@@@                          @@@@@@@@@@ """)
                print('\n\n\nCongratulations! You safely escaped the dungeon!!!!')
                print('THE STAR OF POWER IS ALL YOURS FOR THE TAKING!!')
                sys.exit()
            else:
              #Moving player to a new room using the move() function
              self.move(self.player_action[1].title())        
              self.result=f'You move {self.player_action[1].title()} to a different area.'
              
      # If player tries to move towards an invalid direction it will raise a TypeError
          elif self.move(self.player_action[1].title())==0:
            raise TypeError
        
        #If player just types in 'Move', will ask player to be more specific
        except IndexError: #
          self.result='Please indicate which direction you want to move.'

        # If there is no room in a particular direction, then will tell player that the direction is blocked off
        except TypeError: #
          if self.player_action[1]=='':
            self.result='Please indicate which direction you want to move.'
          elif self.player_action[1].title()=='North' or self.player_action[1].title()=='South' or self.player_action[1].title()=='East' or self.player_action[1].title()=='West':
            self.result='Something is blocking that direction.'
          else:
            self.result='Invalid direction.'


      # If player chooses to Attack. 
      #
      elif self.player_action[0].title()=='Attack':
        try:
            #If the enemy queue is empty, will tell player that no enemies around to attack
          if self.current_room.enemyQueue.getLength()<=0:
            self.result='There are no enemies around to attack.'
            
          #If player does not attack a valid enemy raises TypeError
          elif self.player_action[1].title()!=self.current_room.enemyQueue.peek().name:
            raise TypeError
            
          #If player attacks a valid enemy in the room
          elif self.player_action[1].title()==self.current_room.enemyQueue.peek().name:
            self.player.attack_enemy(self.current_room.enemyQueue.peek())
            
          #Once enemy's health is below 0, enemy will be removed from enemy queue using dequeue
            if self.current_room.enemyQueue.peek().health<=0:
              self.result=f'You defeated the {self.current_room.enemyQueue.peek().name}!!'
              self.current_room.enemyQueue.dequeue()

            #If player attacks enemy, enemy will hit back immediately.
            elif self.current_room.enemyQueue.peek().health>0:
              self.current_room.enemyQueue.peek().attack_player(self.player)
              self.result=f'You attacked the {self.current_room.enemyQueue.peek().name}!\nBut it dealt {self.current_room.enemyQueue.peek().attack} damage!'
              
              # If player's health goes below 0, player is defeated
              if self.player.health<=0:
                print('\n\nYOU HAVE BEEN DEFEATED!!')
                print(r"""     
                         _____
                        / X X \      
                        \     /               
                         |TTT|                     
                         -----          
                       @       @
                        \     /
                         \   /
                          \ /
                          / \
                         /   \
                        @     @
                  """)
                sys.exit()
                  
        #IndexError if player just types 'Attack'
        except IndexError: #
          self.result='Please specify what you would like to attack.'

        #If player does not specify which enemy to attack or tries to attack invalid enemy
        except TypeError: #
          if self.player_action[1]=='' or self.player_action[1].title()=='Enemy':
            self.result='Please specify which enemy you want to attack.'
          else:
            self.result=f"You cannot attack {' '.join(self.player_action[1:])}"

        # If the player decides to exit the game and wants to save:
      if self.player_action[0].title()=='Exit': #
        break

        # If the player does not type one of the four possible moves(Move, Attack, Use, Grab) the game will ask the player to re-enter a valid command
        #
      if self.player_action[0].title()!='Move' and self.player_action[0].title()!='Attack' and self.player_action[0].title()!='Grab' and self.player_action[0].title()!='Use':
        self.result='Invalid action. Please try again.'

      
def main():
    # Displays the introduction to the game
  clear_screen() #
  title_screen() #
  
  game=DungeonGame()
  #Function that manages the player's progression through the dungeon.
  game.play_game() #


if __name__ == '__main__':
    main()
