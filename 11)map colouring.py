
neighbors = {
    "A": ["B", "C", "D"],
    "B": ["A", "C", "E"],
    "C": ["A", "B", "D", "E"],
    "D": ["A", "C", "E"],
    "E": ["B", "C", "D"]
}
colors = ["Red", "Green", "Blue"]
region_colors = {}
def is_valid(region, color):
    for neighbor in neighbors[region]:
        if region_colors.get(neighbor) == color:
            return False
    return True
def color_map(region_list):
    if not region_list:
        return True  

    region = region_list[0]
    for color in colors:
        if is_valid(region, color):
            region_colors[region] = color
            if color_map(region_list[1:]):
                return True
            del region_colors[region]  

    return False
regions = list(neighbors.keys())
if color_map(regions):
    print("Solution:", region_colors)
else:
    print("No solution found.")
