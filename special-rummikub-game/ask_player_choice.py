
class PlayerChoiceHandler:
    def __init__(self):
        pass

    def ask_player_choice(self, player_tiles):
        print("Your Tiles:")
        for idx, tile in enumerate(player_tiles):
            print(f"{idx + 1}: {tile}")
        print("1. Order my serials(PER):")
        print("2. Order my pairs(CIFT):")
        print("3. Drop your serials on the ground:")
        print("4. Drop your pairs on the ground:")
        print("5. Drop the tile which you dont want to have:")
        list_choice = input("Which one do you want to do:")
        while not list_choice.isdigit() or int(list_choice) < 1 or int(list_choice) > 5:
            list_choice = input(
                "Invalid input. Please enter the number of the options you want to choose ")

        return int(list_choice)  # Adjusting for 0-based indexing

    def pair_finding(self, player_tiles):
        # Your implementation of pair_finding method here
        pass
