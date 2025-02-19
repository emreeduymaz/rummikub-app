import random


def generate_combinations():
    colors = ['red', 'blue', 'green', 'black']
    numbers = list(range(1, 14))
    tiles = [{'color': color, 'number': number} for color in colors for number in numbers]
    alltiles = []
    for tile in tiles:
        alltiles.append(tile)
        alltiles.append(tile)

    return alltiles


def distribute_tiles(tiles, num_players):
    # Mix Tiles
    random.shuffle(tiles)

    chosen_tile = random.choice(tiles)  # Random tile in tiles for choosing okey
    tiles.remove(chosen_tile)  # Removing chosen tile from tiles
    chosen_color = chosen_tile['color']
    chosen_number = chosen_tile['number']  # Defined chosen tile's color and number
    chosen_number = chosen_number + 1  # Increment one to find our okey tile
    okey_tile = {'color': chosen_color, 'number': chosen_number}  # Assign the okey to okey_tile
    print(f"Okeyimiz:")
    print(okey_tile)
    print()

    # Mixed Tiles List
    distributed_tiles = []

    # Giving 15 tiles to chosen player
    starting_player = random.randint(0, num_players - 1)
    starting_tiles = tiles[:15]
    distributed_tiles.append(starting_tiles)
    tiles = tiles[15:]
    # Distribute tiles to players except chosen player
    current_player = starting_player
    for _ in range(1, num_players):
        player_tiles = tiles[:14]
        distributed_tiles.append(player_tiles)
        tiles = tiles[14:]

        # After one distribution, distribute tiles to next player
        current_player = (current_player + 1) % num_players

    return distributed_tiles


def bot_play(player_tiles, ground_tiles):
    pull_tile = random.choice(ground_tiles)
    ground_tiles.remove(pull_tile)
    player_tiles.append(pull_tile)
    # Randomly select a tile to play
    drop_tile = random.choice(player_tiles)
    player_tiles.remove(drop_tile)
    print(f"Bot played: {drop_tile}")
    return drop_tile


def ask_player_choice(player_tiles, last_tile):
    print("Your Tiles:")
    for idx, tile in enumerate(player_tiles):
        print(f"{idx + 1}: {tile}")

    choice = input(
        "Which tile do you want to play? Enter the number of the tile: ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(player_tiles):
        choice = input(
            "Invalid input. Please enter the number of the tile you want to play: ")

    return int(choice) - 1  # Adjusting for 0-based indexing


def start_game(players_tiles, ground_tiles):

    num_players = len(players_tiles)
    starting_player = 0  # The player who received the initial 15 tiles starts the game
    print(f"Starting Player: {starting_player}")

    current_player = starting_player
    last_tile = None
    while True:
        player_tiles = players_tiles[current_player]
        print(f"\nPlayer {current_player}'s Turn")

        if current_player == 0:  # If it's your turn
            if last_tile is not None:
                take_last_tile = input(
                    f"Do you want to take the last tile played by the previous player? ({last_tile}) [yes/no]: ")
                if take_last_tile.lower() == 'yes':
                    player_tiles.append(last_tile)
                    print(f"You took the last tile: {last_tile}")
                elif take_last_tile.lower() == 'no':
                    pull_tile = random.choice(ground_tiles)
                    ground_tiles.remove(pull_tile)
                    player_tiles.append(pull_tile)
                    print(f"You took the tile on the ground: {last_tile}")
                    for tile in ground_tiles:
                        print(tile)

            choice_idx = ask_player_choice(player_tiles, last_tile)
            if choice_idx is not None:
                if choice_idx == 'take_last':
                    player_tiles.append(last_tile)
                    print(f"You took the last tile: {last_tile}")
                else:
                    chosen_tile = player_tiles.pop(choice_idx)
                    print(f"You played: {chosen_tile}")
                    last_tile = chosen_tile
            else:
                print("You draw a tile.")

        else:  # If it's a bot's turn
            if last_tile is not None:
                print(f"Last tile played by Player {current_player - 1}: {last_tile}")

            drop_tile = bot_play(player_tiles, ground_tiles)
            last_tile = drop_tile

        # Logic for next player to decide whether to pick from the remaining tiles or not
        print(f"Remaining tiles for Player {current_player}: {player_tiles}")

        # Move to the next player
        current_player = (current_player + 1) % num_players


if __name__ == '__main__':
    tiles = generate_combinations()
    jokers = [{'color': 'joker', 'number': None} for _ in range(2)]
    tiles.extend(jokers)
    players_tiles = distribute_tiles(tiles, 4)

    ground_tiles = tiles.copy()  # Make a copy of all tiles
    for player_tiles in players_tiles:
        for tile in player_tiles:
            if tile in ground_tiles:
                ground_tiles.remove(tile)
    for tile in ground_tiles:
        print(tile)
    start_game(players_tiles, ground_tiles)

