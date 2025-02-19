class PerFinder:
    def __init__(self):
        pass

    def per_finding(self, player_tiles):
        sets = []
        non_sets = []
        total_per_value = 0  # Create a variable to store the total pair value
        sorted_tiles = sorted(player_tiles,
                              key=lambda x: (x['number'], x['color']))  # Sort tiles by number and color
        i = 1
        current_set = [sorted_tiles[0]]  # Create a set initially
        while i < len(sorted_tiles):
            if (sorted_tiles[i]['number'] == current_set[-1]['number'] + 1 and
                    sorted_tiles[i]['color'] == current_set[-1]['color']):
                current_set.append(sorted_tiles[i])
                del sorted_tiles[i]
                # If the next tile is a consecutive piece of the current set and is of the same color, add it to the set
            if (sorted_tiles[i]['number'] == current_set[-1]['number'] and
                    sorted_tiles[i]['color'] != current_set[-1]['color']):
                current_set.append(
                    sorted_tiles[i])  # If the next tile is the same number but a different color, add it to the set.
                del sorted_tiles[i]
            else:
                if len(current_set) >= 3:
                    sets.append(current_set)  # If the set consists of at least 3 tiles, add the set
                    # Calculate the total value of the per and add it to the variable total_per_value
                    total_per_value += sum(tile['number'] for tile in current_set)
                else:
                    non_sets.extend(current_set)  # If the set does not consist at least 3 pieces, add non-pair pieces.
                current_set = [sorted_tiles[i]]  # Create a new set
                i += 1


        if len(current_set) >= 3:
            sets.append(current_set)  # Add remaining set when loop ends
            # Calculate the total value of the per and add it to the variable total_per_value
            total_per_value += sum(tile['number'] for tile in current_set)
        else:
            non_sets.extend(current_set)  # When the cycle ends, add the remaining pieces to the non-pair pieces.
        player_tiles = sets + non_sets
        return player_tiles, total_per_value  # Also return total pair value
