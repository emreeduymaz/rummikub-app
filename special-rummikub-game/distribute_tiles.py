import random


class TileDistributor:
    def __init__(self, tiles, num_players):
        self.tiles = tiles
        self.num_players = num_players

    def distribute_tiles(self):
        # Mix Tiles
        random.shuffle(self.tiles)

        chosen_tile = random.choice(self.tiles)  # Random tile in tiles for choosing okey
        self.tiles.remove(chosen_tile)  # Removing chosen tile from tiles
        chosen_color = chosen_tile['color']
        chosen_number = chosen_tile['number']  # Defined chosen tile's color and number
        chosen_number = chosen_number + 1  # Increment one to find our okey tile
        okey_tile = {'color': chosen_color, 'number': chosen_number}  # Assign the okey to okey_tile
        print("Okeyimiz:")
        print(okey_tile)
        print()

        # Mixed Tiles List
        distributed_tiles = []

        # Giving 15 tiles to chosen player
        starting_player = random.randint(0, self.num_players - 1)
        starting_tiles = self.tiles[:15]
        distributed_tiles.append(starting_tiles)
        self.tiles = self.tiles[15:]
        # Distribute tiles to players except chosen player
        current_player = starting_player
        for _ in range(1, self.num_players):
            player_tiles = self.tiles[:14]
            distributed_tiles.append(player_tiles)
            self.tiles = self.tiles[14:]

            # After one distribution, distribute tiles to next player
            current_player = (current_player + 1) % self.num_players

        return distributed_tiles
