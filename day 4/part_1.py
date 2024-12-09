file = open('day 4/input.txt', 'r')
lines = file.readlines()
file.close()

def count_xmas(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]  # All 8 directions

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    total_count = 0
    seen_patterns = set()

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == word[0]:
                for dx, dy in directions:
                    if search_from(x, y, dx, dy):
                        coordinates = tuple((x + i * dx, y + i * dy) for i in range(word_len))
                        if coordinates not in seen_patterns:
                            seen_patterns.add(coordinates)
                            total_count += 1

    return total_count

print(count_xmas(lines))
