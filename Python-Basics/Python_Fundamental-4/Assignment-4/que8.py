# Logic:
# 1. Create Player class
# 2. Create class variable player_count
# 3. Increase count whenever object is created
# 4. Display total players

class Player:

    # Class variable
    player_count = 0

    # Constructor
    def __init__(self, name, level):

        # Player details store ki
        self.name = name
        self.level = level

        # Player count increase kiya
        Player.player_count += 1

    # Display method
    def display(self):

        print("Name =", self.name)
        print("Level =", self.level)


# Objects create kiye
p1 = Player("Shrutika", 11)
p2 = Player("Pritish", 7)

# Methods call 
p1.display()
p2.display()

# Total players print kiye
print("Total Players =", Player.player_count)


# Q8: Create Player class with class variable player_count and track total created players