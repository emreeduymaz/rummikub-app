class TileGenerator:
    def __init__(self):
        self.colors = ['red', 'blue', 'green', 'black']
        self.numbers = list(range(1, 14))
        self.tiles = [{'color': color, 'number': number} for color in self.colors for number in self.numbers]
        self.alltiles = []
        for tile in self.tiles:
            self.alltiles.append(tile)
            self.alltiles.append(tile)

    def generate_combinations(self):
        return self.alltiles