import sys
import random


class TankGame:
    def __init__(self, N: int = 7):
        """Create a tank game object.

        :param N: the size of the map (grid) NxN to generate for the game.
        """
        self.N = N
        # Hard-coded starting tank location is 2, 1
        self.tank_loc_x = 4
        self.tank_loc_y = 3
        self.target_tank_loc_x = 4
        self.target_tank_loc_y = 6

        self.tank = ' T '
        self.target_tank = ' O '

        # Info
        self.direction = 'down'
        self.bullet_count = 10
        self.total_shots = 0
        self.score = 100
        self.takedowns = 0
        self.right_shots = 0
        self.left_shots = 0
        self.up_shots = 0
        self.down_shots = 0

    def info(self):
        print(f'You are facing {self.direction}.')
        print(f'X: {self.tank_loc_x} \nY: {self.tank_loc_y}\n')
        print(f'Shoots Fired: {self.total_shots}')
        print(f'Shots Fired up: {self.up_shots}\nShots Fired down: {self.down_shots}\nShots Fired right: {self.right_shots}\nShots Fired left: {self.left_shots}')
    
    def print_menu(self):
        menu = ['1. Start Game', '2. Display Info', '3. Exit']
        for item in menu:
            print(item)

    def take_input(self):
        self.print_menu()
        while True:
            try:
                prompt = int(input('Enter a command (1-4): '))
                if prompt not in range(1, 5):
                    print('Invalid Command. Enter numbers between 1 - 4')
                else:
                    break
                    
            except ValueError:
                print('Invalid Command. Enter a number')
        return prompt
    
    def process_input(self):
        prompt = self.take_input()
        if prompt == 1:
            print('Game don start')
        elif prompt == 2:
            self.info()
        elif prompt == 3:
            print('Na here dem dey write name')
        elif prompt == 4:
            sys.exit()

    def print_map(self):

        """Print the current map of the game.

        Example output for a 7x7 map:
           0  1  2  3  4  5  6
        0  .  .  .  .  .  .  .
        1  .  .  T  .  .  .  .
        2  .  .  .  .  .  .  .
        3  .  .  .  .  .  .  .
        4  .  .  .  .  .  .  .
        5  .  .  .  .  .  .  .
        6  .  .  .  .  .  .  .

        where T is the location of the tank,
        where . (the dot) is an empty space on the map,
        where the horizontal axis is the x location of the tank and,
        where the vertical axis is the y location of the tank.
        """
        # Print the numbers for the x axis
        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for i in range(self.N):
            # Print the numbers for the y axis
            print(f"{i} ", end="")
            for j in range(self.N):
                if self.tank_loc_x == j and self.tank_loc_y == i:
                    print(self.tank, end="")
                elif self.target_tank_loc_x == j and self.target_tank_loc_y == i:
                    print(self.target_tank, end="")
                else:
                    print(" . ", end="")
            print()

    def left(self):
        self.tank = ' ← '
        self.direction = 'left'

    def right(self):
        self.tank = ' → '
        self.direction = 'right'

    def up(self):
        self.tank = ' ⊥ '
        self.direction = 'up'

    def down(self):
        self.tank = ' T '
        self.direction = 'down'


    def forward(self):
        error = "Out of Boundary"
        if self.direction == 'down':
            self.tank_loc_y += 1 if self.within_boundary() else print(error)
            self.score -= 10
            print(f"\nScore: {self.score}\n")
        elif self.direction == 'up':
            self.tank_loc_y -= 1 if self.within_boundary() else print(error)
            self.score -= 10
            print(f"\nScore: {self.score}\n")
        elif self.direction == 'right':
            self.tank_loc_x += 1 if self.within_boundary() else print(error)
            self.score -= 10
            print(f"\nScore: {self.score}\n")
        elif self.direction == 'left':
            self.tank_loc_x -= 1 if self.within_boundary() else print(error)
            self.score -= 10
            print(f"\nScore: {self.score}\n")
            

    def within_boundary(self):
        within_x = self.tank_loc_x > 0 and self.tank_loc_x < 6
        within_y = self.tank_loc_y > 0 and self.tank_loc_y < 6
        return within_x and within_y

    

    def set_tank_loc(self, x, y):
        self.tank_loc_x = x
        self.tank_loc_y = y
    
    def change_target_loc(self):
        while True:
            x = random.randint(0, 6)
            y = random.randint(0, 6)
            if self.target_tank_loc_x == x and self.target_tank_loc_y == y:
                continue
            else:
                self.target_tank_loc_x = x
                self.target_tank_loc_y = y
                break

    def update_info(self):
        self.bullet_count -= 1
        self.total_shots += 1
        self.score += 50
        self.takedowns += 1

    def shoot(self):
        print("\nSHOT FIRED!!!\n")
        self.total_shots += 1
        if self.direction == 'right':
            if self.tank_loc_y == self.target_tank_loc_y:
                if self.tank_loc_x < self.target_tank_loc_x:
                    self.right_shots += 1
                    self.update_info()
                    self.change_target_loc()
                    print("************ Hit! +50 points ************")
                else:
                    self.score -= 30
                    print("************ Miss! -30 ************")
            else:
                self.score -= 30
                print("************ Miss! -30 ************")
        elif self.direction == 'left':
            if self.tank_loc_y == self.target_tank_loc_y:
                if self.tank_loc_x > self.target_tank_loc_x:
                    self.left_shots += 1
                    self.update_info()
                    self.change_target_loc()
                    print("************ Hit! +50 points ************")
                else:
                    self.score -= 30
                    print("************ Miss! -30 ************")
            else:
                self.score -= 30
                print("************ Miss! -30 ************")
        elif self.direction == 'up':
            if self.tank_loc_x == self.target_tank_loc_x:
                if self.tank_loc_y > self.target_tank_loc_y:
                    self.up_shots += 1
                    self.update_info()
                    self.change_target_loc()
                    print("************ Hit! +50 points ************")
                else:
                    self.score -= 30
                    print("************ Miss! -30 ************")
            else:
                self.score -= 30
                print("************ Miss! -30 ************")
        elif self.direction == 'down':
            if self.tank_loc_x == self.target_tank_loc_x:
                if self.tank_loc_y < self.target_tank_loc_y:
                    self.down_shots += 1
                    self.update_info()
                    self.change_target_loc()
                    print("************ Hit! +50 points ************")
                else:
                    self.score -= 30
                    print("************ Miss! -30 ************")
            else:
                self.score -= 30
                print("************ Miss! -30 ************")
        print(f"\nScore: {self.score}\n")
        
                    
    # TODO: add more methods here


if __name__ == "__main__":
    # Initialize your game object
    tg = TankGame()
    # tg.process_input()

  
    # Start game loop
    while True:
        tg.print_map()
        if tg.score >= -1:
            command = input("Input a command: ")
            if command == 'go':
                tg.score -= 10
                tg.forward()
            elif command == 'right':
                tg.right()
            elif command == 'left':
                tg.left()
            elif command == 'up':
                tg.up()
            elif command == 'down':
                tg.down()
            elif command == 'info':
                tg.info()
            elif command == 'shoot':
                tg.shoot()
        else:
            print(f"\n************ GAME OVER ************\n\nTotal TakeDowns: {tg.takedowns}")
            break



        # TODO: Implement handling of commands here


  # Print Menu and prompt user input
    

    
