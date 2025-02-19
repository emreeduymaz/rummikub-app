
import distribute_tiles
import generate_combinations
import start_game


if __name__ == '__main__':
    tile_gen = generate_combinations.TileGenerator()
    tiles = tile_gen.generate_combinations()
    jokers = [{'color': 'joker', 'number': 31} for _ in range(2)]
    tiles.extend(jokers)
    tile_distributor = distribute_tiles.TileDistributor(tiles, 4)
    players_tiles = tile_distributor.distribute_tiles()

    ground_tiles = tiles.copy()  # Make a copy of all tiles
    for player_tiles in players_tiles:
        for tile in player_tiles:
            if tile in ground_tiles:
                ground_tiles.remove(tile)
    for tile in ground_tiles:
        print(tile)
    game_starter = start_game.Game()
    game_starter.start_game(players_tiles, ground_tiles)
