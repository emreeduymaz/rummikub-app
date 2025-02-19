class OkeyGame:
    def __init__(self):
        self.tiles = []

    def add_tile(self, color, number):
        # Taş daha önce eklenmemişse ekle
        count = sum(1 for tile in self.tiles if tile['color'] == color and tile['number'] == number)
        if count < 2:
            self.tiles.append({'color': color, 'number': number})

    def find_PER_and_PAIR(self):
        # Taşları renk ve sayı olarak ayır
        colors = {}
        numbers = {}
        per_tiles = []
        non_per_tiles = []

        for tile in self.tiles:
            color = tile['color']
            number = tile['number']
            if color not in colors:
                colors[color] = []
            if number not in numbers:
                numbers[number] = []
            colors[color].append(number)
            numbers[number].append(color)

        # Perleri bul
        PERs = []
        for color, nums in colors.items():
            nums.sort()
            for i in range(len(nums) - 2):
                consecutive_count = 1
                for j in range(i + 1, len(nums)):
                    if nums[j] == nums[j - 1] + 1:
                        consecutive_count += 1
                    else:
                        break
                if consecutive_count >= 3:
                    # Ardışık dizileri PER olarak kabul et
                    self.tiles.remove([{'color': color, 'number': nums[k]} for k in range(i, i + consecutive_count)])
                    for tile in self.tiles:
                        print(tile)
                    per_tiles.extend([{'color': color, 'number': nums[k]} for k in range(i, i + consecutive_count)])
                else:
                    non_per_tiles.extend([{'color': color, 'number': nums[k]} for k in range(i, i + consecutive_count + 1)])

        # Çiftleri bul
        PAIRs = []
        for number, colors_list in numbers.items():
            if len(colors_list) >= 2 and len(set(colors_list)) == 1:  # Renklerin hepsi aynı mı kontrolü
                for color in colors_list:
                    PAIRs.append({'color': color, 'number': number})

        sorted_tiles = per_tiles + non_per_tiles
        return sorted_tiles, PAIRs


# Örnek kullanım
game = OkeyGame()

game.add_tile('black', 12)
game.add_tile('black', 11)
game.add_tile('red', 13)
game.add_tile('black', 13)
game.add_tile('blue', 1)
game.add_tile('blue', 4)
game.add_tile('black', 5)
game.add_tile('blue', 1)
game.add_tile('black', 9)
game.add_tile('black', 10)
game.add_tile('blue', 4)
game.add_tile('red', 6)
game.add_tile('green', 11)
game.add_tile('black', 13)
game.add_tile('red', 6)

tiles, PAIRs = game.find_PER_and_PAIR()
print("Taşlar:")
for tile in tiles:
    print(tile)
print("\nÇiftler:")
for pair in PAIRs:
    print(pair)
