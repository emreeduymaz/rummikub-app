import random


class BotPlayer:
    def __init__(self):
        pass

    def bot_play(self, player_tiles, ground_tiles):
        pull_tile = random.choice(ground_tiles)
        ground_tiles.remove(pull_tile)
        player_tiles.append(pull_tile)
        # Randomly select a tile to play
        drop_tile = random.choice(player_tiles)
        player_tiles.remove(drop_tile)
        print(f"Bot played: {drop_tile}")
        return drop_tile
